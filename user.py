from app_template import *
from dormListPanel import DormListPanel
import wx.lib.scrolledpanel
import csv

# User: user main system

# Get dorm icon path
imgDir = 'img/'
icon = '/icon.jpg'
fullIconPath = ''


class User(wx.App):
    def __init__(self):
        super().__init__()
        self.frame = MyFrame(parent=None, title='RENT-A-DORM', size=(1080, 720))
        self.frame.Center()
        self.frame.Show()


class MyFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super().__init__(parent=parent, title=title, size=size)
        self.SetMinSize(size)
        self.SetMaxSize(size)

        self.panel = MyPanel(parent=self)


# Set panel as default template
class MyPanel(Template):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.SetBackgroundColour('#f3bad6')
        self.title_panel.SetBackgroundColour('#e05297')

        # Display data
        self.data_panel = DataPanel(parent=self)

        self.hpanel_box = wx.BoxSizer(wx.HORIZONTAL)
        self.hpanel_box.AddSpacer(60)

        self.vpanel_box.Add(self.data_panel)
        self.vpanel_box.Add(self.hpanel_box)


class DataPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # Color, Font, and Style
        self.SetBackgroundColour('#f3bad6')

        # Layout
        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        self.vsizer.AddSpacer(20)
        self.top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.top_sizer.AddSpacer(60)

        # Log Out button
        self.logOut_button = wx.Button(self, label='Log Out', size=(200, 33))
        self.top_sizer.Add(self.logOut_button, wx.ALL)
        self.vsizer.Add(self.top_sizer)
        self.vsizer.AddSpacer(30)
        # EVT
        self.logOut_button.Bind(wx.EVT_BUTTON, self.logOutClicked)

        # Dorm List scrolled panel
        self.hsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.hsizer.AddSpacer(60)

        self.scroll_panel = wx.lib.scrolledpanel.ScrolledPanel(self, size=(955, 500), style=wx.SIMPLE_BORDER)
        self.scroll_panel.SetupScrolling()
        self.scroll_panel.SetBackgroundColour('#fceef5')

        self.scroll_vsizer = wx.BoxSizer(wx.VERTICAL)
        self.scroll_vsizer.AddSpacer(20)

        # List of dorm information
        self.dorm_list = []
        # Read every row from csv file and store in a list
        with open('assets/dorm.csv', newline='') as f:
            reader = csv.reader(f)
            dormList = reader
            for row in dormList:
                self.dorm_list.append(row)

        tempSet = set()
        # Match dorm name with directory
        self.dormName = []
        # Change dorm name to all lower case
        for i in self.dorm_list:
            tempSet.add(i[1])
            self.dormName.append(i[0].lower())

        tempList = []
        # Dictionary to store path of each icon
        self.iconPath = {}
        # Replace all space bar with _
        for i in range(len(self.dormName)):
            temp = self.dormName[i].replace(' ', '_')
            tempList.append(temp)
            self.iconPath[self.dorm_list[i][0]] = temp
        self.dormName = tempList

        # Add dorm into dorm lists
        for i in range(len(self.dorm_list)):
            # Get icon path
            full_iconPath = imgDir + self.iconPath.get(self.dorm_list[i][0]) + icon
            dorm_list = DormListPanel(self.scroll_panel, self.dorm_list[i], full_iconPath)
            self.scroll_vsizer.Add(dorm_list, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        self.scroll_panel.SetSizer(self.scroll_vsizer)
        self.hsizer.Add(self.scroll_panel)

        # Initialize
        self.vsizer.Add(self.hsizer)
        self.SetSizer(self.vsizer)

    # EVT Functions
    def logOutClicked(self, event):
        app = self.GetParent().GetParent()
        app.Destroy()
        wx.Exit()


if __name__ == "__main__":
    user = User()
    user.MainLoop()
