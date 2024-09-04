#-*- coding:utf-8 -*-
import cv2
import numpy as np
import imp
import sys

sys.path.append('/usr/local/lib/vmxpi/')
vmxpi = imp.load_source('vmxpi_hal_python', '/usr/local/lib/vmxpi/vmxpi_hal_python.py') #VMXPi Library Load

# 赤色の検出
def detect_red_color(img):
    # HSV色空間に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 赤色のHSVの値域1
    hsv_min = np.array([0,130,120])
    hsv_max = np.array([30,255,255])
    mask1 = cv2.inRange(hsv, hsv_min, hsv_max)

    # 赤色のHSVの値域2
    hsv_min = np.array([150,130,120])
    hsv_max = np.array([179,255,255])
    mask2 = cv2.inRange(hsv, hsv_min, hsv_max)

    # 赤色領域のマスク（255：赤色、0：赤色以外）
    mask = mask1 + mask2

    # マスキング処理
    masked_img = cv2.bitwise_and(img, img, mask=mask)

    return mask, masked_img

# 緑色の検出
def detect_green_color(img):
    # HSV色空間に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 緑色のHSVの値域1
    hsv_min = np.array([30, 64, 0])
    hsv_max = np.array([90,255,255])

    # 緑色領域のマスク（255：赤色、0：赤色以外）
    mask = cv2.inRange(hsv, hsv_min, hsv_max)

    # マスキング処理
    masked_img = cv2.bitwise_and(img, img, mask=mask)

    return mask, masked_img

# 青色の検出
def detect_blue_color(img):
    # HSV色空間に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 青色のHSVの値域1
    hsv_min = np.array([90, 64, 0])
    hsv_max = np.array([150,255,255])

    # 青色領域のマスク（255：赤色、0：赤色以外）
    mask = cv2.inRange(hsv, hsv_min, hsv_max)

    # マスキング処理
    masked_img = cv2.bitwise_and(img, img, mask=mask)

    return mask, masked_img

# ハフ変換
def detect_circle(img):
    # ハフ変換を用いた円検出
    # ぼかし処理
    kernel = (7 * 2) + 1
    img = cv2.GaussianBlur(img, (kernel, kernel), None)
    # HoughCircles関数を使用して円を検出
    circles = cv2.HoughCircles(img, 
                            cv2.HOUGH_GRADIENT, 
                            dp=1.2, 
                            minDist=20, 
                            param1=120, 
                            param2=30, 
                            minRadius=0, 
                            maxRadius=100)
    if circles is not None:
        # 検出成功

        # circles変数をfloatからintに変換
        circles = np.uint16(np.around(circles))

        circle = circles[0, (np.argmax(circles, axis=1)[0,2]) ]
        return circle[0], circle[1], circle[2]  #X, Y, R
    return None, None, None


### VMX ###
def DisplayVMXError(vmxerr): #ErrorLog
    err_description = vmxpi.GetVMXErrorString(vmxerr)
    print(("VMXError %s:  " % (err_description)))

###IMU Func
def diff_yaw(target):
    yaw = vmx.getAHRS().GetYaw()
    result = target - yaw
    if result > 180:
        result = target - (yaw + 360)
    elif result < -180:
        result = target - (yaw - 360)
    return result

###MotorFunc
def set_pwm(handle, low, high):
    success, vmxerr = vmx.getIO().PWMGenerator_SetDutyCycle(motor_handles[handle], low, high)
    if success != True: #DetectError
        print("Error Setting DO LOW for Digital Out Motor")
        DisplayVMXError(vmxerr)
def motor(motor, direction, duty):
    if duty > 100 :
        duty = 100
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
    # motor(1, 'back', duty / 2)
    motor(1, 'back', 0)
def left(duty):
    # motor(0, 'forward', duty / 2)
    motor(0, 'forward', 0)
    motor(1, 'back', duty)
def turn_right(duty):
    motor(0, 'forward', duty)
    motor(1, 'forward', duty)
def turn_left(duty):
    motor(0, 'back', duty)
    motor(1, 'back', duty)
def r_forward(duty):
    motor(0, 'forward', duty)
def r_back(duty):
    motor(0, 'back', duty)
def r_stop():
    motor(0, 'forward', 0)
def l_forward(duty):
    motor(1, 'back', duty)
def l_back(duty):
    motor(1, 'forward', duty)
def l_stop():
    motor(1, 'back', 0)

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
            DisplayVMXError(vmxerr)
            return counter, None
    else:
        print("Error retrieving Encoder %d count" % (encoder_index))
        DisplayVMXError(vmxerr)
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
            DisplayVMXError(vmxerr)
            continue
        encoder_handles[encoder_motor_handle_index] = encoder_res_handle
        encoder_motor_handle_index += 1
        
        if success != True:
            DisplayVMXError(vmxerr)
            continue

    ###SetupMotor
    first_motor_channel_index = 13 #FirstMotorPinNum
    motor_pin_counts = 4    #MotorPinCount
    
    supports_output = vmx.getIO().ChannelSupportsCapability(first_motor_channel_index, vmxpi.DigitalOutput) #CheckHighCurrentPin Input OR Output
    print(("MotorChannel Header Direction:  %s" % ("Output" if (supports_output) else "Input")))
    
    if supports_output != True: #HighCurrentPin is Input
        motor_pin_counts = 0
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

    # camera open
    camera = cv2.VideoCapture(0)
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    height, width = frame.shape[:2]
    center = width / 2
    max_size = 75
    print(f'Height: {height}, Width: {width}')

    try:
        while True:
            # 入力画像の読み込み
            _, frame = camera.read()

            # 色検出（赤、緑、青）
            red_mask, red_masked_img = detect_red_color(frame)
            # green_mask, green_masked_img = detect_green_color(frame)
            # blue_mask, blue_masked_img = detect_blue_color(frame)

            # 結果を出力
            circle_x, circle_y, circle_r = detect_circle(red_mask)
            # 検出成功
            if circle_x is not None:
                # 円周を描画
                cv2.circle(frame, (circle_x, circle_y), circle_r, (0, 255, 0), 3)

                # 中心点を描画
                cv2.circle(frame, (circle_x, circle_y), 1, (0, 255, 255), 2)
                print("中心点: X: %d \tY:%d\t半径: %d" %(circle_x, circle_y, circle_r))

                # モータ制御
                if circle_r < max_size:
                    if circle_x < (center - 80):
                        diff_center = center - circle_x
                        print("左:\t%.2f" %(diff_center))
                        turn_left(40)
                        # left( (0.3125 * diff_center) + 10 )
                    elif circle_x > (center + 80):
                        diff_center = circle_x - center
                        print("右:\t%.2f" %(diff_center))
                        turn_right(40)
                    else:
                        print("前進")
                        forward(40)
                        # forward( ((100 / max_size) * circle_r) + 10)
                else:
                    print("接近")
                    stop_motor()
            else:
                print("未検出\n\n")
                turn_right(40)
            vmx.getTime().DelayMilliseconds(10)
            
            cv2.imshow('video', frame)
            # cv2.imshow('video2', red_masked_img)

            # 'q'キーが押されたらループから抜ける
            if cv2.waitKey(50) & 0xFF == ord('q'):
                stop_motor()
                break


        camera.release()
        cv2.destroyAllWindows()
    except KeyboardInterrupt:
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
