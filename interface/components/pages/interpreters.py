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

class Interpreters(Component):
    def __init__(self, parent):
        super(Interpreters, self).__init__(parent)
        self.container = ScrollableFrame(parent, style="DarkGray.TFrame")

        self.interpretersItems = []
        self.interpretersList = Frame(self.container.interior, style="DarkGray.TFrame")
        self.interpretersList.pack(fill='x')

        ListItem(self.interpretersList, ['Número', 'Nome', 'Tipo'], None, True)

    def loadContent(self):
        DBController.execute('''
            select * from Interprete
        ''')
        self.interpretersData = list(DBController.get())

    def pack(self):
        for interpreter in self.interpretersItems:
            interpreter.unpack()

        self.interpretersItems = []

        self.loadContent()

        for interpreter in self.interpretersData:
            def _(interpreter):
                titles = [
                    interpreter[0],
                    interpreter[1],
                    interpreter[2]
                ]

                def gotointerpreter(_):
                    Navigate.goto('_it', interpreter)

                self.interpretersItems.append(
                    ListItem(self.interpretersList, titles, gotointerpreter))

            _(interpreter)

        self.container.pack(expand=True, fill='both')   
