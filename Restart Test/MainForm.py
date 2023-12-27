import clr
from win32com.client import Dispatch
clr.AddReference("System.Windows.Forms")
clr.AddReference(r'C:\Interop.ZKemKeeper.dll')  # Replace with the actual path to your Interop.ZKemKeeper.dll file
from System.Drawing import Size, Point, Color
from System.Windows.Forms import Form, Button, FlatStyle, Label, TextBox
import System.Windows.Forms
from System.Drawing import Size, Point

dwMachineNumber = 1


zk = Dispatch("zkemkeeper.ZKEM")

class MainForm(Form):
    def __init__(self):
        super().__init__()

    
        self._btnConnect = Button()
        self._buttonRestart = Button()
        self._btnClearAdmin = Button()
        self._btnPowerOff = Button()
        self._lblDescription = Label()
        self._textBoxDescription = TextBox()
        self._textBoxIpAddress = TextBox()
        self._textBoxPort = TextBox()
        self._lblIpAddress = Label()
        self._lblPort = Label()
        self._lblStatus = Label()
        self.SuspendLayout()
        # 
        # btnConnect
        # 
        self._btnConnect.Location = Point(52, 67)
        self._btnConnect.Name = "btnConnect"
        self._btnConnect.Size = Size(75, 23)
        self._btnConnect.TabIndex = 0
        self._btnConnect.Text = "Connect"
        self._btnConnect.UseVisualStyleBackColor = True
        self._btnConnect.Click += self.BtnConnectClick
        # 
        # buttonRestart
        # 
        self._buttonRestart.Location = Point(295, 67)
        self._buttonRestart.Name = "buttonRestart"
        self._buttonRestart.Size = Size(75, 23)
        self._buttonRestart.TabIndex = 1
        self._buttonRestart.Text = "Restart"
        self._buttonRestart.UseVisualStyleBackColor = True
        self._buttonRestart.Click += self.ButtonRestartClick
        # 
        # btnClearAdmin
        # 
        self._btnClearAdmin.Location = Point(133, 67)
        self._btnClearAdmin.Name = "btnClearAdmin"
        self._btnClearAdmin.Size = Size(75, 23)
        self._btnClearAdmin.TabIndex = 2
        self._btnClearAdmin.Text = "Clear Admin"
        self._btnClearAdmin.UseVisualStyleBackColor = True
        self._btnClearAdmin.Click += self.BtnClearAdminClick
        # 
        # btnPowerOff
        # 
        self._btnPowerOff.Location = Point(214, 67)
        self._btnPowerOff.Name = "btnPowerOff"
        self._btnPowerOff.Size = Size(75, 23)
        self._btnPowerOff.TabIndex = 3
        self._btnPowerOff.Text = "Power Off"
        self._btnPowerOff.UseVisualStyleBackColor = True
        self._btnPowerOff.Click += self.BtnPowerOffClick
        # 
        # lblDescription
        # 
        self._lblDescription.Location = Point(52, 130)
        self._lblDescription.Name = "lblDescription"
        self._lblDescription.Size = Size(70, 23)
        self._lblDescription.TabIndex = 4
        self._lblDescription.Text = "Description"
        # 
        # textBoxDescription
        # 
        self._textBoxDescription.Location = Point(145, 133)
        self._textBoxDescription.Name = "textBoxDescription"
        self._textBoxDescription.Size = Size(236, 20)
        self._textBoxDescription.TabIndex = 5
        # 
        # textBoxIpAddress
        # 
        self._textBoxIpAddress.Location = Point(145, 162)
        self._textBoxIpAddress.Name = "textBoxIpAddress"
        self._textBoxIpAddress.Size = Size(129, 20)
        self._textBoxIpAddress.TabIndex = 6
        # 
        # textBoxPort
        # 
        self._textBoxPort.Location = Point(145, 194)
        self._textBoxPort.Name = "textBoxPort"
        self._textBoxPort.Size = Size(80, 20)
        self._textBoxPort.TabIndex = 7

        # 
        # lblIpAddress
        # 
        self._lblIpAddress.Location = Point(52, 162)
        self._lblIpAddress.Name = "lblIpAddress"
        self._lblIpAddress.Size = Size(70, 23)
        self._lblIpAddress.TabIndex = 8
        self._lblIpAddress.Text = "Ip Address"
        # 
        # lblPort
        # 
        self._lblPort.Location = Point(83, 197)
        self._lblPort.Name = "lblPort"
        self._lblPort.Size = Size(39, 23)
        self._lblPort.TabIndex = 9
        self._lblPort.Text = "Port"

        # 
        # lblStatus
        # 
        self._lblStatus.Location = Point(64, 271)
        self._lblStatus.Name = "lblStatus"
        self._lblStatus.Size = Size(503, 38)
        self._lblStatus.TabIndex = 10
        # 
        # MainForm
        #
        self.ClientSize = Size(695, 372)
        self.Controls.Add(self._lblStatus)
        self.Controls.Add(self._lblPort)
        self.Controls.Add(self._lblIpAddress)
        self.Controls.Add(self._textBoxPort)
        self.Controls.Add(self._textBoxIpAddress)
        self.Controls.Add(self._textBoxDescription)
        self.Controls.Add(self._lblDescription)
        self.Controls.Add(self._btnPowerOff)
        self.Controls.Add(self._btnClearAdmin)
        self.Controls.Add(self._buttonRestart)
        self.Controls.Add(self._btnConnect)
        self.Name = "MainForm"
        self.Text = "Test1"
        self.ResumeLayout(False)
        self.PerformLayout()

    def BtnConnectClick(self, sender, e):
        pass

    def BtnClearAdminClick(self, sender, e):
        pass

    def BtnPowerOffClick(self, sender, e):
        pass

    def ButtonRestartClick(self, sender, e):
        # Call the method to restart the device
        self.RestartDevice()

    def RestartDevice(self):
        # Update the IP address and port number using the TextBox values
        ip_address = self._textBoxIpAddress.Text
        port_number = int(self._textBoxPort.Text)  # Assuming the port is an integer

        # Connect to the machine using the specified IP address and port number
        connection_result = zk.Connect_Net(ip_address, port_number)

        # Check the connection result
        if connection_result:
            print("Connected to the machine successfully.")
            
            # Now you can use other methods, such as GetSerialNumber etc...
            restart_device = zk.RestartDevice(dwMachineNumber)

            if restart_device is not None:
                print("Device restarted successfully.")
            else:
                print("Failed to restart device.")
        else:
            print("Failed to connect to the machine.")

if __name__ == "__main__":
    from System.Windows.Forms import Application

    form = MainForm()
    Application.Run(form)
