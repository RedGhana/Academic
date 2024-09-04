import imp
import sys
from time import sleep

sys.path.append('/usr/local/lib/vmxpi/')
vmxpi = imp.load_source('vmxpi_hal_python', '/usr/local/lib/vmxpi/vmxpi_hal_python.py') #VMXPi Library Load

def DisplayVMXError(vmxerr): #ErrorLog
    err_description = vmxpi.GetVMXErrorString(vmxerr)
    print(("VMXError %s:  " % (err_description)))

###AD-ConFunc
def get_analog_count(analog_index):
    success, an_in_voltage, vmxerr = vmx.getIO().Accumulator_GetAverageVoltage(analog_handles[analog_index])
    if success:
        return an_in_voltage
    else:
        print("Error getting Average Voltage of analog accumulator %d" % (analog_index))
        DisplayVMXError(vmxerr)
        return None


vmx = vmxpi.VMXPi(False,50) #RealTime, AhrsSetting
if vmx.IsOpen(): #VMXCheck (Success == True)
    v = vmx.getVersion().GetFirmwareVersion() #VersionCheck
    print(("Firmware Version:  ", v))
    
    vmxerr = 0 #InitErrorCount

    ###Setup AD Converter
    full_scale_voltage = 0
    success, full_scale_voltage, vmxerr = vmx.getIO().Accumulator_GetFullScaleVoltage()
    if success:
        print("Analog Input Voltage:  %.1f" % (full_scale_voltage))
    else:
        print("ERROR acquiring Analog Input Voltage.")
        DisplayVMXError(vmxerr)
    
    first_analog_index = 22 #22~25
    num_analog = 1 #1~4
    analog_handles = [0] * num_analog #CreateHandles
    analog_handle_index = 0 #HandlesControlIndex
    
    for analog_index in range(first_analog_index, first_analog_index + num_analog, 1):
        accum_config = vmxpi.AccumulatorConfig()
        success, res_handle, vmxerr = vmx.getIO().ActivateSinglechannelResource(vmxpi.VMXChannelInfo(first_analog_index, vmxpi.AccumulatorInput), accum_config)
        print("analog_index: ", analog_index)
        
        if success != True:
            print("Error Activating Singlechannel Resource Accumulator for Channel index %d." % (first_analog_index))
            DisplayVMXError(vmxerr)
        else:
            analog_handles[analog_handle_index] = res_handle
            analog_handle_index += 1


    try:
        while True:
            distance = get_analog_count(0)
            print(f"Distance: {distance}")
            if distance > 2.5:
                print("10cm未満")
                exit()
            vmx.getTime().DelayMilliseconds(25)
    except KeyboardInterrupt:
        exit()
else:
    print("Error:  Unable to open VMX Client.")
    print("")
    print("        - Is pigpio (or the system resources it requires) in use by another process?")
    print("        - Does this application have root privileges?")

#Stop Program
exit()
