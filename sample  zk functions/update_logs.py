import clr
from win32com.client import Dispatch
import win32com.client
clr.AddReference(r'C:\Interop.ZKemKeeper.dll')  # Replace with the actual path to your Interop.ZKemKeeper.dll file
from zkemkeeper import CZKEM
import sqlite3
from datetime import datetime
zk = Dispatch("zkemkeeper.ZKEM")

db_connection = sqlite3.connect('C:\laragon\www\BioTime.db')
cursor = db_connection.cursor()

# Connect to the ZK device (replace IP address and port with your values)
zk_ip = '192.168.1.235'
zk_port = '4370'
zk.Connect_Net(zk_ip, zk_port)

# Terminal-specific information
dwMachineNumber = 10  # Assuming this is the terminal ID for the current terminal
terminal_ip = '192.168.1.235'  # Replace with the IP address of the current terminal

# Get logs from the terminal
get_logs = zk.SSR_GetGeneralLogData(dwMachineNumber)
record_index = 1

while True:
    get_logs = zk.SSR_GetGeneralLogData(dwMachineNumber)
    
    if get_logs is not None:
        success, enroll_number, verify_mode, in_out_mode, year, month, day, hour, minute, second, work_code = get_logs
        if success:
            formatted_date_time = datetime(year, month, day, hour, minute, second)
            
            # Update the SQLite database with the log data
            update_query = """INSERT INTO logs (terminal_id, enroll_number, verify_mode, in_out_mode, date_time, work_code) 
                              VALUES (?, ?, ?, ?, ?, ?)"""
            
            cursor.execute(update_query, (dwMachineNumber, enroll_number, verify_mode, in_out_mode, formatted_date_time, work_code))
            
            print(f"Terminal ID: {dwMachineNumber}, Enroll Number: {enroll_number}, Verify Mode: {verify_mode}, In/Out Mode: {in_out_mode}, Date/Time: {formatted_date_time}, Workcode: {work_code} - Record inserted into the database.")
        else:
            print("No more logs.")
            break  # Break the loop if there are no more logs
    else:
        print("No more logs.")
        break  # Break the loop if there are no more logs

# Commit the changes to the database and close the connection
db_connection.commit()
db_connection.close()