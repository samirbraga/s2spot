# -*- coding: utf-8 -*- 
import os
from form import Form
from components.component import Component
from components.menubutton import MenuButton
import Tkinter as tk
from ttk import *

class RegisterComposer(Component):
    def __init__(self, parent):
        super(RegisterComposer, self).__init__(parent)
        self.container = Frame(parent, style="DarkGray.TFrame")

        # self.form = Form(self.container, 'Compositor', [
        # 	{ 'label': 'Nome', 'attr': 'nome', 'type': 'text' },
        # 	{ 'label': 'Idade', 'attr': 'idade', 'type': 'select', 'options': ['um', 'dois'] },
        # ])

    def pack(self):
        self.container.pack(expand=True, fill='both')