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
from components.navigate import Navigate

class Songs(Component):
    def __init__(self, parent, query=None, callback=None):
        super(Songs, self).__init__(parent)
        self.container = ScrollableFrame(parent, style="DarkGray.TFrame")

        self.callback = callback
        self.query = query
        self.songsItems = []
        self.songsList = Frame(self.container.interior, style="DarkGray.TFrame")
        self.songsList.pack(fill='x')

        ListItem(self.songsList, ['Número', 'Playlist', 'Álbum', 'Composição', 'Tipo', 'Descrição', 'Duração'], None, True)

    def loadContent(self):
        query = self.query
        if not self.query:
            query = '''
                SELECT f.cod, pl.nome, a.descricao, f.tipo_comp, f.tipo_grav, f.descricao, f.tempo_exec
                FROM Faixa f LEFT OUTER JOIN Playlist_Faixa pf ON pf.cod_alb=f.cod_alb AND pf.cod_faixa=f.cod
                LEFT OUTER JOIN Playlist pl ON pl.cod=pf.cod_play
                LEFT OUTER JOIN Album a ON a.cod=f.cod_alb
                WHERE f.descricao LIKE '%{}%'
            '''.format(Navigate.current_search)
        if self.callback:
            DBController.execute(query, self.callback())
        else:
            DBController.execute(query)
        self.songsData = list(DBController.get())

    def pack(self):
        for song in self.songsItems:
            song.unpack()

        self.songsItems = []

        self.loadContent()

        if len(self.songsData):
            for song in self.songsData:
                def _(song):
                    sec = timedelta(seconds=song[6])
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
