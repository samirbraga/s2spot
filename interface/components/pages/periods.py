# -*- coding: utf-8 -*- 
import os
from components.component import Component
from components.menubutton import MenuButton
import Tkinter as tk
from ttk import *

class Periods(Component):
    def __init__(self, parent):
        super(Periods, self).__init__(parent)
        self.container = Frame(parent, style="DarkGray.TFrame")

        self.text = Button(self.container, text="Períodos Musicais")
        self.text.pack()

    def pack(self):
        self.container.pack(expand=True, fill='both')