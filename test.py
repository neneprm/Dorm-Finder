import sys
from template import *


# class Homepage(Template):
    def __init__(self):
        super().__init__()
        # self.frame = MyFrame(parent=None, title='RENT-A-DORM', size=(1080, 720))
        # self.frame.Center()
        # self.frame.Show()


# class Panel(MainPanel):
    def __init__(self, parent, area, area_list, vsizer, top_sizer, area_text, area_choice, add_button, list_sizer, list, area_index, detail_sizer, detail_button):
        super().__init__(parent=parent)
        self.area = area
        self.area_list = area_list
        self.vsizer = vsizer
        self.top_sizer = top_sizer
        self.area_text = area_text
        self.area_choice = area_choice
        self.add_button = add_button
        self.list_sizer = list_sizer
        self.list = list
        self.area_index = area_index
        self.detail_sizer = detail_sizer
        self.detail_button = detail_button

    def add_template(self, parent):
        self.area = ['           ------- Select your Area -------', 'Ladkrabang', 'Rangsit', 'Phaya Thai']
        self.area_list = [('1', 'College Town', 'Ladkrabang'), ('2', 'Keystone', 'Rangsit'),
                          ('3', 'CU iHouse', 'Phaya Thai'), ('4', 'JPark Thammasat', 'Rangsit'),
                          ('5', 'The Home', 'Ladkrabang'), ('6', 'The Enter', 'Salaya'), ('7', 'U Center', 'Phayathai'),
                          ('8', 'Pool Villa', 'Ladkrabang')]

        # Layout
        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        self.vsizer.AddSpacer(40)
        self.top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.top_sizer.AddSpacer(60)

        # Select Area
        self.area_text = wx.StaticText(self, label='Area:   ')
        self.area_text.SetFont(self.text_font)
        self.area_choice = wx.Choice(self, size=(300, 33), choices=self.area)

        self.top_sizer.Add(self.area_text, 0, wx.ALL)
        self.top_sizer.Add(self.area_choice, 0, wx.ALL)
        self.top_sizer.AddSpacer(360)

        # Add button
        self.add_button = wx.Button(self, label="Add New Area", size=(200, 33))
        self.top_sizer.Add(self.add_button, 0, wx.ALL)
        self.vsizer.Add(self.top_sizer, 0, wx.ALL)
        self.vsizer.AddSpacer(40)

        # Dorm list
        #   Layout
        self.list_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.list_sizer.AddSpacer(60)
        self.list = wx.ListCtrl(self, -1, size=(935, 150), style=wx.LC_REPORT)
        self.list.InsertColumn(0, 'Number', wx.LIST_FORMAT_CENTER, 150)
        self.list.InsertColumn(1, 'Name', wx.LIST_FORMAT_LEFT, 330)
        self.list.InsertColumn(2, 'Area', wx.LIST_FORMAT_LEFT, 280)
        self.list.InsertColumn(3, 'Status', wx.LIST_FORMAT_CENTER, 175)
        self.list.SetFont(self.list_font)

        #   Data
        for i in self.area_list:
            self.area_index = self.list.InsertStringItem(sys.maxsize, i[0])
            self.list.SetStringItem(self.area_index, 1, i[1])
            self.list.SetStringItem(self.area_index, 2, i[2])

        self.list_sizer.Add(self.list, wx.EXPAND)
        self.vsizer.Add(self.list_sizer)
        self.vsizer.AddSpacer(30)

        # More Detail button
        self.detail_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.detail_sizer.AddSpacer(890)
        self.detail_button = wx.Button(self, label='More Detail', size=(100, 33))
        self.detail_sizer.Add(self.detail_button, 0, wx.ALL)
        self.vsizer.Add(self.detail_sizer, 0, wx.ALL)

        # Initialize
        self.SetSizer(self.vsizer)


if __name__ == "__main__":
    homepage = Homepage()
    homepage.MainLoop()
