# -*- coding: utf-8 -*- 
import os
import Tkinter as tk
from ttk import *
from components.app import App

if __name__ == '__main__':
    root = tk.Tk()
    root.title('S2spot')
    root.state('zoomed')
    app = App(root)
    
    style = Style()
    style.configure("Black.TButton", background="#0f0f0f", foreground="#000000", relief="flat")
    style.configure("Black.TFrame", background="#000000")
    style.configure("DarkGray.TFrame", background="#333333")
    style.configure("DarkGray.TLabel", background="#333333", foreground="#cccccc")
    style.configure("Gray.TFrame", background="#282828")
    style.configure("LightGray.TFrame", background="#111111")
    style.configure("Option.TFrame", background="#000000", foreground="#f1f2f3")
    style.configure("Separator.TFrame", background="#282828")
    style.configure("SeparatorGray.TFrame", background="#444444")
    style.configure("HeaderGray.TLabel", background="#282828", foreground="#666666", font=('Helvetica', 17))
    style.configure("HeaderLightGray.TLabel", background="#333333", foreground="#666666", font=('Helvetica', 10, 'bold'))
    root.mainloop()