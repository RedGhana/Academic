import imp
import sys
from time import sleep

sys.path.append('/usr/local/lib/vmxpi/')
vmxpi = imp.load_source('vmxpi_hal_python', '/usr/local/lib/vmxpi/vmxpi_hal_python.py') #VMXPi Library Load

def DisplayVMXError(vmxerr): #ErrorLog
    err_description = vmxpi.GetVMXErrorString(vmxerr)
    print(("VMXError %s:  " % (err_description)))

vmx = vmxpi.VMXPi(False,50) #RealTime, AhrsSetting
if vmx.IsOpen(): #VMXCheck (Success == True)
    v = vmx.getVersion().GetFirmwareVersion() #VersionCheck
    print(("Firmware Version:  ", v))
    
    vmxerr = 0 #InitErrorCount
    
#     #AutoSetPWMPin
#     hum_hicurrdio_output_channels, first_highcurrdio_channel_index = vmx.getIO().GetNumChannelsByType(vmxpi.HiCurrDIO); #GetHighCurrentDIOPin

    #ManualSetPWMPin
    first_highcurrdio_channel_index = 12
    hum_hicurrdio_output_channels = 8
    
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
            
            print(("PWMGeneratorOutput Channel %d activated on Resource type %s, index %d" % (dio_channel_index,\
                    vmxpi.EXTRACT_VMX_RESOURCE_TYPE(pwm_res_handle), \
                    vmxpi.EXTRACT_VMX_RESOURCE_INDEX(pwm_res_handle))))
            success, vmxerr = vmx.getIO().PWMGenerator_SetDutyCycle(pwm_res_handle, 0, 128) #Duty 50%
            if success != True:
                print(("Failed to set DutyCycle for PWMGenerator Resource %d, Port %d" % (vmxpi.EXTRACT_VMX_RESOURCE_INDEX(pwm_res_handle), 0)))
                DisplayVMXError(vmxerr)
    
    # Delay for awhile; during this time, PWM will be generated on all PWM channels.
    vmx.getTime().DelaySeconds(5)
    
    print("First HighCurrent Index: %d" %(first_highcurrdio_channel_index))
    print("Hum HighCurrent Channel: %d" %(hum_hicurrdio_output_channels))
    
    # Set all HighCurrent Low
    for dio_channel_index in range(0, handle_index, 1):
        success, vmxerr = vmx.getIO().PWMGenerator_SetDutyCycle(hicurr_handles[dio_channel_index], 0, 0) #Duty 0%
        if success != True: #DetectError
            print("Error Setting DO LOW for Digital Out Resource Index %d" % (dio_channel_index))
            DisplayVMXError(vmxerr);
else:
    print("Error:  Unable to open VMX Client.")
    print("")
    print("        - Is pigpio (or the system resources it requires) in use by another process?")
    print("        - Does this application have root privileges?")


exit()