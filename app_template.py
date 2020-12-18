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


class Info(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
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

        # Info
        self.col1_sizer.AddSpacer(40)

        info = wx.StaticText(self, label='Name\n\nArea\n\nYear of Contruction\n\nSize (sq.m.)\n\nNo. of Room\n\nNo. '
                                         'of Floor\n\nPrice (Baht/month)\n\nStatus\n\nContact', style=wx.ALIGN_RIGHT)
        info.SetFont(info_font)
        self.col1_sizer.Add(info, wx.ALL)
        self.col1_sizer.AddSpacer(15)

        col2_sizer = wx.BoxSizer(wx.VERTICAL)

        # def info_txtctrl(info_name, width):
        #     info_name = wx.TextCtrl(self, size=(width, 22))
        #     info_name.SetFont(input_font)
        #     col2_sizer.Add(info_name, wx.ALL)
        #     col2_sizer.AddSpacer(12)
        #
        # info_txtctrl(name, 180)

        name = wx.TextCtrl(self, size=(180, 22))
        name.SetFont(input_font)
        # name.SetEditable(False)
        col2_sizer.Add(name, wx.ALL)
        col2_sizer.AddSpacer(14)

        area = wx.TextCtrl(self, size=(180, 22))
        area.SetFont(input_font)
        col2_sizer.Add(area, wx.ALL)
        col2_sizer.AddSpacer(14)

        year = wx.TextCtrl(self, size=(70, 22))
        year.SetFont(input_font)
        col2_sizer.Add(year, wx.ALL)
        col2_sizer.AddSpacer(14)

        size = wx.TextCtrl(self, size=(70, 22))
        size.SetFont(input_font)
        col2_sizer.Add(size, wx.ALL)
        col2_sizer.AddSpacer(14)

        room = wx.TextCtrl(self, size=(70, 22))
        room.SetFont(input_font)
        col2_sizer.Add(room, wx.ALL)
        col2_sizer.AddSpacer(14)

        floor = wx.TextCtrl(self, size=(70, 22))
        floor.SetFont(input_font)
        col2_sizer.Add(floor, wx.ALL)
        col2_sizer.AddSpacer(14)

        price = wx.TextCtrl(self, size=(70, 22))
        price.SetFont(input_font)
        col2_sizer.Add(price, wx.ALL)
        col2_sizer.AddSpacer(14)

        status = wx.TextCtrl(self, size=(125, 22))
        status.SetFont(input_font)
        col2_sizer.Add(status, wx.ALL)
        col2_sizer.AddSpacer(14)

        contact = wx.TextCtrl(self, size=(125, 22))
        contact.SetFont(input_font)
        col2_sizer.Add(contact, wx.ALL)

        self.col1_sizer.Add(col2_sizer)

        # Pic
        self.col1_sizer.AddSpacer(30)

        pic_sizer = wx.BoxSizer(wx.VERTICAL)

        # insert picture over hereeeeeeeeeee
        # test test test hellowwwww
        # back_icon2 = wx.Bitmap("icons/back.png")
        # back_button2 = buttons.GenBitmapButton(self, bitmap=back_icon2,
        #                                       size=(back_icon2.GetWidth(), back_icon2.GetHeight()))
        # pic_sizer.Add(back_button2)

        # Back and Next Button
        pic_button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        pic_button_sizer.AddSpacer(150)

        back_icon = wx.Bitmap('icons/back.png')
        self.back_button = buttons.GenBitmapButton(self, bitmap=back_icon,
                                              size=(back_icon.GetWidth(), back_icon.GetHeight()))
        # EVT
        self.back_button.Bind(wx.EVT_BUTTON, self.backClicked)

        next_icon = wx.Bitmap('icons/next.png')
        self.next_button = buttons.GenBitmapButton(self, bitmap=next_icon,
                                              size=(next_icon.GetWidth(), back_icon.GetHeight()))
        # EVT
        self.next_button.Bind(wx.EVT_BUTTON, self.nextClicked)

        pic_button_sizer.Add(self.back_button)
        pic_button_sizer.AddSpacer(200)
        pic_button_sizer.Add(self.next_button)
        pic_sizer.Add(pic_button_sizer)

        self.col1_sizer.Add(pic_sizer)

        # Initialize
        self.vsizer.Add(self.col1_sizer)
        self.vsizer.AddSpacer(30)
        self.SetSizer(self.vsizer)

    def backClicked(self, event):
        self.back_button = event.GetEventObject()
        print("Label of pressed button = ", self.back_button)

    def nextClicked(self, event):
        self.next_button = event.GetEventObject()
        print("Label of pressed button = ", self.next_button)


class DormListPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.SetBackgroundColour('#ea86b6')
        # Color, Font, and Style
        name_font = wx.Font(20, wx.MODERN, wx.BOLD, wx.NORMAL)
        detail_font = wx.Font(14, wx.DEFAULT, wx.BOLD, wx.NORMAL)

        # Layout
        # Dorm Button
        self.hsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.dorm_icon = wx.Bitmap('college_town/icon.jpg')
        self.dorm_button = buttons.GenBitmapButton(self, bitmap=self.dorm_icon,
                                               size=(self.dorm_icon.GetWidth(), self.dorm_icon.GetHeight()))
        self.hsizer.Add(self.dorm_button)
        self.hsizer.AddSpacer(100)
        # EVT
        self.dorm_button.Bind(wx.EVT_BUTTON, self.dormClicked)

        # Info
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

    # EVT Functions
    def dormClicked(self, event):
        self.dorm_button = event.GetEventObject()
        print("Label of pressed button = ", self.dorm_button)


if __name__ == "__main__":
    template = Template()
    template.MainLoop()
