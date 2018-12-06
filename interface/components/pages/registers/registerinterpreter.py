# -*- coding: utf-8 -*- 
import os
import random
from form import Form
from components.component import Component
from components.menubutton import MenuButton
import Tkinter as tk
from ttk import *

class RegisterInterpreter(Component):
    def __init__(self, parent):
        super(RegisterInterpreter, self).__init__(parent)
        self.container = Frame(parent, style="DarkGray.TFrame")

        self.form = Form(self.container, 'Interprete', [
        	{ 'label': 'Nome', 'attr': 'nome', 'type': 'text' },
        	{ 'label': 'Tipo', 'attr': 'tipo', 'type': 'text' }
        ], lambda : random.randint(1, 9999))

    def pack(self):
        self.container.pack(expand=True, fill='both')
