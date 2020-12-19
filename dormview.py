from app_template import *


class DormView(wx.App):
    def __init__(self, info):
        super().__init__()
        dorminfo = info

        self.frame = MyFrame(parent=None, title='RENT-A-DORM', size=(900, 300), info=dorminfo)
        self.frame.Center()
        self.frame.Show()


class MyFrame(wx.Frame):
    def __init__(self, parent, title, size, info):
        super().__init__(parent=parent, title=title, size=size)
        self.SetMinSize(size)
        self.SetMaxSize(size)
        self.info = info
        self.panel = MyPanel(parent=self)


class MyPanel(Info):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.SetBackgroundColour('#f3bad6')

        back_icon = wx.Bitmap('icons/back.png')
        back_button = buttons.GenBitmapButton(self, bitmap=back_icon,
                                                   size=(back_icon.GetWidth(), back_icon.GetHeight()))

        # Dorm detail
        detail = self.GetParent()
        print(detail.info)
        self.name.WriteText(detail.info[0])
        self.area.WriteText(detail.info[1])
        self.size.WriteText(detail.info[2])
        self.price.WriteText(detail.info[3])
        self.status.WriteText(detail.info[4])
        self.contact.WriteText(detail.info[5])

        self.name.SetEditable(False)
        self.area.SetEditable(False)
        self.size.SetEditable(False)
        self.price.SetEditable(False)
        self.status.SetEditable(False)
        self.contact.SetEditable(False)

        # EVT
        back_button.Bind(wx.EVT_BUTTON, self.backClicked)
        next_icon = wx.Bitmap('icons/next.png')
        next_button = buttons.GenBitmapButton(self, bitmap=next_icon,
                                                   size=(next_icon.GetWidth(), back_icon.GetHeight()))
        # EVT
        next_button.Bind(wx.EVT_BUTTON, self.nextClicked)
        self.pic_button_sizer.Add(back_button)
        self.pic_button_sizer.AddSpacer(200)
        self.pic_button_sizer.Add(next_button)

    def backClicked(self, event):
        back_button = event.GetEventObject()
        print("Label of pressed button = ", back_button)

    def nextClicked(self, event):
        next_button = event.GetEventObject()
        print("Label of pressed button = ", next_button)


if __name__ == "__main__":
    dormview = DormView()
    dormview.MainLoop()