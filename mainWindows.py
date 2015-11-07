import os
import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title="Medidor", size=(700,500))
        self.initUI()


    def initUI(self):
        menubar = wx.Menu()

        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_ANY, "&Ficheiro")
        fileMenu.AppendSeparator()
        aboutOnClick = fileMenu.Append((wx.ID_ANY, "&Sobre"))
        exitOnClick = fileMenu.Append(wx.ID_EXIT, "&Sair")

        #sub-menu opcoes de recolha de dados
        novoRegisto = wx.Menu()
        novoRegisto.Append(wx.ID_ANY, "&Novo Registo")
        novoRegisto.Append(wx.ID_ANY, "&Guardar Registo")

        #adidionar o sub-menu ao menu
        fileMenu.Append(wx.ID_ANY, '&Novos Registos', novoRegisto)

        #adicionar funcoes aos 'botoes' dos menus
        self.Bind(wx.EVT_MENU, self.onClickAbout, aboutOnClick)
        self.Bind(wx.EVT_MENU, self.onClickExit, exitOnClick)

        #adicionar o menu a frame
        menubar.Append(fileMenu, "&Ficheiro")
        self.SetMenuBar(menubar)
        self.Show()


        def onClickAbout(self, e):
            dlg = wx.MessageDialog( self, "Medidor de Densidade Liquida\nAutor: Miguel Rosa\nESTiG - IPB\nNovembro/Dezembro 2015");
            dlg.ShowModal() #mostra a caixa dialogo
            dlg.Destroy() #apos terminar, destroi

        def onClickExit(self,e):
            self.Close(True)  # Close the frame




def main():
    app = wx.App(False)
    frame = MainWindow(None, "Medidor de densidade")
    app.MainLoop()