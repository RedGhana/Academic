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

    first_encoder_index = 4 #0~4
    num_encoder = 1 #1~5
    encoder_handles = [0] * num_encoder #CreateHandles
    encoder_handle_index = 0 #HandlesControlIndex
    
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
        encoder_handles[encoder_handle_index] = encoder_res_handle
        encoder_handle_index += 1
        
        if success != True:
            DisplayVMXError(vmxerr);
            continue;

    try:
        while True:
            for encoder_index in range(0, num_encoder, 1):
                success, counter, vmxerr = vmx.getIO().Encoder_GetCount(encoder_handles[encoder_index])
                if success:
                    print("Encoder %d count    :  %d" % (encoder_index, counter))
                    success, encoder_direction, vmxerr = vmx.getIO().Encoder_GetDirection(encoder_handles[encoder_index])
                    if success:
                        print("Encoder %d direction:  %s" % (encoder_index, ("Forward" if (encoder_direction == vmxpi.VMXIO.EncoderForward) else "Reverse")))
                    else:
                        print("Error retrieving Encoder %d direction" % (encoder_index))
                        DisplayVMXError(vmxerr);
                else:
                    print("Error retrieving Encoder %d count" % (encoder_index))
                    DisplayVMXError(vmxerr);
            vmx.getTime().DelayMilliseconds(100)
    except KeyboardInterrupt:
        #Stop Program
        exit()

else:
    print("Error:  Unable to open VMX Client.")
    print("")
    print("        - Is pigpio (or the system resources it requires) in use by another process?")
    print("        - Does this application have root privileges?")

#Stop Program
exit()
