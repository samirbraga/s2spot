# -*- coding: utf-8 -*- 
import os
import Tkinter as tk
from ttk import *
from leftpanel import LeftPanel
from rightpanel import RightPanel
from navigate import Navigate
from db.dbcontroller import DBController
from components.pages import *
from components.pages.registers import *
from components.pages.singles import *

def path_to(path):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, path)
    return filename

class App(tk.Tk):
    def __init__(self, parent):
        # DBController.connect(database='S2spot', server="LEC17\FBDSERVER", user='sa', password='Admin123')
        DBController.connect(database='S2spot', server="DESKTOP-LMO6LAE\SQLEXPRESS", user=None, password=None)

        self.parent = parent
        self.container = Frame(parent)
        self.container.pack(fill='both', expand=True)

        self.right_panel = RightPanel(self.container)
        Navigate.setContainer(self.right_panel.main_content.container)

        Navigate.addPage(actived=False, key='rpl', kind='register', label="CADASTRAR PLAYLIST", component=registerplaylist.RegisterPlaylist(Navigate.container))
        Navigate.addPage(actived=False, key='rsg', kind='register', label="CADASTRAR FAIXA", component=registersong.RegisterSong(Navigate.container))
        Navigate.addPage(actived=False, key='rab', kind='register', label="CADASTRAR ÁLBUM", component=registeralbum.RegisterAlbum(Navigate.container))
        Navigate.addPage(actived=False, key='rrd', kind='register', label="CADASTRAR GRAVADORA", component=registerrecord.RegisterRecord(Navigate.container))
        Navigate.addPage(actived=False, key='rcp', kind='register', label="CADASTRAR COMPOSITOR", component=registercomposer.RegisterComposer(Navigate.container))
        Navigate.addPage(actived=False, key='rmp', kind='register', label="CADASTRAR PERÍODO MUSICAL", component=registerperiod.RegisterPeriod(Navigate.container))
        Navigate.addPage(actived=False, key='rit', kind='register', label="CADASTRAR INTÉRPRETE", component=registerinterpreter.RegisterInterpreter(Navigate.container))

        Navigate.addPage(actived=False, key='_sg', kind='single', label="FAIXA", component=song.Song(Navigate.container))
        Navigate.addPage(actived=False, key='_pl', kind='single', label="PLAYLIST", component=playlist.Playlist(Navigate.container))
        Navigate.addPage(actived=False, key='_ab', kind='single', label="ÁLBUM", component=album.Album(Navigate.container))

        Navigate.addPage(actived=False, key='sg', kind='list', label="FAIXAS", component=songs.Songs(Navigate.container))
        Navigate.addPage(actived=False, key='pl', kind='list', label="PLAYLISTS", component=playlists.Playlists(Navigate.container))
        Navigate.addPage(actived=False, key='ab', kind='list', label="ÁLBUNS", component=albums.Albums(Navigate.container))
        Navigate.addPage(actived=False, key='rd', kind='list', label="GRAVADORAS", component=records.Records(Navigate.container))
        Navigate.addPage(actived=False, key='cp', kind='list', label="COMPOSITORES", component=composers.Composers(Navigate.container))
        Navigate.addPage(actived=False, key='mp', kind='list', label="PERÍODOS MUSICAIS", component=periods.Periods(Navigate.container))
        Navigate.addPage(actived=False, key='it', kind='list', label="INTÉRPRETES", component=interpreters.Interpreters(Navigate.container))

        self.left_panel = LeftPanel(self.container)

        Navigate.goto('sg')
        Navigate.setApp(self)
    
    def exit(self):
        self.parent.destroy()   
