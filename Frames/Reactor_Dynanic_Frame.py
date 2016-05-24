#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, 
 wxID_FRAME1STATICBITMAP1, wxID_FRAME1STATICBOX1, 
] = [wx.NewId() for _init_ctrls in range(5)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(443, 202), size=wx.Size(463, 511),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(447, 473))

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label='staticBox1', name='staticBox1', parent=self,
              pos=wx.Point(8, 296), size=wx.Size(328, 160), style=0)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label=u'Point Dynamic Trace', name='button1', parent=self,
              pos=wx.Point(40, 344), size=wx.Size(128, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'Lorenz Trace',
              name='button2', parent=self, pos=wx.Point(40, 384),
              size=wx.Size(128, 24), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'D:/NuclearStudio/ns_pic/Reactor_Dynanic_Frame.JPG',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(8, -8),
              size=wx.Size(435, 296), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        import os
        os.system('PointDynamicTrace.py')
        event.Skip()

    def OnButton2Button(self, event):
        import os
        os.system('lorenz_trace.py')
        event.Skip()
