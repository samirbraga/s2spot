# -*- coding: utf-8 -*- 
import os
from menubutton import MenuButton
from navigate import Navigate
import Tkinter as tk
from ttk import *

def path_to(path):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, path)
    return filename

class OptionsList:
    def __init__(self, parent, text, clickbind):
        self.parent = parent
        self.container = Frame(parent, height=50, style='Option.TFrame')
        self.container.pack_propagate(False)
        self.container.pack(fill='x', anchor='n', pady=0, padx=10)
        
        self.text = tk.Button(self.container,
            background="#000000",
            foreground="white",
            borderwidth=0,
            text=text,
            compound=tk.LEFT,
            justify=tk.LEFT
        )
        self.text.pack(fill='both', expand=True, anchor='w')
        self.text.bind('<Button-1>', clickbind)

        self.separator = Frame(self.container, height=1, style="Separator.TFrame")
        self.separator.pack(side='bottom', fill='x')
    
    def bind(self, evt, cb):
        self.text.bind(evt, cb)

class LeftPanel:
    def __init__(self, parent):
        self.parent = parent
        self.container = Frame(parent, style="Black.TFrame", width=275)
        self.container.pack_propagate(False)
        self.container.pack(side='left', fill='y')

        self.header = Frame(self.container, height=75, style="Black.TFrame")
        self.header.pack_propagate(False)
        self.header.pack(side='top', fill='x')

        self.search_button = MenuButton(self.header, "assets\\search.gif")

        list_pages = [page for page in Navigate.pages if page['kind'] == 'list']

        self.options_list = list(map(
            lambda opt: OptionsList(self.container, opt['label'], lambda x: Navigate.goto(opt['key'])),
            list_pages
        ))

        def navigateCallback(page):
            for i, opt in enumerate(list_pages):
                if opt['kind'] == 'list':
                    self.options_list[i].text.configure(background="#000000")

                    if opt['key'] == page['key']:
                        self.options_list[i].text.configure(background="#333333")

        for i, opt in enumerate(list_pages):
            if opt['kind'] == 'list':
                Navigate.addListener(opt['key'], navigateCallback)

        self.footer = Frame(self.container, height=75, style="Black.TFrame")
        self.footer.pack_propagate(False)
        self.footer.pack(side='bottom', fill='x')

        self.exit_button = MenuButton(self.footer, "assets\\exit.gif", False)
        self.exit_button.pack(side='bottom', anchor='w', fill='y', expand=True)