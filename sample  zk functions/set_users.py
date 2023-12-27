import clr
from win32com.client import Dispatch
import win32com.client
clr.AddReference(r'C:\Interop.ZKemKeeper.dll')  # Replace with the actual path to your Interop.ZKemKeeper.dll file
from zkemkeeper import CZKEM
import sqlite3
from datetime import datetime
zk = Dispatch("zkemkeeper.ZKEM")

#db_connection = sqlite3.connect('C:\laragon\www\BioTime.db')
#cursor = db_connection.cursor()

# Connect to the ZK device (replace IP address and port with your values)
zk_ip = '192.168.1.235'
zk_port = '4370'
zk.Connect_Net(zk_ip, zk_port)

# Terminal-specific information
dwMachineNumber = 3  # Assuming this is the terminal ID for the current terminal
terminal_ip = '192.168.1.235'  # Replace with the IP address of the current terminal

dwEnrollNumber = '5'  # Replace with the desired user ID
Name = "joe soap"  # Replace with the desired user name
Password = "1234"  # Replace with the desired user password
Privilege = 0  # Replace with the desired user privilege (0 for normal user)
Enabled = True  # Replace with True/False based on whether the user account should be enabled

result = zk.SSR_SetUserInfo(dwMachineNumber,dwEnrollNumber,Name,Password,Privilege ,Enabled)

# Check the result
if result:
    print(f"User {dwEnrollNumber} added successfully.")
else:
    print(f"Failed to add user {dwEnrollNumber}.")

# Commit the changes to the database and close the connection
#db_connection.commit()
#db_connection.close()