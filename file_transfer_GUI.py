import wx
import os, sys
import datetime
import sqlite3
import file_transfer_time
import file_transfer_db





    


class transfer(wx.Frame):

    conn = sqlite3.connect('modified.db')
    c = conn.cursor()
    
    def __init__(self, *args, **kwargs):
        super(transfer, self).__init__(*args, **kwargs)
        
        self.dirname = ''
        self.basicGUI()
        self.SetSize((700, 500))

    def basicGUI(self):
        panel = wx.Panel(self)
        self.path1 = wx.TextCtrl(panel, pos = (330, 130), size = (200, 20), style = wx.TE_MULTILINE)
        self.path2 = wx.TextCtrl(panel, pos = (330, 230), size = (200, 20), style = wx.TE_MULTILINE)
        self.time_path = wx.TextCtrl(panel, pos = (370, 325), size = (115, 20))
        path = file_transfer_db.time_grab()
        self.time_path.SetValue(path)
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit')
        font1 = wx.Font(12, wx.DECORATIVE, wx.SLANT, wx.BOLD)
        font2 = wx.Font(12, wx.SCRIPT, wx.NORMAL, wx.BOLD)
        cb1 = wx.Button(panel, label = 'File Directory', pos = (25, 130))
        cb2 = wx.Button(panel, label = 'File Directory', pos = (25, 230))
        trans_but = wx.Button(panel, label = 'File Check', pos = (30, 400))
        clear = wx.Button(panel, label = 'Cancel', pos = (200, 400))
        stat_panel = wx.Panel(panel, pos = (100, 100), size = (200, 200))
        
        
        
        menuBar.Append(fileButton, 'File')
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        self.Bind(wx.EVT_BUTTON, self.fil1, cb1)
        self.Bind(wx.EVT_BUTTON, self.fil2, cb2)
        self.Bind(wx.EVT_BUTTON, self.trans, trans_but)

        heading = wx.StaticText(panel, label='File Transfer', pos = (295, 20))
        heading.SetFont(font1)
        wx.StaticLine(panel, pos = (175, 50), size = (350, 1))
        

        ex1 = wx.StaticText(panel, label = "File Exporting Folder", pos = (25, 100))
        ex1.SetFont(font2)
        ex1.SetForegroundColour((218,165,32))

        ex2 = wx.StaticText(panel, label = "File Receiving Folder", pos = (25, 200))
        ex2.SetFont(font2)
        ex2.SetForegroundColour((218,165,32))

        ex3 = wx.StaticText(panel, label = "Last File Check Time", pos = (350, 300))
        ex3.SetFont(font2)
        ex3.SetForegroundColour((218,165,32))

        self.Show(True)
        

    def Quit(self, event):
        file_trnasfer_GUI.close()
        self.Close()
        

    def fil1(self, event):
        with wx.DirDialog(self, "Choose a file to open:", self.dirname,
                           style = wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                root_path = dlg.GetPath()
                file_transfer_time.dir_src = root_path
                self.path1.SetValue(root_path)
            dlg.Destroy()

    def fil2(self, event):
        with wx.DirDialog(self, "Choose a file to open:", self.dirname,
                           style = wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                root_path = dlg.GetPath()
                file_transfer_time.dir_dst = root_path
                self.path2.SetValue(root_path)
            dlg.Destroy()

    def trans(self, event):
            file_transfer_time.move()
            file_transfer_db.dataEntry()
            path = file_transfer_db.time_grab()
            self.time_path.SetValue(path)
            self.path1.Clear()
            self.path2.Clear()
            wx.MessageBox('The most Recent files have been transfered')
             

        
def main():
    app = wx.App()
    transfer(None, title='File Transfer')
    app.MainLoop()


if __name__ == '__main__': main()
