# -*- coding: utf-8 -*- 
import os
import Tkinter as tk
from ttk import *
from leftpanel import LeftPanel
from rightpanel import RightPanel
from navigate import Navigate
from components.pages import *

def path_to(path):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, path)
    return filename

class App:
    def __init__(self, parent):
        self.parent = parent
        self.container = Frame(parent)
        self.container.pack(fill='both', expand=True)

        self.right_panel = RightPanel(self.container)
        Navigate.setContainer(self.right_panel.main_content.container)

        Navigate.addPage(actived=False, key='_sg', kind='single', label="FAIXA", component=song.Song(Navigate.container))
        Navigate.addPage(actived=False, key='sg', kind='list', label="FAIXAS", component=songs.Songs(Navigate.container))
        Navigate.addPage(actived=False, key='pl', kind='list', label="PLAYLISTS", component=playlists.Playlists(Navigate.container))
        Navigate.addPage(actived=False, key='ab', kind='list', label="ÁLBUNS", component=albums.Albums(Navigate.container))
        Navigate.addPage(actived=False, key='rd', kind='list', label="GRAVADORAS", component=records.Records(Navigate.container))
        Navigate.addPage(actived=False, key='cp', kind='list', label="COMPOSITORES", component=composers.Composers(Navigate.container))
        Navigate.addPage(actived=False, key='mp', kind='list', label="PERÍODOS MUSICAIS", component=periods.Periods(Navigate.container))

        self.left_panel = LeftPanel(self.container)

        Navigate.goto('sg')
    