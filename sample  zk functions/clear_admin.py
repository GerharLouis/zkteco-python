import clr
from win32com.client import Dispatch

clr.AddReference(r'C:\Interop.ZKemKeeper.dll')  # Replace with the actual path to your Interop.ZKemKeeper.dll file

dwMachineNumber = 1


zk = Dispatch("zkemkeeper.ZKEM")

# Update the IP address and port number accordingly
ip_address = '192.168.1.235'
port_number = 4370

# Connect to the machine using the specified IP address and port number
connection_result = zk.Connect_Net(ip_address, port_number)

# Check the connection result
if connection_result:
    print("Connected to the machine successfully.")
    
    # Now you can use other methods, such as GetSerialNumber etc...
    clear_admin = zk.ClearAdministrators(dwMachineNumber)

    if clear_admin is not None:
        print("administrators cleared")
    else:
        print("Failed to clear administartors.")
else:
    print("Failed to connect to the machine.")