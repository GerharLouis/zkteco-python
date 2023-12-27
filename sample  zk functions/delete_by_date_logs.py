import clr
from win32com.client import Dispatch

clr.AddReference(r'C:\Interop.ZKemKeeper.dll')  # Replace with the actual path to your Interop.ZKemKeeper.dll file
zk = Dispatch("zkemkeeper.ZKEM")


dwMachineNumber = 1
sTime = YYYY-MM-DD hh:mm:ss


# Update the IP address and port number accordingly
ip_address = '192.168.1.235'
port_number = 4370

# Connect to the machine using the specified IP address and port number
connection_result = zk.Connect_Net(ip_address, port_number)

if connection_result:
    print("Connected to the machine successfully.")
    
    
    delete_by_date = zk.DeleteAttlogByTim(dwMachineNumber, sTime)

    if delete_by_date is not None:
        print("logs deleted" ))
    else:
        print("Failed to delete logs.")
else:
    print("Failed to connect to the machine.")