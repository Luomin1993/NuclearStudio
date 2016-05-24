#Boa:Frame:NStudio

import wx

def create(parent):
    return NStudio(parent)

[wxID_NSTUDIO, wxID_NSTUDIOSCROLLEDWINDOW1, wxID_NSTUDIOSTATICBITMAP2, 
] = [wx.NewId() for _init_ctrls in range(3)]

class NStudio(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_NSTUDIO, name=u'NStudio', parent=prnt,
              pos=wx.Point(578, 187), size=wx.Size(527, 483),
              style=wx.DEFAULT_FRAME_STYLE, title=u'NStudio')
        self.SetClientSize(wx.Size(511, 445))

        self.scrolledWindow1 = wx.ScrolledWindow(id=wxID_NSTUDIOSCROLLEDWINDOW1,
              name='scrolledWindow1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(511, 445), style=wx.HSCROLL | wx.VSCROLL)

        self.staticBitmap2 = wx.StaticBitmap(bitmap=wx.Bitmap(u'D:/NuclearStudio/ns_pic/chain_pic_1.JPG',
              wx.BITMAP_TYPE_JPEG), id=wxID_NSTUDIOSTATICBITMAP2,
              name='staticBitmap2', parent=self.scrolledWindow1,
              pos=wx.Point(16, 16), size=wx.Size(536, 464), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
