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


class Composers(Component):
    def __init__(self, parent):
        super(Composers, self).__init__(parent)
        self.container = ScrollableFrame(parent, style="DarkGray.TFrame")

        self.composerItems = []
        self.composerList = Frame(self.container.interior,
                                style="DarkGray.TFrame")
        self.composerList.pack(fill='x')

        ListItem(self.composerList, ['Número', 'Período Musical', 'Nome', 'Cidade',
                                   'País', 'Data de Nascimento', 'Data de Morte'], None, True)

    def loadContent(self):
        DBController.execute('''
            SELECT c.cod, pm.descricao, c.nome, c.cidade, c.pais, c.dt_nasc, c.dt_morte FROM Compositor c
            INNER JOIN Periodo_Musical pm ON c.pr_msc=pm.cod
        ''')
        self.composerData = list(DBController.get())

    def pack(self):
        for composer in self.composerItems:
            composer.unpack()

        self.composerItems = []

        self.loadContent()

        for composer in self.composerData:
            def _(composer):
                dt1 = composer[5]
                dt2 = composer[6]
                titles = [
                    composer[0],
                    composer[1],
                    composer[2],
                    composer[3],
                    composer[4],
                    "%02d/%02d/%02d" % (dt1.day, dt1.month, dt1.year),
                    "%02d/%02d/%02d" % (dt2.day, dt2.month, dt2.year)
                ]

                def gotocomposer(_):
                    Navigate.goto('_cp', composer)

                self.composerItems.append(
                    ListItem(self.composerList, titles, gotocomposer))

            _(composer)

        self.container.pack(expand=True, fill='both')
