import os
import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500,500))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A StatusBar in the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Sobre o programa")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Termina o programa")
        menuMedicao = filemenu.Append(wx.ID_ANY,"M&edir", "Regista nova medicao")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        menuBar.Append(filemenu,"&Medicao")
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.onMedir, menuMedicao)

        self.Show(True)

    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "MEDIDOR DENSIDADE LIQUIDA\nEscola Superior Tecnologia e Gestao - Instituto Politecnico Beja\nAutor: Miguel Rosa\nNovembro 2015", "Medidor Densidade", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    def onMedir(self,e):
        dlg = wx.MessageDialog( self, "Nova Medicao by MENU");
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()