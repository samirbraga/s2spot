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

class Songs(Component):
    def __init__(self, parent):
        super(Songs, self).__init__(parent)
        self.container = ScrollableFrame(parent, style="DarkGray.TFrame")

        self.songsItems = []
        self.songsList = Frame(self.container.interior, style="DarkGray.TFrame")
        self.songsList.pack(fill='x')

        ListItem(self.songsList, ['Número', 'Nome', 'Álbum', 'Composição', 'Tipo', 'Descrição', 'Duração'], None, True)

    def loadContent(self):
        DBController.execute('''
            SELECT f.cod, pl.nome, a.descricao, f.tipo_comp, f.tipo_grav, f.descricao, f.tempo_exec
            FROM Faixa f INNER JOIN Playlist pl ON f.cod_alb=pl.cod
            INNER JOIN Album a ON a.cod=f.cod_alb
        ''')
        self.songsData = list(DBController.get())

    def pack(self):
        for song in self.songsItems:
            song.unpack()

        self.songsItems = []

        self.loadContent()

        if len(self.songsData):
            for song in self.songsData:
                def _(song):
                    sec = timedelta(seconds=song[6]/1000)
                    dt = datetime(1, 1, 1) + sec
                    titles = [
                        song[0],
                        song[1],
                        song[2],
                        song[3],
                        song[4],
                        " ".join(song[5].split(' ')[0:5]) + '...',
                        "%02d:%02d:%02d" % (dt.hour, dt.minute, dt.second)
                    ]

                    def gotoSong(_):
                        Navigate.goto('_sg', song)

                    self.songsItems.append(
                        ListItem(self.songsList, titles, gotoSong))

                _(song)
        else:
            self.songsItems.append(
                ListItem(self.songsList, ['Nenhuma música cadastrada.'], lambda _: _))

        self.container.pack(expand=True, fill='both')   
