import imp
import sys
from time import sleep

sys.path.append('/usr/local/lib/vmxpi/')
vmxpi = imp.load_source('vmxpi_hal_python', '/usr/local/lib/vmxpi/vmxpi_hal_python.py') #VMXPi Library Load

def DisplayVMXError(vmxerr): #ErrorLog
    err_description = vmxpi.GetVMXErrorString(vmxerr)
    print(("VMXError %s:  " % (err_description)))

def diff_yaw(target):
    yaw = vmx.getAHRS().GetYaw()
    result = target - yaw
    if result > 180:
        result = target - (yaw + 360)
    elif result < -180:
        result = target - (yaw - 360)
    return result

vmx = vmxpi.VMXPi(False,50) #RealTime, AhrsSetting
if vmx.IsOpen(): #VMXCheck (Success == True)
    v = vmx.getVersion().GetFirmwareVersion() #VersionCheck
    print(("Firmware Version:  ", v))
    
    vmxerr = 0 #InitErrorCount
    
    target = -45
    
    try:
        while True:
            print(diff_yaw(45))
            vmx.getTime().DelayMilliseconds(25);
            
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
