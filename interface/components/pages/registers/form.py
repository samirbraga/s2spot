# -*- coding: utf-8 -*- 
import os
from db.dbcontroller import DBController
from components.navigate import Navigate
from components.component import Component
from components.menubutton import MenuButton
import Tkinter as tk
import tkMessageBox
from ttk import *

class TextInput(Component):
    def __init__(self, parent, entry):
        super(TextInput, self).__init__(parent)
        self.container = Frame(parent, style="DarkGray.TFrame")
        self.container.pack(fill='x')
        self.entry = entry
        self.attr = entry['attr']

        if entry['type'] in ['text', 'int']:
            self.input = Entry(self.container)
        elif entry['type'] == 'select':
            option = tk.StringVar(self.container)
            DBController.execute('''
                SELECT %s, %s FROM %s
            ''' % (entry['target_label'], entry['target_key'], entry['target']))

            results = [("%d- %s" % (i, result[0]), result[1]) for i, result in enumerate(DBController.get())]
            choices = set([result[0] for result in results])
            self.results = results
            if results:
                option.set(results[0])
            self.input = OptionMenu(self.container, option, *choices)
            self.options = option

    def pack(self):
        if self.entry['type'] == 'select':
            DBController.execute('''
                SELECT %s, %s FROM %s
            ''' % (self.entry['target_label'], self.entry['target_key'], self.entry['target']))
            results = [("%d- %s" % (i, result[0]), result[1]) for i, result in enumerate(DBController.get())]
            self.results = results
            menu = self.input["menu"]
            menu.delete(0, "end")
            for string in self.results:
                menu.add_command(label=string, 
                                command=lambda value=string: self.options.set(value[0]))

        self.container.pack(fill='x', side='right')
        self.input.pack(side='right')

    def value(self):
        if self.entry['type'] == 'select':
            return self.options.get()
        else:
            return self.input.get()

class FormGroup(Component):
    def __init__(self, parent, entry):
        super(FormGroup, self).__init__(parent)
        self.container = Frame(parent, style="DarkGray.TFrame")
        self.label = Label(self.container, style='DarkGray.TLabel', text=entry['label'])
        self.input = TextInput(self.container, entry)

        self.entry = entry
        self.container.pack(fill='x', padx=(10, 20), pady=(0, 14))
        self.label.pack(side='left', expand=True, padx=(5, 20))
        self.input.pack()

class Form(Component):
    def __init__(self, parent, table, entries, cod_generator):
        super(Form, self).__init__(parent)
        self.container = Frame(parent, style="DarkGray.TFrame", width=500)
        self.submitinput = MenuButton(self.container, 'assets\\play-button.gif')
        self.submitinput.bind('<Button-1>', self.submit)

        self.groups=[]
        self.entries = entries
        self.table = table
        self.codgenerator = cod_generator
        
        self.pack()

    def pack(self):
        self.unpack()
        for entry in self.entries:
            self.groups.append(FormGroup(self.container, entry))

        self.container.pack(anchor='center', side='top', pady=(10, 20))

        self.submitinput.pack()

    def unpack(self):
        for group in self.groups:
            group.pack_forget()

        self.submitinput.unpack()
        self.groups=[]

    def submit(self, _):
        columns = ['cod'] + [entry['attr'] for entry in self.entries]
        values_entries = ['?' for _ in range(len(self.entries) + 1)]
        values = [self.codgenerator()] 
        for group in self.groups:
            if group.entry['type'] == 'select':
                index = int(group.input.value().split("-")[0])
                values.append(int(group.input.results[index][1]))
            else:
                values.append(float(group.input.value()) if group.entry['type'] == 'int' else group.input.value())

        try:
            DBController.execute('''
                INSERT INTO %s (%s) VALUES (%s)
            ''' % (self.table, ", ".join(columns), ", ".join(values_entries)), 
                *values
            )
            DBController.commit()
        except Exception as e:
            tkMessageBox.showinfo("ERRO!", "Um erro aparenta ter ocorrido, por favor, tente novamente. Veja-o abaixo:\n %s." % e)
        else:
            Navigate.goto(Navigate.current_page['key'][1:])
