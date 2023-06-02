from tkinter import *
from tkinter.ttk import *
from screeninfo import get_monitors

class gui:
    def __init__(self):
        self.root = Tk()
        self.root.geometry(str(self.root.winfo_screenwidth())+"x"+str(self.root.winfo_screenheight()))
