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
        f.close()

        # Color, Font, and Style
        self.SetBackgroundColour('#aee7e8')
        list_font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)

        # Layout
        self.vsizer = wx.BoxSizer(wx.VERTICAL)
        self.vsizer.AddSpacer(30)
        self.top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.top_sizer.AddSpacer(600)

        # Refresh button
        self.refresh_button = wx.Button(self, label='Refresh', size=(100, 33))
        self.top_sizer.Add(self.refresh_button, wx.ALL)
        self.top_sizer.AddSpacer(20)
        # EVT
        self.refresh_button.Bind(wx.EVT_BUTTON, self.refreshClicked)

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
        self.list.InsertColumn(1, 'Name', wx.LIST_FORMAT_LEFT, 150)
        self.list.InsertColumn(2, 'Area', wx.LIST_FORMAT_LEFT, 150)
        self.list.InsertColumn(3, 'Size', wx.LIST_FORMAT_CENTER, 150)
        self.list.InsertColumn(4, 'Price', wx.LIST_FORMAT_CENTER, 150)
        self.list.InsertColumn(5, 'Status', wx.LIST_FORMAT_CENTER, 150)
        self.list.InsertColumn(6, 'Contact', wx.LIST_FORMAT_CENTER, 150)
        self.list.SetFont(list_font)
        self.list.AlwaysShowScrollbars(hflag=False, vflag=True)

        for i in self.area_list:
            self.area_index = self.list.InsertItem(sys.maxsize, i[0])
            for j in range(1, len(i)):
                self.list.SetItem(self.area_index, j, i[j])

        self.list.Bind(wx.EVT_LIST_ITEM_SELECTED, self.listSelected)

        self.list_sizer.Add(self.list, wx.EXPAND | wx.ALL)
        self.list_sizer.AddSpacer(60)
        self.vsizer.Add(self.list_sizer, 0, wx.EXPAND | wx.ALL)
        self.vsizer.AddSpacer(110)

        self.detailadd_panel = DetailAdd(parent=parent, info=self.area_list)

        self.hpanel_box = wx.BoxSizer(wx.HORIZONTAL)
        self.hpanel_box.AddSpacer(60)
        self.hpanel_box.Add(self.detailadd_panel)

        self.vsizer.Add(self.hpanel_box)

        # self.detailadd_panel.show_info()
        self.detailadd_panel.add_info()

        # Initialize
        self.SetSizer(self.vsizer)

    # EVT Functions
    def refreshClicked(self, event):
        with open('assets/dorm.csv', newline='') as f:
            reader = csv.reader(f)
            dormList = reader
            for row in dormList:
                if row not in self.area_list:
                    self.area_list.append(row)
        f.close()

        for i in self.area_list:
            self.area_index = self.list.InsertItem(sys.maxsize, i[0])
            for j in range(1, len(i)):
                self.list.SetItem(self.area_index, j, i[j])

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
            size = obj.GetItem(item, 2)
            price = obj.GetItem(item, 3)
            status = obj.GetItem(item, 4)
            contact = obj.GetItem(item, 5)

            # print(name.Text + ' ' + area.Text + ' ' + size.Text + ' ' + price.Text + ' ' + status.Text + ' ' + contact.Text)

            self.detailadd_panel.add.name.SetValue(name.Text)
            self.detailadd_panel.add.area.SetValue(area.Text)
            self.detailadd_panel.add.size.SetValue(size.Text)
            self.detailadd_panel.add.price.SetValue(price.Text)
            self.detailadd_panel.add.status.SetValue(status.Text)
            self.detailadd_panel.add.contact.SetValue(contact.Text)
            item = obj.GetNextSelected(item)


class DetailAdd(wx.Panel):
    def __init__(self, parent, info):
        super().__init__(parent=parent)
        self.box_sizer = wx.BoxSizer(wx.VERTICAL)
        self.dormList = info
        self.parent = parent

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
        self.add = Info(self)
        save_button = wx.Button(self, label='Save', size=(130, 33))
        self.add.button_sizer.Add(save_button)
        self.add.button_sizer.AddSpacer(60)
        # EVT
        save_button.Bind(wx.EVT_BUTTON, self.saveClicked)

        add_pic_button = wx.Button(self, label='Add Image Here', size=(200, 33))
        self.add.pic_button_sizer.Add(add_pic_button, wx.ALL)
        add_pic_button.Bind(wx.EVT_BUTTON, self.add_picClicked)
        # self.pic_sizer.Add(self.pic_button_sizer)

        self.box_sizer.Add(self.add)
        self.SetSizer(self.box_sizer)

    def saveClicked(self, event): # write file
        for i in range(len(self.dormList)):
            templist = []
            templist.append(self.add.name.GetValue())
            templist.append(self.add.area.GetValue())
            templist.append(self.add.size.GetValue())
            templist.append(self.add.price.GetValue())
            templist.append(self.add.status.GetValue())
            templist.append(self.add.contact.GetValue())
            if self.add.name.GetValue() == self.dormList[i][0]: # overwrite to existing information
                for j in range(1, len(self.dormList[i])):
                    self.dormList[i][j] = templist[j]
                # print(self.dormList)
                self.dormList[i] = templist
                with open('assets/dorm.csv',"w",newline="") as f:
                    writer = csv.writer(f)
                    writer.writerows(self.dormList)
                    f.close()
                break
            else:
                for j in range(1, len(self.dormList[i])):
                    self.dormList[i][j] = templist[j]
                self.dormList.append(templist)
                with open('assets/dorm.csv', newline='', mode='w') as f:
                    writer = csv.writer(f)
                    writer.writerows(self.dormList)
                    f.close()
                break

            # add to list
            # refresh listctrl after add or save
    def refresh(self, event):
        self.parent.data_panel.list.RefreshItems(0, 5)

    def add_picClicked(self, event):
        with wx.FileDialog(self, 'Add Image', style=wx.FD_DEFAULT_STYLE) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            path = fileDialog.GetPath()
            print(self.add.name.GetValue())


if __name__ == "__main__":
    admin = Admin()
    admin.MainLoop()
