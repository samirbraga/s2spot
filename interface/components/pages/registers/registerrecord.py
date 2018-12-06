# -*- coding: utf-8 -*- 
import os
import random
from form import Form
from components.component import Component
from components.menubutton import MenuButton
import Tkinter as tk
from ttk import *

class RegisterRecord(Component):
    def __init__(self, parent):
        super(RegisterRecord, self).__init__(parent)
        self.container = Frame(parent, style="DarkGray.TFrame")

        self.form = Form(self.container, 'Gravadora', [
            {'label': 'Nome', 'attr': 'nome', 'type': 'text'},
           	{'label': 'Rua', 'attr': 'rua', 'type': 'text'},
           	{'label': 'Cidade', 'attr': 'cidade', 'type': 'text'},
           	{'label': 'UF', 'attr': 'uf', 'type': 'text'},
           	{'label': 'País', 'attr': 'pais', 'type': 'text'},
           	{'label': 'Nº', 'attr': 'numero', 'type': 'int'},
           	{'label': 'Homepage', 'attr': 'homepage', 'type': 'text'}
        ], lambda: random.randint(1, 9999))

    def pack(self):
        self.container.pack(expand=True, fill='both')
