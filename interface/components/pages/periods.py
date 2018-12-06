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

class Periods(Component):
    def __init__(self, parent):
        super(Periods, self).__init__(parent)
        self.container = ScrollableFrame(parent, style="DarkGray.TFrame")

        self.periodsItems = []
        self.periodsList = Frame(self.container.interior, style="DarkGray.TFrame")
        self.periodsList.pack(fill='x')

        ListItem(self.periodsList, ['Número', 'Nome', 'Ano de Início', 'Ano de Término'], None, True)

    def loadContent(self):
        DBController.execute('''
            select * from Periodo_Musical
        ''')
        self.periodsData = list(DBController.get())

    def pack(self):
        for period in self.periodsItems:
            period.unpack()

        self.periodsItems = []

        self.loadContent()

        for period in self.periodsData:
            def _(period):
                titles = [
                    period[0],
                    period[1],
                    period[2],
                    period[3]
                ]

                def gotoperiod(_):
                    Navigate.goto('_mp', period)

                self.periodsItems.append(
                    ListItem(self.periodsList, titles, gotoperiod))

            _(period)

        self.container.pack(expand=True, fill='both')   
