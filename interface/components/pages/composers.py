# -*- coding: utf-8 -*- 
import os
from components.component import Component
from components.menubutton import MenuButton
import Tkinter as tk
from ttk import *

class Composers(Component):
    def __init__(self, parent):
        super(Composers, self).__init__(parent)
        self.container = Frame(parent, style="DarkGray.TFrame")

        self.text = Button(self.container, text="Compositores")
        self.text.pack()

    def pack(self):
        self.container.pack(expand=True, fill='both')