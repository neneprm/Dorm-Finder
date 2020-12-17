from app_template import *
import sys


class Homepage(wx.App):
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

        self.data_panel = DataPanel(parent=self)
        self.detailadd_panel = DetailAdd(parent=self)

        self.hpanel_box = wx.BoxSizer(wx.HORIZONTAL)
        self.hpanel_box.AddSpacer(60)

        self.vpanel_box.Add(self.data_panel)
        self.vpanel_box.Add(self.hpanel_box)
        self.hpanel_box.Add(self.detailadd_panel)

        # self.hpanel_box.AddSpacer(60)

        # self.detailadd_panel.show_info()
        self.detailadd_panel.add_info()


class DataPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.area = ['           ------- Select your Area -------', 'Ladkrabang', 'Rangsit', 'Phaya Thai']
        self.area_list = [('College Town', 'Ladkrabang'), ('Keystone', 'Rangsit'),
                          ('CU iHouse', 'Phaya Thai'), ('JPark Thammasat', 'Rangsit'), ('The Home', 'Ladkrabang'),
                          ('The Enter', 'Salaya'), ('U Center', 'Phayathai'), ('Pool Villa', 'Ladkrabang')]

        # Color, Font, and Style
        self.SetBackgroundColour('light blue')
        self.text_font = wx.Font(22, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.list_font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

        # Layout
        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        self.vsizer.AddSpacer(20)
        self.top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.top_sizer.AddSpacer(60)

        # Select Area
        self.area_text = wx.StaticText(self, label='Area:   ')
        self.area_text.SetFont(self.text_font)
        self.area_choice = wx.Choice(self, size=(300, 33), choices=self.area)

        self.top_sizer.Add(self.area_text, 0, wx.ALL)
        self.top_sizer.Add(self.area_choice, 0, wx.ALL)
        self.top_sizer.AddSpacer(140)

        # Add button
        self.add_button = wx.Button(self, label="Add New Dorm", size=(200, 33))
        self.top_sizer.Add(self.add_button, 0, wx.ALL)
        self.top_sizer.AddSpacer(40)

        self.detail_button = wx.Button(self, label='More Details', size=(200, 33))
        self.top_sizer.Add(self.detail_button, 0, wx.ALL)
        self.vsizer.Add(self.top_sizer, wx.ALL)
        self.vsizer.AddSpacer(20)

        # Dorm list
        #   Layout
        self.list_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.list_sizer.AddSpacer(60)
        self.list = wx.ListCtrl(self, -1, size=(960, 100), style=wx.LC_REPORT)
        self.list.InsertColumn(1, 'Name', wx.LIST_FORMAT_LEFT, 400)
        self.list.InsertColumn(2, 'Area', wx.LIST_FORMAT_LEFT, 300)
        self.list.InsertColumn(3, 'Status', wx.LIST_FORMAT_CENTER, 250)
        self.list.SetFont(self.list_font)
        self.list.AlwaysShowScrollbars(hflag=False, vflag=True)

        #   Data
        for i in self.area_list:
            self.area_index = self.list.InsertItem(sys.maxsize, i[0])
            self.list.SetItem(self.area_index, 1, i[1])

        self.list_sizer.Add(self.list, wx.EXPAND | wx.ALL)
        self.list_sizer.AddSpacer(60)
        self.vsizer.Add(self.list_sizer, 0, wx.EXPAND | wx.ALL)
        self.vsizer.AddSpacer(20)

        # Initialize
        self.SetSizer(self.vsizer)


class DetailAdd(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.box_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        self.col1_sizer = wx.BoxSizer(wx.HORIZONTAL)

    def show_info(self):
        # Color, Font, and Style
        self.SetBackgroundColour('pale green')
        info_font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        input_font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.vsizer.AddSpacer(20)

        # Done button
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.AddSpacer(770)
        done_button = wx.Button(self, label='Done', size=(130, 33))
        button_sizer.Add(done_button)
        button_sizer.AddSpacer(60)
        self.vsizer.Add(button_sizer)
        self.vsizer.AddSpacer(10)

        # Info
        self.col1_sizer.AddSpacer(40)

        info = wx.StaticText(self, label='Name\n\nArea\n\nYear of Contruction\n\nSize (sq.m.)\n\nNo. of Room\n\nNo. of Floor\n\nPrice (Baht/month)\n\nStatus\n\nContact', style=wx.ALIGN_RIGHT)
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
        insert_pic = wx.StaticText(self, label='insert pic', style=wx.ALIGN_CENTER)
        self.col1_sizer.Add(insert_pic)

        # Initialize
        self.vsizer.Add(self.col1_sizer)
        self.vsizer.AddSpacer(30)
        self.SetSizer(self.vsizer)

    def add_info(self):
        # Color, Font, and Style
        self.SetBackgroundColour('pale green')
        info_font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        input_font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.vsizer.AddSpacer(20)

        # Done button
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.AddSpacer(770)
        save_button = wx.Button(self, label='Save', size=(130, 33))
        button_sizer.Add(save_button)
        button_sizer.AddSpacer(60)
        self.vsizer.Add(button_sizer)
        self.vsizer.AddSpacer(10)

        # Info
        self.col1_sizer.AddSpacer(40)

        info = wx.StaticText(self,
                             label='Name\n\nArea\n\nYear of Contruction\n\nSize (sq.m.)\n\nNo. of Room\n\nNo. of Floor\n\nPrice (Baht/month)\n\nStatus\n\nContact',
                             style=wx.ALIGN_RIGHT)
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
        insert_pic = wx.StaticText(self, label='insert pic', style=wx.ALIGN_CENTER)
        self.col1_sizer.Add(insert_pic)

        # Initialize
        self.vsizer.Add(self.col1_sizer)
        self.vsizer.AddSpacer(30)
        self.SetSizer(self.vsizer)


if __name__ == "__main__":
    homepage = Homepage()
    homepage.MainLoop()
