# -*- coding: utf-8 -*- 
import os
from components.component import Component
from components.menubutton import MenuButton
from components.navigate import Navigate
import Tkinter as tk
from ttk import *

class Song(Component):
    def __init__(self, parent):
        super(Song, self).__init__(parent)
        self.container = Frame(parent, style="DarkGray.TFrame")
        self.content = Frame(self.container, style="DarkGray.TFrame")
        self.infos = []

    def loadContent(self):
    	label_translater = {
    		"composition": "COMPOSIÇÃO",
    		"time": "DURAÇÃO",
    		"record_type": "TIPO DE GRAVAÇÃO",
    		"number": "POSIÇÃO",
    		"description": "DESCRIÇÃO"
    	}

        self.content.pack_forget()

        for info in self.infos:
        	info.pack_forget()

        self.infos = []

        if Navigate.current_data:
	        for label in Navigate.current_data:
	        	def _(label):
			        text = Label(self.content, text="{label}: {value}".format(label=label_translater[label], value=Navigate.current_data[label]))
			        self.infos.append(text)
		        	text.pack(fill='x')

		        _(label)

    def pack(self):
    	self.loadContent()

        self.container.pack(expand=True, fill='both')
        self.content.pack(expand=True, fill='both')

    def unpack(self):
        self.content.pack_forget()
        self.container.pack_forget()