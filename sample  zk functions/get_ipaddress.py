import clr
clr.AddReference(r'C:\Interop.ZKemKeeper.dll')  # Replace with the actual path to your Interop.ZKemKeeper.dll file
from zkemkeeper import CZKEM
import os
from win32com.client import Dispatch
import win32com.client

dwMachineNumber = 1
IPAddr = str()

zk = Dispatch("zkemkeeper.ZKEM")
zk.Connect_Net('192.168.1.222', '4370')

ip_address = zk.GetDeviceIP(dwMachineNumber,IPAddr)

if ip_address is not None:
    print("Ip Address : %s" % str(ip_address))
else:
    print("Failed to retrieve ip_address .")
	
	
#Ip Address : (True, '192.168.1.222')