import wx
import wx.lib.buttons as buttons


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


class DormListPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.SetBackgroundColour('#ea86b6')
        name_font = wx.Font(20, wx.MODERN, wx.BOLD, wx.NORMAL)
        detail_font = wx.Font(14, wx.DEFAULT, wx.BOLD, wx.NORMAL)

        self.hsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.dorm_icon = wx.Bitmap('college_town/icon.jpg')
        self.dorm_button = buttons.GenBitmapButton(self, bitmap=self.dorm_icon,
                                               size=(self.dorm_icon.GetWidth(), self.dorm_icon.GetHeight()))
        self.hsizer.Add(self.dorm_button)
        self.hsizer.AddSpacer(100)

        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        self.vsizer.AddSpacer(20)
        self.name = wx.StaticText(self, label='College Town', style=wx.ALIGN_LEFT)
        self.name.SetFont(name_font)
        self.vsizer.Add(self.name, 0, wx.EXPAND)
        self.vsizer.AddSpacer(15)

        self.hinfo_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.col1_sizer = wx.BoxSizer(wx.VERTICAL)
        self.col1_text = wx.StaticText(self, label='Area :\n\nSize :')
        self.col1_text.SetFont(detail_font)
        self.col1_sizer.Add(self.col1_text)
        self.hinfo_sizer.Add(self.col1_sizer)

        self.col2_sizer = wx.BoxSizer(wx.VERTICAL)
        self.col2_text = wx.StaticText(self, label='Ladkrabang\n\n32 sq.m.')
        self.col2_text.SetFont(detail_font)
        self.col2_sizer.Add(self.col2_text)
        self.hinfo_sizer.Add(self.col2_sizer)
        self.hinfo_sizer.AddSpacer(20)

        self.col3_sizer = wx.BoxSizer(wx.VERTICAL)
        self.col3_text = wx.StaticText(self, label='Price   :\n\nStatus :')
        self.col3_text.SetFont(detail_font)
        self.col3_sizer.Add(self.col3_text)
        self.hinfo_sizer.Add(self.col3_sizer)

        self.col4_sizer = wx.BoxSizer(wx.VERTICAL)
        self.col4_text = wx.StaticText(self, label='8000\n\nAvailable')
        self.col4_text.SetFont(detail_font)
        self.col4_sizer.Add(self.col4_text)
        self.hinfo_sizer.Add(self.col4_sizer)

        self.vsizer.Add(self.hinfo_sizer)
        self.vsizer.AddSpacer(10)

        self.hsizer.Add(self.vsizer)
        self.hsizer.AddSpacer(100)

        self.SetSizer(self.hsizer)


if __name__ == "__main__":
    template = Template()
    template.MainLoop()
