#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, 
 wxID_FRAME1STATICBITMAP1, wxID_FRAME1STATICBOX1, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(524, 105), size=wx.Size(436, 485),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Nuetron Reactive')
        self.SetClientSize(wx.Size(420, 447))

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Nuetron Reactive', name='staticBox1', parent=self,
              pos=wx.Point(16, 296), size=wx.Size(344, 176), style=0)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'D:/NuclearStudio/ns_pic/Nuetron_Reactive_Frame.JPG',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(410, 259), style=0)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'(n,arfa) REC',
              name='button1', parent=self, pos=wx.Point(48, 320),
              size=wx.Size(96, 32), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'(n,gama) REC',
              name='button2', parent=self, pos=wx.Point(200, 320),
              size=wx.Size(96, 32), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label=u'(n,p) REC',
              name='button3', parent=self, pos=wx.Point(48, 408),
              size=wx.Size(96, 32), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BUTTON3)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        import os
        os.system('n_arfa.py')
        event.Skip()

    def OnButton2Button(self, event):
        import os
        os.system('n_gama.py')
        event.Skip()

    def OnButton3Button(self, event):
        import os
        os.system('n_p.py')
        event.Skip()
