import wx
import wx.lib.buttons as buttons
import dormview


class DormListPanel(wx.Panel):
    def __init__(self, parent, area_list, path):
        super().__init__(parent=parent)
        self.SetBackgroundColour('#ea86b6')

        self.info = area_list
        # print(self.info)

        # Color, Font, and Style
        name_font = wx.Font(20, wx.MODERN, wx.BOLD, wx.NORMAL)
        detail_font = wx.Font(14, wx.DEFAULT, wx.BOLD, wx.NORMAL)
        # print(path)

        # Layout
        # Dorm Button
        self.hsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.dorm_icon = wx.Bitmap(path)
        self.dorm_button = buttons.GenBitmapButton(self, bitmap=self.dorm_icon,
                                               size=(self.dorm_icon.GetWidth(), self.dorm_icon.GetHeight()))
        self.hsizer.Add(self.dorm_button)
        self.hsizer.AddSpacer(100)
        # EVT
        self.dorm_button.Bind(wx.EVT_BUTTON, self.dormClicked)

        # Info
        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        self.vsizer.AddSpacer(20)
        self.name = wx.StaticText(self, label=area_list[0], style=wx.ALIGN_LEFT)
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
        self.col2_text = wx.StaticText(self, label=area_list[1] + '\n\n' + area_list[2] + ' sq.m.')
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
        self.col4_text = wx.StaticText(self, label=area_list[3] + '\n\n' + area_list[4])
        self.col4_text.SetFont(detail_font)
        self.col4_sizer.Add(self.col4_text)
        self.hinfo_sizer.Add(self.col4_sizer)

        self.vsizer.Add(self.hinfo_sizer)
        self.vsizer.AddSpacer(10)

        self.hsizer.Add(self.vsizer)
        self.hsizer.AddSpacer(100)

        self.SetSizer(self.hsizer)

    # EVT Functions
    def dormClicked(self, event):
        # print(self.info)
        app = dormview.DormView(self.info)
        app.MainLoop()