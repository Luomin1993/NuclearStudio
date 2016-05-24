#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, 
 wxID_FRAME1STATICBITMAP1, wxID_FRAME1STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(505, 126), size=wx.Size(400, 485),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(384, 447))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'D:/NuclearStudio/ns_pic/Nuclear_primary_calculator_frame.JPG',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(360, 248), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'In this section, you can use these tools to calculator the datas you want.If you wana more accurate data,you can input the data you inquire.',
              name='staticText1', parent=self, pos=wx.Point(8, 272),
              size=wx.Size(376, 56), style=0)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label=u'micro absorb cross', name='button1', parent=self,
              pos=wx.Point(8, 336), size=wx.Size(144, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2,
              label=u'critical condition', name='button2', parent=self,
              pos=wx.Point(8, 376), size=wx.Size(144, 24), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label=u'W-S formula',
              name='button3', parent=self, pos=wx.Point(8, 416),
              size=wx.Size(144, 24), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BUTTON3)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        import os
        os.system('micro rective cross.py')
        event.Skip()

    def OnButton2Button(self, event):
        import os
        os.system('six_factors.py')
        event.Skip()

    def OnButton3Button(self, event):
        import os
        os.system('BW.py')
        event.Skip()
