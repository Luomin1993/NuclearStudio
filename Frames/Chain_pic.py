#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import Chain_pic_Frame

modules ={u'Chain_pic_Frame': [1, 'Main frame of Application', u'Chain_pic_Frame.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = Chain_pic_Frame.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
