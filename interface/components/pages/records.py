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

class Records(Component):
    def __init__(self, parent):
        super(Records, self).__init__(parent)
        self.container = ScrollableFrame(parent, style="DarkGray.TFrame")

        self.recordsItems = []
        self.recordsList = Frame(self.container.interior, style="DarkGray.TFrame")
        self.recordsList.pack(fill='x')

        ListItem(self.recordsList, ['Número', 'Nome', 'Rua', 'Cidade', 'UF', 'País', 'Nº', 'Homepage'], None, True)

    def loadContent(self):
        DBController.execute('''
            select * from Gravadora
        ''')
        self.recordsData = list(DBController.get())

    def pack(self):
        for record in self.recordsItems:
            record.unpack()

        self.recordsItems = []

        self.loadContent()

        for record in self.recordsData:
            def _(record):
                titles = [
                    record[0],
                    record[1],
                    record[2],
                    record[3],
                    record[4],
                    record[5],
                    record[6],
                    record[7]
                ]

                def gotorecord(_):
                    Navigate.goto('_ab', record)

                self.recordsItems.append(
                    ListItem(self.recordsList, titles, gotorecord))

            _(record)

        self.container.pack(expand=True, fill='both')   
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

class records(Component):
    def __init__(self, parent):
        super(records, self).__init__(parent)
        self.container = ScrollableFrame(parent, style="DarkGray.TFrame")

        self.recordsItems = []
        self.recordsList = Frame(self.container.interior, style="DarkGray.TFrame")
        self.recordsList.pack(fill='x')

        ListItem(self.recordsList, ['Número', 'Nome', 'Rua', 'Cidade', 'UF', 'País', 'Nº', 'Homepage'], None, True)

    def loadContent(self):
        DBController.execute('''
            select * from record
        ''')
        self.recordsData = list(DBController.get())

    def pack(self):
        for record in self.recordsItems:
            record.unpack()

        self.recordsItems = []

        self.loadContent()

        for record in self.recordsData:
            def _(record):
                titles = [
                    record[0],
                    record[1],
                    record[2],
                    record[3],
                    record[4],
                    record[5],
                    record[6],
                    record[7]
                ]

                def gotorecord(_):
                    Navigate.goto('_rd', record)

                self.recordsItems.append(
                    ListItem(self.recordsList, titles, gotorecord))

            _(record)

        self.container.pack(expand=True, fill='both')   
