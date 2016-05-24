#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import Nuetron_Reactive_Frame

modules ={u'Nuetron_Reactive_Frame': [1,
                             'Main frame of Application',
                             u'Nuetron_Reactive_Frame.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = Nuetron_Reactive_Frame.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
