#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import Reactor_Dynanic_Frame

modules ={u'Reactor_Dynanic_Frame': [1,
                            'Main frame of Application',
                            u'Reactor_Dynanic_Frame.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = Reactor_Dynanic_Frame.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
