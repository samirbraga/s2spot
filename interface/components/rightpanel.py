# -*- coding: utf-8 -*- 
import os
import Tkinter as tk
from component import Component
from menubutton import MenuButton
from navigate import Navigate
from ttk import *

def path_to(path):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, path)
    return filename

class MenuBar(Component):
    def __init__(self, parent):
        super(MenuBar, self).__init__(parent)
        self.container = Frame(parent, style="Gray.TFrame", height=75)
        self.container.pack_propagate(False)
        self.function = {
            'icon': "assets\\add-playlist.gif",
            'href': 'rpl'
        }
        self.menu_btn = MenuButton(self.container, self.function['icon'])

        def gotoRegister(page):
            if page['kind'] == 'list':
                self.menu_btn.pack()
                self.menu_btn.unbind("<Button 1>")
                self.menu_btn.bind('<Button-1>', lambda _: Navigate.goto("r%s"%(page['key'])))
            else:
                self.menu_btn.unpack()

        Navigate.addListener("__all__", gotoRegister)

        self.header = Label(self.container, style='HeaderGray.TLabel')
        self.header.pack(side='left', fill='y', padx=(15, 0))

        def changeHeader(page):
            self.header.configure(text=page['label'])

        Navigate.addListener('__all__', changeHeader)

        self.pack()
    
    def pack(self):
        self.container.pack(fill='x')

class ControlsBar(Component):
    def __init__(self, parent):
        super(ControlsBar, self).__init__(parent)
        self.container = Frame(parent, style="Gray.TFrame", height=75)
        self.container.pack_propagate(False)
        self.pack()

        self.nextBtn = MenuButton(
            self.container, 'assets\\play-next-button.gif')
        self.nextBtn.pack(anchor='center', fill='y')

        self.playBtn = MenuButton(self.container, 'assets\\play-button.gif')
        self.playBtn.pack(anchor='center', fill='y')

        self.previousBtn = MenuButton(
            self.container, 'assets\\play-previous-button.gif')
        self.previousBtn.pack(anchor='center', fill='y')
    
    def pack(self):
        self.container.pack(fill='both')

class MainContent(Component):
    def __init__(self, parent):
        super(MainContent, self).__init__(parent)
        self.container = Frame(parent, style="LightGray.TFrame")
        self.pack()

    def pack(self):
        self.container.pack(side='top', fill='both', expand=True)

class RightPanel(Component):
    def __init__(self, parent):
        super(RightPanel, self).__init__(parent)
        self.container = Frame(parent, style="DarkGray.TFrame")
        self.menu_bar = MenuBar(self.container)
        self.main_content = MainContent(self.container)
        self.controls_bar = ControlsBar(self.container)
        self.pack()

    def pack(self):
        self.container.pack(side='right', fill='both', expand=True) 
