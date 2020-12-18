from app_template import *


class DormView(wx.App):
    def __init__(self):
        super().__init__()
        self.frame = MyFrame(parent=None, title='College Town', size=(900, 400))
        self.frame.Center()
        self.frame.Show()


class MyFrame(wx.Frame):
    def __init__(self, parent, title, size):
        super().__init__(parent=parent, title=title, size=size)
        self.SetMinSize(size)
        self.SetMaxSize(size)

        self.panel = MyPanel(parent=self)


class MyPanel(Info):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.SetBackgroundColour('#f3bad6')


if __name__ == "__main__":
    dormview = DormView()
    dormview.MainLoop()