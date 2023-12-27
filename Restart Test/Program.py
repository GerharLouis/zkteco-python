import clr

clr.AddReference("System.Windows.Forms")
import System.Windows.Forms as WinForms
from System.Drawing import Size, Point

from System.Windows.Forms import Application
import MainForm

Application.EnableVisualStyles()
form = MainForm.MainForm()
Application.Run(form)
