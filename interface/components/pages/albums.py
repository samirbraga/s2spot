# -*- coding: utf-8 -*- 
import os
import Tkinter as tk
from ttk import *
from db.dbcontroller import DBController
from datetime import datetime, timedelta
from components.navigate import Navigate
from components.listitem import ListItem
from components.menubutton import MenuButton
from components.component import Component
from components.scrollableframe import ScrollableFrame
from components.menubutton import MenuButton

class Albums(Component):
    def __init__(self, parent):
        super(Albums, self).__init__(parent)
        self.container = ScrollableFrame(parent, style="DarkGray.TFrame")

        self.albumsItems = []
        self.albumsList = Frame(self.container.interior, style="DarkGray.TFrame")
        self.albumsList.pack(fill='x')

        ListItem(self.albumsList, ['Número', 'Gravadora', 'Preço', 'Data de Compra', 'Data de Gravação', 'Tipo de Compra', 'Descrição'], None, True)

    def loadContent(self):
        DBController.execute('''
            SELECT a.cod, g.nome, a.pr_compra, a.data_compra, a.data_grav, a.tipo_compra, a.descricao
            FROM Album a INNER JOIN Gravadora g ON a.codgrav=g.cod
        ''')
        self.albumsData = list(DBController.get())

    def pack(self):
        for album in self.albumsItems:
            album.unpack()

        self.albumsItems = []

        self.loadContent()

        for album in self.albumsData:
            def _(album):
                dt = album[3]
                titles = [
                    album[0],
                    album[1],
                    album[2],
                    "%02d/%02d/%02d" % (dt.day, dt.month, dt.year),
                    album[4],
                    album[5],
                    album[6]
                ]

                def gotoalbum(_):
                    Navigate.goto('_ab', album)

                self.albumsItems.append(
                    ListItem(self.albumsList, titles, gotoalbum))

            _(album)

        self.container.pack(expand=True, fill='both')   
