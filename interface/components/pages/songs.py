# -*- coding: utf-8 -*- 
import os
import Tkinter as tk
from ttk import *
from datetime import datetime, timedelta
from components.navigate import Navigate
from components.menubutton import MenuButton
from components.component import Component
from components.scrollableframe import ScrollableFrame
from components.menubutton import MenuButton

class SongItem(Component):
    def __init__(self, parent, titles, cb, isHeader=False):
        super(SongItem, self).__init__(parent)
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

class Songs(Component):
    def __init__(self, parent):
        super(Songs, self).__init__(parent)
        self.container = ScrollableFrame(parent, style="DarkGray.TFrame")

        self.songsItems = []
        self.songsList = Frame(self.container.interior, style="DarkGray.TFrame")
        self.songsList.pack(fill='x')

        SongItem(self.songsList, ['Número', 'Descrição', 'Composição', 'Duração', 'Tipo'], None, True)

    def loadContent(self):
        self.songsData = [{
            'number': 0,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Algo Laudo',
            'time': 240000,
            'record_type': 'ADD'
        }, {
            'number': 1,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Lorem LORD',
            'time': 310000,
            'record_type': 'DDD'
        }, {
            'number': 2,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Lord Huron',
            'time': 200000,
            'record_type': 'DDD'
        }, {
            'number': 3,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Kinds Leon',
            'time': 320000,
            'record_type': 'ADD'
        }, {
            'number': 1,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Lorem LORD',
            'time': 310000,
            'record_type': 'DDD'
        }, {
            'number': 2,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Lord Huron',
            'time': 200000,
            'record_type': 'DDD'
        }, {
            'number': 3,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Kinds Leon',
            'time': 320000,
            'record_type': 'ADD'
        }, {
            'number': 1,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Lorem LORD',
            'time': 310000,
            'record_type': 'DDD'
        }, {
            'number': 2,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Lord Huron',
            'time': 200000,
            'record_type': 'DDD'
        }, {
            'number': 3,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Kinds Leon',
            'time': 320000,
            'record_type': 'ADD'
        }, {
            'number': 1,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Lorem LORD',
            'time': 310000,
            'record_type': 'DDD'
        }, {
            'number': 2,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Lord Huron',
            'time': 200000,
            'record_type': 'DDD'
        }, {
            'number': 3,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Kinds Leon',
            'time': 320000,
            'record_type': 'ADD'
        }, {
            'number': 1,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Lorem LORD',
            'time': 310000,
            'record_type': 'DDD'
        }, {
            'number': 2,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Lord Huron',
            'time': 200000,
            'record_type': 'DDD'
        }, {
            'number': 3,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Kinds Leon',
            'time': 320000,
            'record_type': 'ADD'
        }, {
            'number': 1,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Lorem LORD',
            'time': 310000,
            'record_type': 'DDD'
        }, {
            'number': 2,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Lord Huron',
            'time': 200000,
            'record_type': 'DDD'
        }, {
            'number': 3,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Kinds Leon',
            'time': 320000,
            'record_type': 'ADD'
        }, {
            'number': 1,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Lorem LORD',
            'time': 310000,
            'record_type': 'DDD'
        }, {
            'number': 2,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Lord Huron',
            'time': 200000,
            'record_type': 'DDD'
        }, {
            'number': 3,
            'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officiis quidem voluptatibus delectus obcaecati, nobis et eligendi? Facilis sed enim eos vero itaque aut delectus, nostrum iste esse aspernatur. Unde, odio!',
            'composition': 'Kinds Leon',
            'time': 320000,
            'record_type': 'ADD'
        }]

    def pack(self):
        for song in self.songsItems:
            song.unpack()

        self.songsItems = []

        self.loadContent()

        for song in self.songsData:
            sec = timedelta(seconds=song['time']/1000)
            dt = datetime(1, 1, 1) + sec
            titles = [
                song['number'],
                " ".join(song['description'].split(' ')[0:5]) + '...',
                song['composition'],
                "%02d:%02d:%02d" % (dt.hour, dt.minute, dt.second),
                song['record_type']
            ]

            def gotoSong(_):
                Navigate.goto('_sg', song)

            self.songsItems.append(SongItem(self.songsList, titles, gotoSong))

        self.container.pack(expand=True, fill='both')   