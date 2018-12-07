# -*- coding: utf-8 -*- 
import os
from components.component import Component
from components.menubutton import MenuButton
from components.navigate import Navigate
from components.pages.songs import Songs
import Tkinter as tk
from ttk import *

class Playlist(Component):
    def __init__(self, parent):
        super(Playlist, self).__init__(parent)
        self.container = Frame(parent, style="Black.TFrame")
        self.content = Frame(self.container, style="Black.TFrame", width=500)
        self.songs = Frame(self.container, style="Black.TFrame")
        self.song_list=Songs(self.songs, '''
            SELECT f.cod, pl.nome, a.descricao, f.tipo_comp, f.tipo_grav, f.descricao, f.tempo_exec
            FROM Faixa f INNER JOIN Playlist_Faixa pf ON pf.cod_alb=f.cod_alb AND pf.cod_faixa=f.cod
            INNER JOIN Playlist pl ON pl.cod=pf.cod_play
            INNER JOIN Album a ON a.cod=f.cod_alb
            WHERE pl.cod=?''', lambda : Navigate.current_data[0] if Navigate.current_data else 0)

        self.infos = []

    def loadContent(self):
    	label_translater = ["NUMERO", "TITULO", "DATA DE CRIACAO", "TEMPO TOTAL"]

        self.content.pack_forget()

        for info in self.infos:
            info.pack_forget()

        self.infos = []

        if Navigate.current_data:
            for i, value in enumerate(Navigate.current_data):
                def _(value):
                    text = Label(self.content, style="Black.TLabel", text="%s: %s" % (label_translater[i], value))
                    self.infos.append(text)
                    text.pack(fill='x', pady=20)

                _(value)

    def pack(self):
        self.loadContent()

        self.container.pack(fill='both', anchor='center', expand=True, side='top')
        self.content.pack(anchor='center', side='top', fill='y', padx=30, pady=30)
        self.songs.pack(fill='both', anchor='center', side='top', expand=True)
        self.song_list.pack()


    def unpack(self):
        self.content.pack_forget()
        self.container.pack_forget()
        self.songs.pack_forget()
        self.song_list.unpack()