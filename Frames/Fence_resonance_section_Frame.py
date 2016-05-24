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
              pos=wx.Point(597, 194), size=wx.Size(482, 485),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(466, 447))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'D:/NuclearStudio/ns_pic/fence_frame.JPG',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(448, 264), style=0)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Fence inaverage effect', name='staticBox1', parent=self,
              pos=wx.Point(8, 272), size=wx.Size(256, 176), style=0)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label=u'NR/NRIM Fuel resonance nuetron flex', name='button1',
              parent=self, pos=wx.Point(16, 320), size=wx.Size(216, 24),
              style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2,
              label=u'effective resonance integral', name='button2',
              parent=self, pos=wx.Point(16, 376), size=wx.Size(216, 24),
              style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        import os
        os.system('Fuel_resonance_nuetron_flex.py')
        event.Skip()

    def OnButton2Button(self, event):
        import os
        os.system('resonance_integral.py')
        event.Skip()
