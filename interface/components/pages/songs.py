# -*- coding: utf-8 -*- 
import os
import Tkinter as tk
from ttk import *
from db.dbcontroller import DBController
from datetime import datetime, timedelta
from components.navigate import Navigate
from components.listitem import ListItem
from components.menubutton import MenuButton
from components.component import Component
from components.scrollableframe import ScrollableFrame
from components.menubutton import MenuButton

class Songs(Component):
    def __init__(self, parent):
        super(Songs, self).__init__(parent)
        self.container = ScrollableFrame(parent, style="DarkGray.TFrame")

        self.songsItems = []
        self.songsList = Frame(self.container.interior, style="DarkGray.TFrame")
        self.songsList.pack(fill='x')

        ListItem(self.songsList, ['Número', 'Descrição', 'Composição', 'Duração', 'Tipo'], None, True)

    def loadContent(self):
        DBController.execute('SELECT * FROM professor');
        for row in DBController.get():
            print("row= %r" % (row,))

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
            def _(song):
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

                self.songsItems.append(
                    ListItem(self.songsList, titles, gotoSong))

            _(song)

        self.container.pack(expand=True, fill='both')   
