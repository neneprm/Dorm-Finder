from app_template import *


class User(wx.App):
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
        self.SetBackgroundColour('pink')
        self.title_panel.SetBackgroundColour('blue violet')

        self.data_panel = DataPanel(parent=self)

        self.hpanel_box = wx.BoxSizer(wx.HORIZONTAL)
        self.hpanel_box.AddSpacer(60)

        self.vpanel_box.Add(self.data_panel)
        self.vpanel_box.Add(self.hpanel_box)


class DataPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        # Color, Font, and Style
        self.SetBackgroundColour('sky blue')
        self.text_font = wx.Font(22, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.list_font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)



if __name__ == "__main__":
    user = User()
    user.MainLoop()
