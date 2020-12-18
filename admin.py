from app_template import *
import csv
import sys


class Admin(wx.App):
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
        self.SetBackgroundColour('#aee7e8')
        self.title_panel.SetBackgroundColour('#248ea9')

        self.data_panel = DataPanel(parent=self)
        self.detailadd_panel = DetailAdd(parent=self)

        self.hpanel_box = wx.BoxSizer(wx.HORIZONTAL)
        self.hpanel_box.AddSpacer(60)

        self.vpanel_box.Add(self.data_panel)
        self.vpanel_box.Add(self.hpanel_box)
        self.hpanel_box.Add(self.detailadd_panel)

        # self.detailadd_panel.show_info()
        self.detailadd_panel.add_info()


class DataPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.area_list = []
        with open('assets/dorm.csv', newline='') as f:
            reader = csv.reader(f)
            dormList = reader
            for row in dormList:
                self.area_list.append(row)


        # Color, Font, and Style
        self.SetBackgroundColour('#aee7e8')
        list_font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

        # Layout
        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        self.vsizer.AddSpacer(20)
        self.top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.top_sizer.AddSpacer(200)

        # Add button
        self.add_button = wx.Button(self, label="Add New Dorm", size=(200, 33))
        self.top_sizer.Add(self.add_button, wx.ALL)
        self.top_sizer.AddSpacer(40)
        # EVT
        self.add_button.Bind(wx.EVT_BUTTON, self.addClicked)

        # Detail button
        self.detail_button = wx.Button(self, label='More Details', size=(200, 33))
        self.top_sizer.Add(self.detail_button, wx.ALL)
        self.top_sizer.AddSpacer(40)
        # EVT
        self.detail_button.Bind(wx.EVT_BUTTON, self.detailClicked)

        # Log Out button
        self.logOut_button = wx.Button(self, label='Log Out', size=(200, 33))
        self.top_sizer.Add(self.logOut_button, wx.ALL)
        # EVT
        self.logOut_button.Bind(wx.EVT_BUTTON, self.logOutClicked)

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
        self.list.SetFont(list_font)
        self.list.AlwaysShowScrollbars(hflag=False, vflag=True)

        for i in self.area_list:
            self.area_index = self.list.InsertItem(sys.maxsize, i[0])
            self.list.SetItem(self.area_index, 1, i[1])
            self.list.SetItem(self.area_index, 2, i[4])

        self.list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.listSelected)

        self.list_sizer.Add(self.list, wx.EXPAND | wx.ALL)
        self.list_sizer.AddSpacer(60)
        self.vsizer.Add(self.list_sizer, 0, wx.EXPAND | wx.ALL)
        self.vsizer.AddSpacer(20)

        # Initialize
        self.SetSizer(self.vsizer)

    # EVT Functions
    def addClicked(self, event):
        self.add_button = event.GetEventObject().GetLabel()
        print("Label of pressed button = ", self.add_button)

    def detailClicked(self, event):
        self.detail_button = event.GetEventObject().GetLabel()
        print("Label of pressed button = ", self.detail_button)

    def logOutClicked(self, event):
        app = self.GetParent().GetParent()
        app.Destroy()
        wx.Exit()

    def listSelected(self, event):
        obj = event.GetEventObject()
        item = obj.GetFirstSelected()

        while item != -1:
            name = obj.GetItem(item, 0)
            area = obj.GetItem(item, 1)

            print(name.Text + ', ' + area.Text)
            item = obj.GetNextSelected(item)


class DetailAdd(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.box_sizer = wx.BoxSizer(wx.VERTICAL)

    def show_info(self):
        # Color, Font, and Style
        self.SetBackgroundColour('#dff0ea')
        show = Info(self)
        show.button_sizer.AddSpacer(190)
        self.box_sizer.Add(show)
        self.SetSizer(self.box_sizer)

    def add_info(self):
        # Color, Font, and Style
        self.SetBackgroundColour('#dff0ea')
        add = Info(self)
        save_button = wx.Button(self, label='Save', size=(130, 33))
        add.button_sizer.Add(save_button)
        add.button_sizer.AddSpacer(60)
        self.box_sizer.Add(add)
        self.SetSizer(self.box_sizer)
        # EVT
        save_button.Bind(wx.EVT_BUTTON, self.saveClicked)

    def saveClicked(self, event):
        save_button = event.GetEventObject().GetLabel()
        print("Label of pressed button = ", save_button)


if __name__ == "__main__":
    admin = Admin()
    admin.MainLoop()
