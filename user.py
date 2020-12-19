from app_template import *
from dormListPanel import DormListPanel
import wx.lib.scrolledpanel
import csv

imgdir = 'img/'
icon = '/icon.jpg'
fulliconpath = ''


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


class MyPanel(Template):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.SetBackgroundColour('#f3bad6')
        self.title_panel.SetBackgroundColour('#e05297')

        self.data_panel = DataPanel(parent=self)

        self.hpanel_box = wx.BoxSizer(wx.HORIZONTAL)
        self.hpanel_box.AddSpacer(60)

        self.vpanel_box.Add(self.data_panel)
        self.vpanel_box.Add(self.hpanel_box)


class DataPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.area = ['           ------- Select your Area -------']

        self.dorm_list = []
        with open('assets/dorm.csv', newline='') as f:
            reader = csv.reader(f)
            dormList = reader
            for row in dormList:
                self.dorm_list.append(row)

        tempset = set()
        dormname = []
        for i in self.dorm_list:
            tempset.add(i[1])
            dormname.append(i[0].lower())

        templist = []
        iconpath = {}
        for i in range(len(dormname)):
            temp = dormname[i].replace(' ', '_')
            templist.append(temp)
            iconpath[self.dorm_list[i][0]] = temp
        dormname = templist
        # print(iconpath.get(self.dorm_list[0][0]))

        for i in range(len(tempset)):
            self.area.append(tempset.pop())

        # Color, Font, and Style
        self.SetBackgroundColour('#f3bad6')
        text_font = wx.Font(22, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

        # Layout
        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        self.vsizer.AddSpacer(20)
        self.top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.top_sizer.AddSpacer(60)

        # Select Area
        area_text = wx.StaticText(self, label='Area:   ')
        area_text.SetFont(text_font)
        self.area_choice = wx.Choice(self, size=(300, 33), choices=self.area)
        # EVT
        self.area_choice.Bind(wx.EVT_CHOICE, self.areaSelected)

        self.top_sizer.Add(area_text, 0, wx.ALL)
        self.top_sizer.Add(self.area_choice, 0, wx.ALL)
        self.top_sizer.AddSpacer(375)

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

        scroll_panel = wx.lib.scrolledpanel.ScrolledPanel(self, size=(955, 500), style=wx.SIMPLE_BORDER)
        scroll_panel.SetupScrolling()
        scroll_panel.SetBackgroundColour('#fceef5')

        scroll_vsizer = wx.BoxSizer(wx.VERTICAL)
        scroll_vsizer.AddSpacer(20)

        # Dorm list
        for i in range(len(self.dorm_list)):
            full_iconpath = imgdir + iconpath.get(self.dorm_list[i][0]) + icon
            # print(full_iconpath)
            dorm_list = DormListPanel(scroll_panel, self.dorm_list[i], full_iconpath)
            scroll_vsizer.Add(dorm_list, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        scroll_panel.SetSizer(scroll_vsizer)
        self.hsizer.Add(scroll_panel)

        # Initialize
        self.vsizer.Add(self.hsizer)
        self.SetSizer(self.vsizer)

    # EVT Functions
    def areaSelected(self, event):
        obj = event.GetEventObject()
        item = obj.GetCurrentSelection()
        # print(obj.GetString(item))
        if obj.GetString(item) == "":
            pass


    def logOutClicked(self, event):
        app = self.GetParent().GetParent()
        app.Destroy()
        wx.Exit()


if __name__ == "__main__":
    user = User()
    user.MainLoop()
