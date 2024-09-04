import imp
import sys
from time import sleep

sys.path.append('/usr/local/lib/vmxpi/')
vmxpi = imp.load_source('vmxpi_hal_python', '/usr/local/lib/vmxpi/vmxpi_hal_python.py')

def DisplayVMXError(vmxerr): #ErrorLog
    err_description = vmxpi.GetVMXErrorString(vmxerr)
    print(("VMXError %s:  " % (err_description)))
    
vmx = vmxpi.VMXPi(False,50)
print("0kokomadeOK!")

if vmx.IsOpen():
    
    print("kokomadeOK!")
    
    digitalio_res_handles = [0]
    digital_output_res_handle_index = 0
    dio_channel_index = 8
    dio_config = vmxpi.DIOConfig(vmxpi.DIOConfig.PUSHPULL);
    success, res_handle, vmxerr = vmx.getIO().ActivateSinglechannelResource(vmxpi.VMXChannelInfo(dio_channel_index, vmxpi.DigitalOutput), dio_config)

    print("flexio_channel_index:", dio_channel_index, vmxpi.DigitalOutput)
    print("success:", success)
    print("res_handle:", res_handle)
    if success != True:
        print("Error Activating Singlechannel Resource DigitalOutput for Channel index %d." % (dio_channel_index))
        DisplayVMXError(vmxerr)
    else:
        digitalio_res_handles[digital_output_res_handle_index] = res_handle
        print("Digital Output Channel %d activated on Resource type %s, index %d" % (dio_channel_index,\
            vmxpi.EXTRACT_VMX_RESOURCE_TYPE(digitalio_res_handles[digital_output_res_handle_index]), \
            vmxpi.EXTRACT_VMX_RESOURCE_INDEX(digitalio_res_handles[digital_output_res_handle_index])))
    
        digital_output_res_handle_index = digital_output_res_handle_index + 1
        
    success, vmxerr = vmx.getIO().DIO_Set(digitalio_res_handles[0], True)
    
    if success != True:
        print("Error Setting DO HIGH for Digital Out Resource Index %d" % (dig_out_res_index))
        DisplayVMXError(vmxerr);

    vmx.getTime().DelayMilliseconds(500);
        
    success, vmxerr = vmx.getIO().DIO_Set(digitalio_res_handles[0], False)
    if success != True:
        print("Error Setting DO LOW for Digital Out Resource Index %d" % (dig_out_res_index))
        DisplayVMXError(vmxerr);

    vmx.getTime().DelayMilliseconds(5000);
