# -*- coding: utf-8 -*- 
import os
import random
from form import Form
from components.component import Component
from components.menubutton import MenuButton
import Tkinter as tk
from ttk import *

class RegisterPeriod(Component):
    def __init__(self, parent):
        super(RegisterPeriod, self).__init__(parent)
        self.container = Frame(parent, style="DarkGray.TFrame")

        self.form = Form(self.container, 'Compositor', [
        	{ 'label': 'Nome', 'attr': 'descricao', 'type': 'text' },
        	{ 'label': 'Ano de Início', 'attr': 'ano_inicio', 'type': 'text' },
        	{ 'label': 'Ano de Término', 'attr': 'ano_fim', 'type': 'text' }
        ], lambda _: random.randint(1, 999999))

    def pack(self):
        self.container.pack(expand=True, fill='both')
