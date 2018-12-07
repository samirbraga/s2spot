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

class Playlists(Component):
    def __init__(self, parent, query=None):
        super(Playlists, self).__init__(parent)
        self.container = ScrollableFrame(parent, style="DarkGray.TFrame")

        self.query = query
        self.playlistsItems = []
        self.playlistsList = Frame(self.container.interior, style="DarkGray.TFrame")
        self.playlistsList.pack(fill='x')

        ListItem(self.playlistsList, ['Número', 'Nome', 'Data de Criação', 'Tempo total'], None, True)

    def loadContent(self):
        query = self.query
        if not self.query:
            query = '''
                select * from Playlist
            '''
        DBController.execute(query)
        self.playlistsData = list(DBController.get())

    def pack(self):
        for playlist in self.playlistsItems:
            playlist.unpack()

        self.playlistsItems = []

        self.loadContent()

        for playlist in self.playlistsData:
            def _(playlist):
                dt = playlist[2]
                titles = [
                    playlist[0],
                    playlist[1],
                    "%02d/%02d/%02d" % (dt.day, dt.month, dt.year),
                    playlist[3]
                ]

                def gotoplaylist(_):
                    Navigate.goto('_pl', playlist)

                self.playlistsItems.append(
                    ListItem(self.playlistsList, titles, gotoplaylist))

            _(playlist)

        self.container.pack(expand=True, fill='both')   
