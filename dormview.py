from app_template import *
import glob


class DormView(wx.App):
    def __init__(self, info):
        super().__init__()
        dorminfo = info

        self.frame = MyFrame(parent=None, title='RENT-A-DORM', size=(1200, 650), info=dorminfo)
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

        detail = self.GetParent()
        self.index = 0
        # Dorm pics
        # print(detail.info)
        name = detail.info[0]
        name = name.lower().replace(' ', '_')
        # print(name)
        self.pic_path = tuple(glob.glob('img/' + name + '/*[0-9].jpg')) # list of picture's directory
        # print(pic_path)

        self.img = wx.Image(self.pic_path[self.index], wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmp = wx.StaticBitmap(self, -1, self.img, (self.img.GetWidth(), self.img.GetHeight()))

        self.pic_sizer.Add(self.bmp)

        # Back and Next buttons
        back_icon = wx.Bitmap('icons/back.png')
        back_button = buttons.GenBitmapButton(self, bitmap=back_icon,
                                                   size=(back_icon.GetWidth(), back_icon.GetHeight()))
        next_icon = wx.Bitmap('icons/next.png')
        next_button = buttons.GenBitmapButton(self, bitmap=next_icon,
                                              size=(next_icon.GetWidth(), back_icon.GetHeight()))
        self.pic_button_sizer.Add(back_button)
        self.pic_button_sizer.AddSpacer(10)
        self.pic_button_sizer.Add(next_button)

        self.pic_sizer.Add(self.pic_button_sizer)

        # Display information
        # print(detail.info)
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
        next_button.Bind(wx.EVT_BUTTON, self.nextClicked)

    def backClicked(self, event):
        self.img = wx.Image(self.pic_path[(self.index - 1) % len(self.pic_path)], wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmp.SetBitmap(self.img)
        self.index -= 1

    def nextClicked(self, event):
        self.img = wx.Image(self.pic_path[(self.index + 1) % len(self.pic_path)], wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bmp.SetBitmap(self.img)
        self.index += 1


if __name__ == "__main__":
    dormview = DormView()
    dormview.MainLoop()