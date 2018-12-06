# -*- coding: utf-8 -*- 
import os
import random
from form import Form
from components.component import Component
from components.menubutton import MenuButton
import Tkinter as tk
from ttk import *

class RegisterAlbum(Component):
    def __init__(self, parent):
        super(RegisterAlbum, self).__init__(parent)
        self.container = Frame(parent, style="DarkGray.TFrame")

        self.form = Form(self.container, 'Album', [
            {'label': 'Gravadora', 'attr': 'codgrav', 'type': 'select', 'target': 'Gravadora', 'target_label': 'nome', 'target_key': 'cod'},
            {'label': 'Preço de Compra', 'attr': 'pr_compra', 'type': 'int'},
            {'label': 'Data de Compra', 'attr': 'data_compra', 'type': 'text'},
            {'label': 'Data de Gravação', 'attr': 'data_grav', 'type': 'text'},
            {'label': 'Tipo de Compra', 'attr': 'tipo_compra', 'type': 'text'},
            {'label': 'Descrição', 'attr': 'descricao', 'type': 'text'}
        ], lambda: random.randint(1, 9999))

    def pack(self):
        self.container.pack(expand=True, fill='both')

