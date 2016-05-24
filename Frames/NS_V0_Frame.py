#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BITMAPBUTTON1, wxID_FRAME1BUTTON1, 
 wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, wxID_FRAME1BUTTON4, 
 wxID_FRAME1BUTTON5, wxID_FRAME1BUTTON7, wxID_FRAME1CONTEXTHELPBUTTON1, 
 wxID_FRAME1CONTEXTHELPBUTTON2, wxID_FRAME1PANEL1, wxID_FRAME1PANEL2, 
 wxID_FRAME1PANEL5, wxID_FRAME1STATICBITMAP1, wxID_FRAME1STATICBITMAP2, 
 wxID_FRAME1STATICBITMAP3, wxID_FRAME1STATICBITMAP4, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, 
] = [wx.NewId() for _init_ctrls in range(20)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(568, 53), size=wx.Size(576, 571),
              style=wx.DEFAULT_FRAME_STYLE, title=u'NStudio')
        self.SetClientSize(wx.Size(560, 533))
        self.Enable(True)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(8, 264), size=wx.Size(528, 160), style=wx.NO_3D)

        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2', parent=self,
              pos=wx.Point(8, 432), size=wx.Size(528, 96),
              style=wx.TAB_TRAVERSAL)

        self.panel5 = wx.Panel(id=wxID_FRAME1PANEL5, name='panel5', parent=self,
              pos=wx.Point(8, 144), size=wx.Size(528, 96),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Real Model', name='staticText1', parent=self.panel1,
              pos=wx.Point(8, 8), size=wx.Size(58, 14), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Nuclear CAL', name='staticText2', parent=self.panel5,
              pos=wx.Point(8, 8), size=wx.Size(65, 14), style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'E Draft', name='staticText3', parent=self.panel2,
              pos=wx.Point(8, 8), size=wx.Size(62, 16), style=0)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2,
              label=u'Fence Calculator', name='button2', parent=self.panel5,
              pos=wx.Point(128, 32), size=wx.Size(112, 24), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_FRAME1BUTTON2)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1,
              label=u'Nuclear Physics', name='button1', parent=self.panel5,
              pos=wx.Point(8, 32), size=wx.Size(96, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3,
              label=u'Reactor Dynamics', name='button3', parent=self.panel5,
              pos=wx.Point(264, 32), size=wx.Size(120, 24), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_FRAME1BUTTON3)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self.panel5,
              pos=wx.Point(456, 72), size=wx.Size(64, 19),
              style=wx.BU_AUTODRAW)

        self.bitmapButton1 = wx.BitmapButton(bitmap=wx.Bitmap(u'D:/NuclearStudio/ns_pic/main2.JPG',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME1BITMAPBUTTON1,
              name='bitmapButton1', parent=self.panel1, pos=wx.Point(16, 24),
              size=wx.Size(200, 128), style=wx.BU_AUTODRAW)
        self.bitmapButton1.Bind(wx.EVT_BUTTON, self.OnBitmapButton1Button,
              id=wxID_FRAME1BITMAPBUTTON1)

        self.contextHelpButton2 = wx.ContextHelpButton(parent=self.panel1,
              pos=wx.Point(456, 136), size=wx.Size(64, 19),
              style=wx.BU_AUTODRAW)

        self.staticBitmap2 = wx.StaticBitmap(bitmap=wx.Bitmap(u'D:/NuclearStudio/ns_pic/main_1.JPG',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME1STATICBITMAP2,
              name='staticBitmap2', parent=self, pos=wx.Point(80, 8),
              size=wx.Size(472, 128), style=0)
        self.staticBitmap2.SetBackgroundStyle(wx.BG_STYLE_COLOUR)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'D:/NuclearStudio/ns_pic/main_3.JPG',
              wx.BITMAP_TYPE_JPEG), id=wxID_FRAME1STATICBITMAP1,
              name='staticBitmap1', parent=self.panel1, pos=wx.Point(456, 0),
              size=wx.Size(80, 48), style=0)

        self.staticBitmap3 = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_FRAME1STATICBITMAP3, name='staticBitmap3',
              parent=self.panel5, pos=wx.Point(296, -24), size=wx.Size(64, 8),
              style=0)

        self.staticBitmap4 = wx.StaticBitmap(bitmap=wx.Bitmap(u'D:/NuclearStudio/ns_pic/main4.PNG',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME1STATICBITMAP4,
              name='staticBitmap4', parent=self.panel2, pos=wx.Point(464, 0),
              size=wx.Size(64, 48), style=0)

        self.button4 = wx.Button(id=wxID_FRAME1BUTTON4, label=u'Chain Reactor',
              name='button4', parent=self.panel2, pos=wx.Point(16, 40),
              size=wx.Size(96, 24), style=0)
        self.button4.Bind(wx.EVT_BUTTON, self.OnButton4Button,
              id=wxID_FRAME1BUTTON4)

        self.button5 = wx.Button(id=wxID_FRAME1BUTTON5,
              label=u'Nuetron Energy Chart', name='button5', parent=self.panel2,
              pos=wx.Point(136, 40), size=wx.Size(136, 24), style=0)
        self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button,
              id=wxID_FRAME1BUTTON5)

        self.button7 = wx.Button(id=wxID_FRAME1BUTTON7,
              label=u'Nuetron Reactive', name='button7', parent=self.panel5,
              pos=wx.Point(8, 64), size=wx.Size(112, 24), style=0)
        self.button7.Bind(wx.EVT_BUTTON, self.OnButton7Button,
              id=wxID_FRAME1BUTTON7)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton2Button(self, event):
        import os
        os.system('Fence_resonance_section.py')     
        event.Skip()

    def OnButton1Button(self, event):
        import os
        os.system('Nuclear_primary_calculator.py')
        event.Skip()

    def OnButton6Button(self, event):
        event.Skip()

    def OnButton3Button(self, event):
        import os
        os.system('Reactor_Dynanic.py')
        event.Skip()

    def OnButton7Button(self, event):
        import os
        os.system('Nuetron_Reactive.py')
        event.Skip()

    def OnBitmapButton1Button(self, event):
        import os
        os.system('nuclear.blend')
        event.Skip()

    def OnButton4Button(self, event):
        import os
        os.system('Chain_pic.py')
        event.Skip()

    def OnButton5Button(self, event):
        import os
        os.system('MB_3S.py')
        event.Skip()
