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




if __name__ == "__main__":
    homepage = Homepage()
    homepage.MainLoop()
