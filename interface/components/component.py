# -*- coding: utf-8 -*- 

class Component(object):
    def __init__(self, parent):
        self.parent = parent
    
    def unpack(self):
        self.container.pack_forget()