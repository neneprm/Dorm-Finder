import wx
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


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.SetBackgroundColour('light blue')

        self.title_panel = TitlePanel(parent=self)
        self.data_panel = DataPanel(parent=self)
        self.detail_panel = DetailPanel(parent=self)

        self.panel_box = wx.BoxSizer(wx.VERTICAL)
        self.panel_box.Add(self.title_panel, 0, wx.EXPAND | wx.ALL)
        self.panel_box.Add(self.data_panel, 0, wx.EXPAND | wx.ALL)

        self.detail_box = wx.BoxSizer(wx.HORIZONTAL)
        self.detail_box.AddSpacer(60)
        self.detail_box.Add(self.detail_panel, wx.EXPAND | wx.ALL)
        self.detail_box.AddSpacer(60)
        self.panel_box.Add(self.detail_box, wx.EXPAND | wx.ALL)

        self.SetSizer(self.panel_box)


class TitlePanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.SetBackgroundColour('sky blue')
        self.title_font = wx.Font(32, wx.MODERN, wx.BOLD, wx.NORMAL)

        self.title_sizer = wx.BoxSizer(wx.VERTICAL)
        self.title_sizer.AddSpacer(20)

        self.title = wx.StaticText(self, label='RENT-A-DORM', style=wx.ALIGN_CENTER)
        self.title.SetFont(self.title_font)
        self.title_sizer.Add(self.title, 0, wx.ALL | wx.EXPAND)

        self.title_sizer.AddSpacer(20)
        self.SetSizer(self.title_sizer)


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
        self.list = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
        self.list.InsertColumn(1, 'Name', wx.LIST_FORMAT_LEFT, 400)
        self.list.InsertColumn(2, 'Area', wx.LIST_FORMAT_LEFT, 300)
        self.list.InsertColumn(3, 'Status', wx.LIST_FORMAT_CENTER, 250)
        self.list.SetFont(self.list_font)

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


class DetailPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # Color, Font, and Style
        self.row2_sizer = wx.BoxSizer(wx.HORIZONTAL)
        # self.save_button = wx.Button(self, label="Save", size=(160, 33))
        self.status = wx.StaticText(self, label='Status', style=wx.ALIGN_RIGHT)
        self.status_input = wx.TextCtrl(self, size=(80, 20))
        self.status_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.pic_sizer = wx.BoxSizer(wx.VERTICAL)
        self.price_input = wx.TextCtrl(self, size=(80, 20))
        self.floor_input = wx.TextCtrl(self, size=(80, 20))
        self.room_input = wx.TextCtrl(self, size=(80, 20))
        self.size_input = wx.TextCtrl(self, size=(80, 20))
        self.area_input = wx.TextCtrl(self, size=(150, 20))
        self.name_input = wx.TextCtrl(self, size=(150, 20))
        self.year_input = wx.TextCtrl(self, size=(80, 20))
        self.info_sizer = wx.BoxSizer(wx.VERTICAL)
        self.info1 = wx.StaticText(self, label='Year of Construction \n\nName \n\nArea \n\nSize (sq.m.) \n\nNo. of '
                                               'Room \n\nNo. of Floor \n\nPrice (Baht/Month)', style=wx.ALIGN_RIGHT)
        self.row1_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetBackgroundColour('cadet blue')
        self.info_font = wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.input_font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

        # Layout
        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        self.vsizer.AddSpacer(60)

        # Dorm Image
        # self.ct_1 = wx.Image('college_town/college_town_1.jpg', wx.BITMAP_TYPE_ANY)
        # self.ct_1 = wx.Image.Scale(self.ct_1, 10, 10, quality=wx.IMAGE_QUALITY_BOX_AVERAGE)
        # self.w1 = self.ct_1.GetWidth()
        # self.h1 = self.ct_1.GetHeight()
        # print(type(self.ct_1))
        # self.ct_1 = wx.Image.Scale(10, 10)
        # self.row1_sizer.Add(self.ct_1)

        # self.detail()
        self.info()

    def detail(self):
        # Dorm Info.
        self.row1_sizer.AddSpacer(20)
        self.info1.SetFont(self.info_font)

        self.row1_sizer.Add(self.info1)
        self.row1_sizer.AddSpacer(5)

        # Year of construct.
        self.year_input.SetFont(self.input_font)
        self.year_input.SetEditable(True)
        self.info_sizer.Add(self.year_input)

        # Name
        self.info_sizer.AddSpacer(18)
        self.name_input.SetFont(self.input_font)
        self.name_input.SetEditable(True)
        self.info_sizer.Add(self.name_input)

        # Area
        self.info_sizer.AddSpacer(18)
        self.area_input.SetFont(self.input_font)
        self.area_input.SetEditable(True)
        self.info_sizer.Add(self.area_input)

        # Size
        self.info_sizer.AddSpacer(18)
        self.size_input.SetFont(self.input_font)
        self.size_input.SetEditable(True)
        self.info_sizer.Add(self.size_input)

        # Np. of room
        self.info_sizer.AddSpacer(18)
        self.room_input.SetFont(self.input_font)
        self.room_input.SetEditable(True)
        self.info_sizer.Add(self.room_input)

        # No. of floor
        self.info_sizer.AddSpacer(18)
        self.floor_input.SetFont(self.input_font)
        self.floor_input.SetEditable(True)
        self.info_sizer.Add(self.floor_input)

        # Price
        self.info_sizer.AddSpacer(18)
        self.price_input.SetFont(self.input_font)
        self.price_input.SetEditable(True)
        self.info_sizer.Add(self.price_input)

        # Status
        # self.info_sizer.AddSpacer(18)
        # self.status_input = wx.TextCtrl(self, size=(80, 20))
        # self.status_input.SetFont(self.input_font)
        # self.status_input.SetEditable(True)
        # self.info_sizer.Add(self.status_input)

        self.row1_sizer.Add(self.info_sizer)
        self.row1_sizer.AddSpacer(80)

        self.status.SetFont(self.info_font)
        self.status_sizer.Add(self.status)

        self.status_sizer.AddSpacer(20)
        self.status_input.SetFont(self.input_font)
        self.status_input.SetEditable(True)
        self.status_sizer.Add(self.status_input)
        self.status_sizer.AddSpacer(500)

        self.pic_sizer.Add(self.status_sizer)
        self.row1_sizer.Add(self.pic_sizer)

        self.vsizer.Add(self.row1_sizer, 0, wx.EXPAND)
        self.vsizer.AddSpacer(12)

        # Initialize
        self.vsizer.AddSpacer(20)
        self.SetSizer(self.vsizer)

    def info(self):
        # Save button
        save_button = wx.Button(self, label="Save", size=(160, 33))
        self.row1_sizer.Add(save_button, 0, wx.ALL)
        self.row1_sizer.AddSpacer(40)
        self.vsizer.Add(self.row1_sizer, wx.EXPAND)
        self.vsizer.AddSpacer(10)

        # Dorm Info.
        self.row2_sizer.AddSpacer(20)
        self.info1 = wx.StaticText(self, label='Year of Construction \n\nName \n\nArea \n\nSize (sq.m.) \n\nNo. of '
                                               'Room \n\nNo. of Floor \n\nPrice (Baht/Month)', style=wx.ALIGN_RIGHT)
        self.info1.SetFont(self.info_font)

        self.row2_sizer.Add(self.info1)
        self.row2_sizer.AddSpacer(5)

    # Year of construct.
        self.info_sizer = wx.BoxSizer(wx.VERTICAL)
        self.year_input = wx.TextCtrl(self, size=(80, 20))
        self.year_input.SetFont(self.input_font)
        self.year_input.SetEditable(True)
        self.info_sizer.Add(self.year_input)

        # Name
        self.info_sizer.AddSpacer(18)
        self.name_input = wx.TextCtrl(self, size=(150, 20))
        self.name_input.SetFont(self.input_font)
        self.name_input.SetEditable(True)
        self.info_sizer.Add(self.name_input)

        # Area
        self.info_sizer.AddSpacer(18)
        self.area_input = wx.TextCtrl(self, size=(150, 20))
        self.area_input.SetFont(self.input_font)
        self.area_input.SetEditable(True)
        self.info_sizer.Add(self.area_input)

        # Size
        self.info_sizer.AddSpacer(18)
        self.size_input = wx.TextCtrl(self, size=(80, 20))
        self.size_input.SetFont(self.input_font)
        self.size_input.SetEditable(True)
        self.info_sizer.Add(self.size_input)

        # Np. of room
        self.info_sizer.AddSpacer(18)
        self.room_input = wx.TextCtrl(self, size=(80, 20))
        self.room_input.SetFont(self.input_font)
        self.room_input.SetEditable(True)
        self.info_sizer.Add(self.room_input)

        # No. of floor
        self.info_sizer.AddSpacer(18)
        self.floor_input = wx.TextCtrl(self, size=(80, 20))
        self.floor_input.SetFont(self.input_font)
        self.floor_input.SetEditable(True)
        self.info_sizer.Add(self.floor_input)

        # Price
        self.info_sizer.AddSpacer(18)
        self.price_input = wx.TextCtrl(self, size=(80, 20))
        self.price_input.SetFont(self.input_font)
        self.price_input.SetEditable(True)
        self.info_sizer.Add(self.price_input)

        # Status
        # self.info_sizer.AddSpacer(18)
        # self.status_input = wx.TextCtrl(self, size=(80, 20))
        # self.status_input.SetFont(self.input_font)
        # self.status_input.SetEditable(True)
        # self.info_sizer.Add(self.status_input)

        self.row2_sizer.Add(self.info_sizer)
        self.row2_sizer.AddSpacer(80)

        self.pic_sizer = wx.BoxSizer(wx.VERTICAL)
        self.status_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.status = wx.StaticText(self, label='Status', style=wx.ALIGN_RIGHT)
        self.status.SetFont(self.info_font)
        self.status_sizer.Add(self.status)

        self.status_sizer.AddSpacer(20)
        self.status_input = wx.TextCtrl(self, size=(80, 20))
        self.status_input.SetFont(self.input_font)
        self.status_input.SetEditable(True)
        self.status_sizer.Add(self.status_input)

        self.pic_sizer.Add(self.status_sizer)
        self.row2_sizer.Add(self.pic_sizer)

        self.vsizer.Add(self.row2_sizer, 0, wx.EXPAND)
        self.vsizer.AddSpacer(12)

        # Initialize
        self.vsizer.AddSpacer(20)
        self.SetSizer(self.vsizer)


if __name__ == "__main__":
    homepage = Homepage()
    homepage.MainLoop()
