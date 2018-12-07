# -*- coding: utf-8 -*- 
import os
from db.dbcontroller import DBController
from components.component import Component
from components.menubutton import MenuButton
from components.navigate import Navigate
import Tkinter as tk
from ttk import *

class Song(Component):
    def __init__(self, parent):
        super(Song, self).__init__(parent)
        self.container = Frame(parent, style="DarkGray.TFrame", width=500)
        self.content = Frame(self.container, style="DarkGray.TFrame", width=500)
        self.add2playlist = Frame(self.content, style="DarkGray.TFrame")
        self.addLabel = Label(self.content, style="DarkGray.TLabel", text="Adicione a playlist: ")
        self.addSelectVar = tk.StringVar(self.content)

        DBController.execute('''
            SELECT nome, cod FROM Playlist
        ''')

        results = [("%d- %s" % (i, result[0]), result[1]) for i, result in enumerate(DBController.get())]
        choices = set([result[0] for result in results])
        self.addSelect = OptionMenu(self.content, self.addSelectVar, *choices)

        def addToPlaylist(*args):
            song_code = Navigate.current_data[0]
            DBController.execute('''
                SELECT cod_alb FROM Faixa WHERE cod=%s
            ''' % song_code)
            cod_alb = list(DBController.get())
            cod_alb = cod_alb[0][0]
            index = int(self.addSelectVar.get().split("-")[0])
            cod_pl = int(results[index][1])
            
            DBController.execute('''
                DELETE FROM Playlist_Faixa WHERE cod_faixa=? AND cod_alb=?
            ''', song_code, cod_alb)
            DBController.commit()

            DBController.execute('''
                INSERT INTO Playlist_Faixa VALUES (?, ?, ?)
            ''', cod_pl, song_code, cod_alb)
            DBController.commit()

        self.addSelectVar.trace('w', addToPlaylist)
        self.infos = []

    def loadContent(self):
    	label_translater = ["NUMERO", "NOME", "ALBUM", "COMPOSICAO", "TIPO", "DESCRICAO", "DURACAO"]

        self.content.pack_forget()

        for info in self.infos:
        	info.pack_forget()

        self.infos = []

        if Navigate.current_data:
	        for i, value in enumerate(Navigate.current_data):
	        	def _(value):
			        text = Label(self.content, style="DarkGray.TLabel", text="%s: %s" % (label_translater[i], value))
			        self.infos.append(text)
		        	text.pack(fill='x', pady=10)

		        _(value)

    def pack(self):
    	self.loadContent()

        self.container.pack(anchor='center', side='top')
        self.addLabel.pack(anchor='center', side='top')
        self.addSelect.pack(anchor='center', side='top')
        self.content.pack(anchor='center', side='top', padx=30, pady=30)

    def unpack(self):
        self.content.pack_forget()
        self.container.pack_forget()
