import clr
clr.AddReference(r'C:\Interop.ZKemKeeper.dll')  # Replace with the actual path to your Interop.ZKemKeeper.dll file
from zkemkeeper import CZKEM
import os
from win32com.client import Dispatch
import win32com.client

dwMachineNumber = 1



zk = Dispatch("zkemkeeper.ZKEM")
zk.Connect_Net('192.168.1.222', '4370')

set_time = zk.SetDeviceTime(dwMachineNumber)

if set_time is not None:
    print("Serial Number: %s" % str(set_time))
else:
    print("Failed to set time.")


#set time: (True)