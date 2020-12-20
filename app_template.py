import wx


# Application templates


# Default template (Empty window with app title)
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


# Dorm information display template
class Info(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # Color, Font, and Style
        self.box_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        self.col1_sizer = wx.BoxSizer(wx.HORIZONTAL)

        info_font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        input_font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.vsizer.AddSpacer(20)

        # Button
        self.button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.button_sizer.AddSpacer(770)
        self.vsizer.Add(self.button_sizer)
        self.vsizer.AddSpacer(10)

        # Information
        self.col1_sizer.AddSpacer(40)

        info = wx.StaticText(self, label='Name\n\nArea\n\nSize (sq.m.)\n\nPrice (Baht/month)\n\nStatus\n\nContact',
                             style=wx.ALIGN_RIGHT)
        info.SetFont(info_font)
        self.col1_sizer.Add(info, wx.ALL)
        self.col1_sizer.AddSpacer(15)

        col2_sizer = wx.BoxSizer(wx.VERTICAL)

        self.name = wx.TextCtrl(self, size=(180, 22))
        self.name.SetFont(input_font)
        col2_sizer.Add(self.name, wx.ALL)
        col2_sizer.AddSpacer(14)

        self.area = wx.TextCtrl(self, size=(180, 22))
        self.area.SetFont(input_font)
        col2_sizer.Add(self.area, wx.ALL)
        col2_sizer.AddSpacer(14)

        self.size = wx.TextCtrl(self, size=(70, 22))
        self.size.SetFont(input_font)
        col2_sizer.Add(self.size, wx.ALL)
        col2_sizer.AddSpacer(14)

        self.price = wx.TextCtrl(self, size=(70, 22))
        self.price.SetFont(input_font)
        col2_sizer.Add(self.price, wx.ALL)
        col2_sizer.AddSpacer(14)

        self.status = wx.TextCtrl(self, size=(125, 22))
        self.status.SetFont(input_font)
        col2_sizer.Add(self.status, wx.ALL)
        col2_sizer.AddSpacer(14)

        self.contact = wx.TextCtrl(self, size=(125, 22))
        self.contact.SetFont(input_font)
        col2_sizer.Add(self.contact, wx.ALL)

        self.col1_sizer.Add(col2_sizer)

        # Image
        self.col1_sizer.AddSpacer(30)
        self.pic_sizer = wx.BoxSizer(wx.VERTICAL)

        # Back and Next Button
        self.pic_button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.pic_button_sizer.AddSpacer(350)
        self.col1_sizer.Add(self.pic_sizer)

        # Initialize
        self.vsizer.Add(self.col1_sizer)
        self.vsizer.AddSpacer(50)
        self.SetSizer(self.vsizer)


if __name__ == "__main__":
    template = Template()
    template.MainLoop()
