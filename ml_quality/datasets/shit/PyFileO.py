'''
Author: Muhammad Aman (therefore the "MA" in "MAthecoder")
Project Name: Python made File Organiser
'''

from organisingsystems import OrganiserSystem as OrgSys
import wx

class MainApp(wx.Frame):

    def __init__(self,parent,id):

        global organise
        organise=OrgSys()

        wx.Frame.__init__(self,parent,id,'PyFileO (Alpha v0.0.3) by MATc',size=(350,250))
        panel = wx.Panel(self)
        self.button1 = wx.Button(panel,label = 'Type a path',pos=(15,120),size=(300,-1))
        self.button2 = wx.Button(panel,label = 'Browse for a path',pos=(15,160),size=(300,-1))
        self.Bind(wx.EVT_BUTTON,self.getPathtxt,self.button1)
        self.Bind(wx.EVT_BUTTON,self.onPathBrowse,self.button2)

    def getPathtxt(self,event):
        txtBox=wx.TextEntryDialog(None,'Please enter an absolute path','Type a path','Ex: C:/Users/Matc/Downloads')
        if txtBox.ShowModal()==wx.ID_OK:
            path=txtBox.GetValue()
            organise.StartSorting(path)

        
            
    def onPathBrowse(self, event):
        dlg = wx.DirDialog(self, "Choose a directory:",style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            path=dlg.GetPath()
            organise.StartSorting(path)
        dlg.Destroy()

        
        
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MainApp(parent = None,id = -1)
    frame.Show()
    app.MainLoop()

