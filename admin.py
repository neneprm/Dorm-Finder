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
        # self.detailadd_panel = DetailAdd(parent=self)

        # self.hpanel_box = wx.BoxSizer(wx.HORIZONTAL)
        # self.hpanel_box.AddSpacer(60)

        self.vpanel_box.Add(self.data_panel)
        # self.vpanel_box.Add(self.hpanel_box)
        # self.hpanel_box.Add(self.detailadd_panel)

        # self.detailadd_panel.show_info()
        # self.detailadd_panel.add_info()


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
        self.vsizer.AddSpacer(30)
        self.top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.top_sizer.AddSpacer(820)

        # Log Out button
        self.logOut_button = wx.Button(self, label='Log Out', size=(200, 33))
        self.top_sizer.Add(self.logOut_button, wx.ALL)
        # EVT
        self.logOut_button.Bind(wx.EVT_BUTTON, self.logOutClicked)

        self.vsizer.Add(self.top_sizer, 0, wx.ALL)
        self.vsizer.AddSpacer(30)

        # Dorm list
        #   Layout
        self.list_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.list_sizer.AddSpacer(60)
        self.list = wx.ListCtrl(self, -1, size=(960, 140), style=wx.LC_REPORT)
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
        self.vsizer.AddSpacer(110)

        self.detailadd_panel = DetailAdd(parent=parent)

        self.hpanel_box = wx.BoxSizer(wx.HORIZONTAL)
        self.hpanel_box.AddSpacer(60)
        self.hpanel_box.Add(self.detailadd_panel)

        self.vsizer.Add(self.hpanel_box)

        # self.detailadd_panel.show_info()
        self.detailadd_panel.add_info()

        # Initialize
        self.SetSizer(self.vsizer)

    # EVT Functions
    def addClicked(self, event):
        self.detailadd_panel.add_info()

    def detailClicked(self, event):
        self.detailadd_panel.show_info()

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
        # show.button_sizer.AddSpacer(190)
        self.box_sizer.Add(show)
        self.SetSizer(self.box_sizer)

    def add_info(self):
        # Color, Font, and Style
        self.SetBackgroundColour('#dff0ea')
        add = Info(self)
        add_button = wx.Button(self, label='Add', size=(130, 33))
        add.button_sizer.Add(add_button)
        add.button_sizer.AddSpacer(60)
        # EVT
        add_button.Bind(wx.EVT_BUTTON, self.addClicked)

        add_pic_button = wx.Button(self, label='Add Image Here', size=(200, 33))
        add.pic_button_sizer.Add(add_pic_button, wx.ALL)
        add_pic_button.Bind(wx.EVT_BUTTON, self.add_picClicked)

        self.box_sizer.Add(add)
        self.SetSizer(self.box_sizer)

    def addClicked(self, event):
        add_button = event.GetEventObject().GetLabel()
        print("Label of pressed button = ", add_button)

    def add_picClicked(self, event):
        with wx.FileDialog(self, 'Add Image', style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
        pathname = fileDialog.GetPath()
        try:
            with open(pathname, 'w') as file:
                file.write(pathname + '.jpg')
        except IOError:
            wx.LogError("Cannot save image in file '%s' " % pathname)


if __name__ == "__main__":
    admin = Admin()
    admin.MainLoop()
