import wx


# class Template(wx.App):
#     def __init__(self):
#         super().__init__()
#         self.frame = MyFrame(parent=None, title='RENT-A-DORM', size=(1080, 720))
#         self.frame.Center()
#         self.frame.Show()
#
#
# class MyFrame(wx.Frame):
#     def __init__(self, parent, title, size):
#         super().__init__(parent=parent, title=title, size=size)
#         self.SetMinSize(size)
#         self.SetMaxSize(size)
#
#         self.panel = MyPanel(parent=self)


class Template(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.title_panel = TitlePanel(parent=self)

        self.vpanel_box = wx.BoxSizer(wx.VERTICAL)
        self.vpanel_box.Add(self.title_panel, 0, wx.EXPAND | wx.ALL)

        self.SetSizer(self.vpanel_box)


class TitlePanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.title_font = wx.Font(32, wx.MODERN, wx.BOLD, wx.NORMAL)

        self.title_sizer = wx.BoxSizer(wx.VERTICAL)
        self.title_sizer.AddSpacer(20)

        self.title = wx.StaticText(self, label='RENT-A-DORM', style=wx.ALIGN_CENTER)
        self.title.SetFont(self.title_font)
        self.title_sizer.Add(self.title, 0, wx.ALL | wx.EXPAND)

        self.title_sizer.AddSpacer(20)
        self.SetSizer(self.title_sizer)


# class MainPanel(wx.Panel):
#     def __init__(self, parent):
#         super().__init__(parent=parent)
#         self.add_template(parent)
        #
        # # Color, Font, and Style
        # self.SetBackgroundColour('light blue')
        # self.text_font = wx.Font(22, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        # self.list_font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

if __name__ == "__main__":
    template = Template()
    template.MainLoop()
