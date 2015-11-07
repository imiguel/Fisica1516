#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import os

class mainWindow(wx.Frame):
    #criar a estrutura da janela, menu, botoes, etc
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title="Medidor", size=(700,500))
        self.CreateStatusBar() # A StatusBar in the bottom of the window

        #criar um menu
        fileMenu = wx.Menu()

        #criar os sub-menus do menu de cima
        menuAbout = fileMenu.Append(wx.ID_ABOUT, "&Sobre", "Sobre o programa")
        menuExit = fileMenu.Append(wx.ID_EXIT,"&Sair"," Termina o programa")

        #cria a barra de menus
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu,"&Ficheiro") #adiciona o "filemenu" ao MenuBar
        self.SetMenuBar(menuBar)  #adiciona o MenuBar a janela


        #cria os eventos nos botoes do menu
        self.Bind(wx.EVT_MENU, self.onClickSobre, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnClickSair, menuExit)

        #finalmente mostra todas as opcoes
        self.Show(True)


    #Metodos dos clicks dos botoes no menu
    def onClickSobre(self,e):
        dlg = wx.MessageDialog( self, "Medidor de Densidade Liquida\nAutor: Miguel Rosa\nESTiG - IPB\nNovembro/Dezembro 2015");
        dlg.ShowModal() #mostra a caixa dialogo
        dlg.Destroy() #apos terminar, destroi

    def OnClickSair(self,e):
        self.Close(True)  # Close the frame.


aplicacao = wx.App(False)
frame = mainWindow(None, "MEDIDOR")
aplicacao.MainLoop()