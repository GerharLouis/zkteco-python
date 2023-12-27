import clr
clr.AddReference(r'C:\Interop.ZKemKeeper.dll')  # Replace with the actual path to your Interop.ZKemKeeper.dll file
from zkemkeeper import CZKEM
import os
from win32com.client import Dispatch
import win32com.client

dwMachineNumber = 1
IPAddr = '192.168.1.235'


zk = Dispatch("zkemkeeper.ZKEM")
zk.Connect_Net('192.168.1.222', '4370')

set_ip = zk.SetDeviceIP(dwMachineNumber,IPAddr)

if set_ip is not None:
    print("Ip Address: %s" % str(set_ip))
else:
    print("Failed to set ip address.")


#set time: (True)