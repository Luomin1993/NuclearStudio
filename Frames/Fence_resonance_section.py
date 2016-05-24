#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import Fence_resonance_section_Frame

modules ={u'Fence_resonance_section_Frame': [1,
                                    'Main frame of Application',
                                    u'Fence_resonance_section_Frame.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = Fence_resonance_section_Frame.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
