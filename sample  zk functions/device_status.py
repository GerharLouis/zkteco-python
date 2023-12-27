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

    dwStatus = 12  # Data to be obtained
    dwValue = 1   # Content of the data specified by dwStatus
    
    device_status = zk.GetDeviceStatus(dwMachineNumber, dwStatus, dwValue)

    if device_status is not None:
        print("Device status:", device_status)
        
        # Print values based on dwStatus
        if dwStatus == 1:
            print("Number of administrators:", device_status)
        elif dwStatus == 2:
            print("Number of registered users:", device_status)
        elif dwStatus == 3:
            print("Number of fingerprint templates on the machine:", device_status)
        elif dwStatus == 4:
            print("Number of passwords:", device_status)
        elif dwStatus == 5:
            print("Number of operation records:", device_status)
        elif dwStatus == 6:
            print("Number of attendance records:", device_status)
        elif dwStatus == 7:
            print("Fingerprint template capacity:", device_status)
        elif dwStatus == 8:
            print("User capacity:", device_status)
        elif dwStatus == 9:
            print("Attendance record capacity:", device_status)
        elif dwStatus == 10:
            print("Remaining fingerprint template capacity:", device_status)
        elif dwStatus == 11:
            print("Remaining user capacity:", device_status)
        elif dwStatus == 12:
            print("Remaining attendance record capacity:", device_status)
        elif dwStatus == 21:
            print("Number of faces:", device_status)
        elif dwStatus == 22:
            print("Face capacity:", device_status)
        elif dwStatus == 0:
            print("Other conditions:", device_status)
        else:
            print("Unknown dwStatus value:", dwStatus)
    else:
        print("Failed to retrieve device status.")
else:
    print("Failed to connect to the machine.")

