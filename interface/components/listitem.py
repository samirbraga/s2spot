# -*- coding: utf-8 -*- 
import os
from component import Component
from menubutton import MenuButton
import Tkinter as tk
from ttk import *

class ListItem(Component):
    def __init__(self, parent, titles, cb, isHeader=False):
        super(ListItem, self).__init__(parent)
        self.container = Frame(parent, style="DarkGray.TFrame")
        self.container.pack(fill='x')
        self.titles_container = Frame(self.container, style="DarkGray.TFrame")
        self.titles_container.pack(fill='x', expand=True)
        self.titles = []
        
        for title in titles:
            frame = Frame(self.titles_container, style='DarkGray.TFrame', height=60)
            frame.pack_propagate(False)
            frame.pack(fill='both', side='left', expand=True)
            label_class = 'HeaderLightGray.TLabel' if isHeader else 'DarkGray.TLabel'
            label = Label(frame, style=label_class, text=title)
            label.pack(fill='y', padx=(15, 0), pady=(20, 0))
            self.titles.append(frame)
        
        self.button_container = Frame(self.titles_container, style='DarkGray.TFrame', width=60)
        self.button_container.pack_propagate(False)
        self.button_container.pack(fill='y', side='left')
        
        if not isHeader:
            self.button = MenuButton(self.button_container, 'assets\\small-search.gif')
            if cb:
                self.button.bind('<Button-1>', cb)
            self.button.pack(fill='y')
        
        self.separator = Frame(self.container, height=1, style="SeparatorGray.TFrame")
        self.separator.pack(fill='x')
