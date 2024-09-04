import imp
import sys
from time import sleep

sys.path.append('/usr/local/lib/vmxpi/')
vmxpi = imp.load_source('vmxpi_hal_python', '/usr/local/lib/vmxpi/vmxpi_hal_python.py') #VMXPi Library Load

def DisplayVMXError(vmxerr): #ErrorLog
    err_description = vmxpi.GetVMXErrorString(vmxerr)
    print(("VMXError %s:  " % (err_description)))

def set_pwm(handle, low, high):
    success, vmxerr = vmx.getIO().PWMGenerator_SetDutyCycle(hicurr_handles[handle], low, high)
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
def init_motor(hum_hicurrdio_output_channels):
    for dio_channel_index in range(0, hum_hicurrdio_output_channels, 1):
        set_pwm(dio_channel_index, 0, 1)
    #vmx.getTime().DelayMilliseconds(10)
    #for dio_channel_index in range(0, hum_hicurrdio_output_channels, 1):
        set_pwm(dio_channel_index, 0, 0)
    #vmx.getTime().DelayMilliseconds(10)
def forward(duty):
    motor(0, 'forward', duty)
    motor(1, 'back', duty)
    motor(2, 'back', duty)
    motor(3, 'forward', duty)
def back(duty):
    motor(0, 'back', duty)
    motor(1, 'forward', duty)
    motor(2, 'forward', duty)
    motor(3, 'back', duty)
def stop_motor():
    motor(0, 'forward', 0)
    motor(1, 'forward', 0)
    motor(2, 'forward', 0)
    motor(3, 'forward', 0)
def right(duty):
    motor(0, 'forward', duty)
    motor(1, 'back', duty / 3)
    motor(2, 'back', duty / 3)
    motor(3, 'forward', duty)
def left(duty):
    motor(0, 'forward', duty / 3)
    motor(1, 'back', duty)
    motor(2, 'back', duty)
    motor(3, 'forward', duty / 3)
def turn_right(duty):
    motor(0, 'forward', duty)
    motor(1, 'forward', duty)
    motor(2, 'forward', duty)
    motor(3, 'forward', duty)
def turn_left(duty):
    motor(0, 'back', duty)
    motor(1, 'back', duty)
    motor(2, 'back', duty)
    motor(3, 'back', duty)

vmx = vmxpi.VMXPi(False,50) #RealTime, AhrsSetting
if vmx.IsOpen(): #VMXCheck (Success == True)
    v = vmx.getVersion().GetFirmwareVersion() #VersionCheck
    print(("Firmware Version:  ", v))
    
    vmxerr = 0 #InitErrorCount
    
    #SetMotorPin
    first_highcurrdio_channel_index = 13 #FirstMotorPinNum
    hum_hicurrdio_output_channels = 8    #MotorPinCount
    
    supports_output = vmx.getIO().ChannelSupportsCapability(first_highcurrdio_channel_index, vmxpi.DigitalOutput); #CheckHighCurrentPin Input OR Output
    print(("HiCurrDIO Header Direction:  %s" % ("Output" if (supports_output) else "Input")))
    
    if supports_output != True: #HighCurrentPin is Input
        hum_hicurrdio_output_channels = 0;
        print("HiCurrDIO Channels may NOT be used for PWM Generation due to jumper setting.")
    else: #HighCurrentPin is Output
        print(("HiCurrDIO Channel Indexes:  %d - %d" % (first_highcurrdio_channel_index, first_highcurrdio_channel_index + hum_hicurrdio_output_channels - 1)))

    hicurr_handles = [0] * hum_hicurrdio_output_channels #CreateHandles
    handle_index = 0 #HandlesControlIndex
    
    # Configure all HighCurrDIOs as PWM Generator Outputs.
    for dio_channel_index in range(first_highcurrdio_channel_index, first_highcurrdio_channel_index + hum_hicurrdio_output_channels, 1):
        pwmgen_cfg = vmxpi.PWMGeneratorConfig(200) #Set Frequency (Hz) to 200
        success, pwm_res_handle, vmxerr = vmx.getIO().ActivateSinglechannelResource(vmxpi.VMXChannelInfo(dio_channel_index, vmxpi.PWMGeneratorOutput), pwmgen_cfg)
        if success != True:
            print(("Error Activating Singlechannel Resource PWMGenerator for Channel index %d." % (dio_channel_index)))
            DisplayVMXError(vmxerr)
        else:
            
            hicurr_handles[handle_index] = pwm_res_handle
            handle_index += 1
    #PWM Init
    init_motor(hum_hicurrdio_output_channels)
    stop_motor()
else:
    print("Error:  Unable to open VMX Client.")
    print("")
    print("        - Is pigpio (or the system resources it requires) in use by another process?")
    print("        - Does this application have root privileges?")

#Stop Program
exit()
