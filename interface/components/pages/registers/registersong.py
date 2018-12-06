# -*- coding: utf-8 -*- 
import os
import random
from form import Form
from components.component import Component
from components.menubutton import MenuButton
import Tkinter as tk
from ttk import *

class RegisterSong(Component):
    def __init__(self, parent):
        super(RegisterSong, self).__init__(parent)
        self.container = Frame(parent, style="DarkGray.TFrame")

        self.form = Form(self.container, 'Faixa', [
            {'label': 'Álbum', 'attr': 'cod_alb', 'type': 'select', 'target': 'Album', 'target_label': 'descricao', 'target_key': 'cod'},
            {'label': 'Tipo de Composição', 'attr': 'tipo_comp', 'type': 'select', 'target': 'Tipo_Comp', 'target_label': 'descricao', 'target_key': 'cod'},
            {'label': 'Tempo de execução', 'attr': 'tempo_exec', 'type': 'text'},
            {'label': 'Tipo de Gravação', 'attr': 'tipo_grav', 'type': 'text'},
            {'label': 'Descrição', 'attr': 'descricao', 'type': 'text'}
        ], lambda: random.randint(1, 9999))

    def pack(self):
        self.container.pack(expand=True, fill='both')
