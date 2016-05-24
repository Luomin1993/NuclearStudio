#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import Nuclear_primary_calculator_frame

modules ={u'Nuclear_primary_calculator_frame': [1,
                                       'Main frame of Application',
                                       u'Nuclear_primary_calculator_frame.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = Nuclear_primary_calculator_frame.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
