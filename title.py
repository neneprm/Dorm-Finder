import wx
import admin
import user


class Title(wx.App):
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


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.SetBackgroundColour('#ff8364')

        self.main_panel = MainPanel(parent=self)

        self.panel_box = wx.BoxSizer(wx.VERTICAL)
        self.panel_box.AddSpacer(35)
        self.panel_box.Add(self.main_panel, 0, wx.EXPAND | wx.ALL, 30)

        # self.panel_box.Add(self.data_panel, 0, wx.EXPAND | wx.ALL)

        # self.detail_box = wx.BoxSizer(wx.HORIZONTAL)
        # self.detail_box.AddSpacer(60)
        # self.detail_box.Add(self.detail_panel, wx.EXPAND | wx.ALL)
        # self.detail_box.AddSpacer(60)
        # self.panel_box.Add(self.detail_box, wx.EXPAND | wx.ALL)

        self.SetSizer(self.panel_box)


class MainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # Color, Font, and Style
        self.SetBackgroundColour('#ffd98e')
        self.title_font = wx.Font(110, wx.MODERN, wx.BOLD, wx.NORMAL)
        self.text_font = wx.Font(28, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.input_font = wx.Font(22, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

        # Layout
        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        self.vsizer.AddSpacer(195)

        # Title
        self.title = wx.StaticText(self, label='RENT-A-DORM', style=wx.ALIGN_CENTER)
        self.title.SetFont(self.title_font)
        self.vsizer.Add(self.title, 0, wx.ALL | wx.EXPAND)
        self.vsizer.AddSpacer(10)

        self.button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.button_sizer.AddSpacer(250)

        # Admin
        self.admin_button = wx.Button(self, label="Log In as Admin", size=(235, 50), style=wx.ALIGN_CENTER)
        self.button_sizer.Add(self.admin_button, 0, wx.ALL)
        self.button_sizer.AddSpacer(50)
        # EVT
        self.admin_button.Bind(wx.EVT_BUTTON, self.adminClicked)

        # Guest
        self.guest_button = wx.Button(self, label="Log In as Guest", size=(235, 50), style=wx.ALIGN_CENTER)
        self.button_sizer.Add(self.guest_button, 0, wx.ALL)
        self.vsizer.AddSpacer(10)
        # EVT
        self.guest_button.Bind(wx.EVT_BUTTON, self.guestClicked)

        self.vsizer.Add(self.button_sizer, 0, wx.ALL)

        # Initialize
        self.vsizer.AddSpacer(180)
        self.SetSizer(self.vsizer)

    # EVT Functions
    def adminClicked(self, event):
        frame = self.GetParent()
        app = frame.GetParent()
        app.Destroy()
        wx.Exit()
        admin_app = admin.Admin()
        admin_app.MainLoop()

    def guestClicked(self, event):
        frame = self.GetParent()
        app = frame.GetParent()
        app.Destroy()
        wx.Exit()
        guest_app = user.User()
        guest_app.MainLoop()


if __name__ == '__main__':
    title = Title()
    title.MainLoop()
