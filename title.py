import wx


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
        self.SetBackgroundColour('sky blue')

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
        self.SetBackgroundColour('light blue')
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

        # Username
        self.user_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.user_sizer.AddSpacer(350)
        self.user = wx.StaticText(self, label='Username  :')
        self.user.SetFont(self.text_font)
        self.user_sizer.Add(self.user, 0, wx.ALL)
        self.user_sizer.AddSpacer(11)

        self.user_input = wx.TextCtrl(self, size=(200, 33))
        self.user_input.SetFont(self.input_font)
        self.user_input.SetMaxLength(10)
        self.user_sizer.Add(self.user_input, 0, wx.ALL)
        self.vsizer.Add(self.user_sizer, 0, wx.ALL)
        self.vsizer.AddSpacer(10)

        # Password
        self.pw_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.pw_sizer.AddSpacer(350)
        self.pw = wx.StaticText(self, label='Password   :')
        self.pw.SetFont(self.text_font)
        self.pw_sizer.Add(self.pw, 0, wx.ALL)
        self.pw_sizer.AddSpacer(10)

        self.pw_input = wx.TextCtrl(self, size=(200, 33), style=wx.TE_PASSWORD)
        self.pw_input.SetFont(self.input_font)
        self.pw_input.SetMaxLength(10)
        self.pw_sizer.Add(self.pw_input, 0, wx.ALL)
        self.vsizer.Add(self.pw_sizer, 0, wx.ALL)
        self.vsizer.AddSpacer(10)

        # Create Acc button
        self.button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.create_button = wx.Button(self, label="Create New Account", size=(235, 50))
        self.button_sizer.Add(self.create_button, 0, wx.ALL)
        self.button_sizer.AddSpacer(23)

        self.create_button.Bind(wx.EVT_BUTTON, self.createClicked)

        # Log In button
        self.logIn_button = wx.Button(self, label="Log In", size=(115, 50))
        self.button_sizer.Add(self.logIn_button, 0, wx.ALL)
        self.vsizer.Add(self.button_sizer, 0, wx.ALL | wx.ALIGN_CENTER)

        self.logIn_button.Bind(wx.EVT_BUTTON, self.logInClicked)

        # Initialize
        self.vsizer.AddSpacer(115)
        self.SetSizer(self.vsizer)

    def createClicked(self, event):
        self.create_button = event.GetEventObject().GetLabel()
        print("Label of pressed button = ", self.create_button)

    def logInClicked(self, event):
        self.logIn_button = event.GetEventObject().GetLabel()
        print("Label of pressed button = ", self.logIn_button)


if __name__ == '__main__':
    title = Title()
    title.MainLoop()
