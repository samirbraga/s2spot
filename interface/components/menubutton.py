# -*- coding: utf-8 -*- 
import os
from component import Component
import Tkinter as tk
from ttk import *

def path_to(path):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, path)
    return filename

class MenuButton(Component):
    def __init__(self, parent, path, to_pack=True):
        super(MenuButton, self).__init__(parent)

        button_icon = tk.PhotoImage(file=path)
        self.container = tk.Button(parent,
            background="black",
            width=75,
            borderwidth=0,
            image=button_icon
        )
        self.container.image = button_icon

        self.container.bind('<Enter>', lambda x: self.changeBg('#282828'))
        self.container.bind('<Leave>', lambda x: self.changeBg('#000000'))
        self.container.bind('<Button-1>', lambda x: self.changeBg('#111111'))
        self.container.bind('<ButtonRelease-1>', lambda x: self.changeBg('#000000'))

        if to_pack:
            self.pack()

    def bind(self, evt, cb):
        self.container.bind(evt, cb)

    def changeBg(self, bg):
        self.container.config(background=bg)

    def pack(self, fill='y', expand=False, side='right', anchor='e'):
        self.container.pack(fill=fill, expand=expand, side=side, anchor=anchor)