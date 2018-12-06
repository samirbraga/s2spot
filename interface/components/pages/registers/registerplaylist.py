# -*- coding: utf-8 -*- 
import os
import random
from form import Form
from components.component import Component
from components.menubutton import MenuButton
import Tkinter as tk
from ttk import *

class RegisterPlaylist(Component):
    def __init__(self, parent):
        super(RegisterPlaylist, self).__init__(parent)
        self.container = Frame(parent, style="DarkGray.TFrame")

        self.form = Form(self.container, 'Playlist', [
            {'label': 'Nome', 'attr': 'nome', 'type': 'text'},
            {'label': 'Data de Criação', 'attr': 'data_criacao', 'type': 'text'},
            {'label': 'Tempo Total', 'attr': 'tempo_total', 'type': 'int'}
        ], lambda: random.randint(1, 9999))

    def pack(self):
        self.container.pack(expand=True, fill='both')
