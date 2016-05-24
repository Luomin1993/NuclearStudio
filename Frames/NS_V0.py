#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import NS_V0_Frame

modules ={u'NS_V0_Frame': [1, 'Main frame of Application', u'NS_V0_Frame.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = NS_V0_Frame.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
