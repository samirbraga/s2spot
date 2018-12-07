# -*- coding: utf-8 -*- 
import os
from db.dbcontroller import DBController
from components.component import Component
from components.menubutton import MenuButton
from components.navigate import Navigate
import Tkinter as tk
import tkMessageBox
from ttk import *

class Album(Component):
    def __init__(self, parent):
        super(Album, self).__init__(parent)
        self.container = Frame(parent, style="DarkGray.TFrame", width=500)
        self.content = Frame(self.container, style="DarkGray.TFrame", width=500)
        self.infos = []
        self.inputs = []
        self.submitinput = MenuButton(self.container, 'assets\\play-button.gif')
        self.submitinput.bind("<Button-1>", lambda _: self.submit())  

    def loadContent(self):
    	label_translater = ["NUMERO", "GRAVADORA", "PRECO", "DATA DE COMPRA", "DATA DE GRAVACAO", "TIPO DE COMPRA", "DESCRICAO"]

        self.content.pack_forget()

        for info in self.infos:
            info[0].pack_forget()

        self.infos = []

        if Navigate.current_data:
            for i, value in enumerate(Navigate.current_data):
                def _(value):
                    container = Frame(self.content, style="DarkGray.TFrame")
                    container.pack(fill='x')
                    text = Label(container, style="DarkGray.TLabel", text=label_translater[i])
                    text.pack(side='left', pady=20, padx=(0, 20))
                    input_ = Entry(container)
                    input_.pack(side='right')
                    input_.delete(0, 2000)
                    input_.insert(0, value)

                    self.infos.append([container, text, input_])
                _(value)

    def pack(self):
    	self.loadContent()

        self.container.pack(anchor='center', side='top')
        self.content.pack(anchor='center', side='top', padx=30, pady=30)
        self.submitinput.pack(anchor='center', side='bottom')

    def unpack(self):
        self.content.pack_forget()
        self.container.pack_forget()
        self.submitinput.unpack()

    def submit(self):
        new_values = [info[2].get() for i, info in enumerate(self.infos) if i > 1]

        try:
            DBController.execute('''
                UPDATE Album SET pr_compra=?, data_compra=?, data_grav=?, tipo_compra=?, descricao=?
                WHERE cod=%s
            ''' % (Navigate.current_data[0]),
                *new_values
            )
            DBController.commit()
        except Exception as e:
            tkMessageBox.showinfo("ERRO!", "Um erro aparenta ter ocorrido, por favor, tente novamente. Veja-o abaixo:\n %s." % e)
        else:
            Navigate.goto(Navigate.current_page['key'][1:])

