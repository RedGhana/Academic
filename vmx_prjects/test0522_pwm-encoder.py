import imp
import sys
from time import sleep

sys.path.append('/usr/local/lib/vmxpi/')
vmxpi = imp.load_source('vmxpi_hal_python', '/usr/local/lib/vmxpi/vmxpi_hal_python.py') #VMXPi Library Load

def DisplayVMXError(vmxerr): #ErrorLog
    err_description = vmxpi.GetVMXErrorString(vmxerr)
    print(("VMXError %s:  " % (err_description)))


###MotorFunc
def set_pwm(handle, low, high):
    success, vmxerr = vmx.getIO().PWMGenerator_SetDutyCycle(motor_handles[handle], low, high)
    if success != True: #DetectError
        print("Error Setting DO LOW for Digital Out Motor")
        DisplayVMXError(vmxerr);
def motor(motor, direction, duty):
    pwm = int(duty * 2.55)
    pin = motor * 2
    if direction == 'forward':
        set_pwm(pin, 0, pwm)
        set_pwm((pin + 1), 0, 0)
    elif direction == 'back':
        set_pwm(pin, 0, 0)
        set_pwm((pin + 1), 0, pwm)
    else:
        print("Error: Motor%d Direction" %motor)

# FirstLowSignalBug(If the PWM initially set is Low, the correct waveform will not be formed.)
def init_motor(motor_pin_counts):
    for motor_channel_index in range(0, motor_pin_counts, 1):
        set_pwm(motor_channel_index, 0, 1)
        set_pwm(motor_channel_index, 0, 0)
def forward(duty):
    motor(0, 'forward', duty)
    motor(1, 'back', duty)
def back(duty):
    motor(0, 'back', duty)
    motor(1, 'forward', duty)
def stop_motor():
    motor(0, 'forward', 0)
    motor(1, 'forward', 0)
def right(duty):
    motor(0, 'forward', duty)
    motor(1, 'back', duty / 2)
def left(duty):
    motor(0, 'forward', duty / 2)
    motor(1, 'back', duty)
def turn_right(duty):
    motor(0, 'forward', duty)
    motor(1, 'forward', duty)
def turn_left(duty):
    motor(0, 'back', duty)
    motor(1, 'back', duty)

###EncoderFunc
def get_encoder_count(encoder_index):
    success, counter, vmxerr = vmx.getIO().Encoder_GetCount(encoder_handles[encoder_index])
    if success:
        success, motor1_direction, vmxerr = vmx.getIO().Encoder_GetDirection(encoder_handles[encoder_index])
        if success:
            if motor1_direction == vmxpi.VMXIO.EncoderForward:
                if encoder_index == 1 or encoder_index == 2:
                    result_direction = "Reverse"
                else:
                    result_direction = "Forward"
            else:
                if encoder_index == 1 or encoder_index == 2:
                    result_direction = "Forward"
                else:
                    result_direction = "Reverse"
            if encoder_index == 1 or encoder_index == 2:
                return -counter, result_direction
            else:
                return counter, result_direction
        else:
            print("Error retrieving Encoder %d direction" % (encoder_index))
            DisplayVMXError(vmxerr);
            return counter, None
    else:
        print("Error retrieving Encoder %d count" % (encoder_index))
        DisplayVMXError(vmxerr);
        return None, None

vmx = vmxpi.VMXPi(False,50) #RealTime, AhrsSetting
if vmx.IsOpen(): #VMXCheck (Success == True)
    v = vmx.getVersion().GetFirmwareVersion() #VersionCheck
    print(("Firmware Version:  ", v))
    
    vmxerr = 0 #InitErrorCount

    ###SetupEncoder
    first_encoder_index = 0 #0~4
    num_encoder = 2 #1~5
    encoder_handles = [0] * num_encoder #CreateHandles
    encoder_motor_handle_index = 0 #HandlesControlIndex
    
    for encoder_index in range(0, num_encoder, 1):
        enc_channel_a = vmxpi.VMXChannelInfo(( (first_encoder_index * 2) + (encoder_index * 2) + 0), vmxpi.EncoderAInput)
        enc_channel_b = vmxpi.VMXChannelInfo(( (first_encoder_index * 2) + (encoder_index * 2) + 1), vmxpi.EncoderBInput)
        print("encoder_index: ", encoder_index)

        enc_config = vmxpi.EncoderConfig(vmxpi.EncoderConfig.x4)
        success, res_handle, vmxerr = vmx.getIO().ActivateDualchannelResource(enc_channel_a, enc_channel_b, enc_config)
        if success != True:
            print("Error Activating Dualchannel Resource Encoder for Channel indexes %d and %d." % (enc_channel_a.index, enc_channel_b.index))
            DisplayVMXError(vmxerr)
        else:
            print("Successfully Activated Encoder Resource %d with VMXChannels %d and %d" % (encoder_index, enc_channel_a.index, enc_channel_b.index))
    #GetEncoderHandle
    for encoder_index in range (first_encoder_index, first_encoder_index + num_encoder, 1):
        success, encoder_res_handle, vmxerr = vmx.getIO().GetResourceHandle(vmxpi.Encoder, encoder_index) #encoder_index is 0~4
        print("encoder_res_handle: ", encoder_res_handle)
        if success != True:
            DisplayVMXError(vmxerr);
            continue;
        encoder_handles[encoder_motor_handle_index] = encoder_res_handle
        encoder_motor_handle_index += 1
        
        if success != True:
            DisplayVMXError(vmxerr);
            continue;

    ###SetupMotor
    first_motor_channel_index = 13 #FirstMotorPinNum
    motor_pin_counts = 4    #MotorPinCount
    
    supports_output = vmx.getIO().ChannelSupportsCapability(first_motor_channel_index, vmxpi.DigitalOutput); #CheckHighCurrentPin Input OR Output
    print(("MotorChannel Header Direction:  %s" % ("Output" if (supports_output) else "Input")))
    
    if supports_output != True: #HighCurrentPin is Input
        motor_pin_counts = 0;
        print("Motor Channels may NOT be used for PWM Generation due to jumper setting.")
    else: #HighCurrentPin is Output
        print(("Motor Channel Indexes:  %d - %d" % (first_motor_channel_index, first_motor_channel_index + motor_pin_counts - 1)))

    motor_handles = [0] * motor_pin_counts #CreateHandles
    motor_handle_index = 0 #HandlesControlIndex
    
    # Configure all HighCurrDIOs as PWM Generator Outputs.
    for motor_channel_index in range(first_motor_channel_index, first_motor_channel_index + motor_pin_counts, 1):
        pwmgen_cfg = vmxpi.PWMGeneratorConfig(200) #Set Frequency (Hz) to 200
        success, pwm_res_handle, vmxerr = vmx.getIO().ActivateSinglechannelResource(vmxpi.VMXChannelInfo(motor_channel_index, vmxpi.PWMGeneratorOutput), pwmgen_cfg)
        if success != True:
            print(("Error Activating Singlechannel Resource PWMGenerator for Channel index %d." % (motor_channel_index)))
            DisplayVMXError(vmxerr)
        else:
            
            motor_handles[motor_handle_index] = pwm_res_handle
            motor_handle_index += 1
    ###PWM Init
    init_motor(motor_pin_counts)
    # ~ forward(100)
    # ~ vmx.getTime().DelayMilliseconds(100)
#    try:
#        while True:
            #MainCode
#            motor1_count, motor1_direction = get_encoder_count(0)
#            motor2_count, motor2_direction = get_encoder_count(1)
#            print(f"Motor1:\tCounter: {motor1_count}\tDirection: {motor1_direction}")
#            print(f"Motor2:\tCounter: {motor2_count}\tDirection: {motor2_direction}")
            # ~ if motor1_count < 5000:
                # ~ forward(20)
                # ~ print("-- Forward (Duty:20%) --")
            # ~ elif motor1_count < 10000:
                # ~ right(50)
                # ~ print("-- Right (Duty:50%) --")
            # ~ elif motor1_count < 15000:
                # ~ left(75)
                # ~ print("-- Left (Duty:75%) --")
            # ~ elif motor1_count < 20000:
                # ~ turn_right(100)
                # ~ print("-- TurnRight (Duty:100%) --")
            # ~ elif motor1_count < 25000:
                # ~ stop_motor()
                # ~ print("-- MotorStop --")
                # ~ exit()
#            forward(50)
#            vmx.getTime().DelayMilliseconds(100)
#    except KeyboardInterrupt:
#        stop_motor()
#        #Stop Program
#        exit()
    forward(50)
    vmx.getTime().DelaySeconds(2)
    # back(50)
    # vmx.getTime().DelaySeconds(2)
    # left(50)
    # vmx.getTime().DelaySeconds(2)
    # right(50)
    # vmx.getTime().DelaySeconds(2)
    # turn_left(50)
    # vmx.getTime().DelaySeconds(2)
    # turn_right(50)
    # vmx.getTime().DelaySeconds(2)
    stop_motor()
    exit()

else:
    print("Error:  Unable to open VMX Client.")
    print("")
    print("        - Is pigpio (or the system resources it requires) in use by another process?")
    print("        - Does this application have root privileges?")

#Stop Program
stop_motor()
exit()
