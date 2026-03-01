from tkinter import *
from tkinter import ttk
import main

class gui:
    def __init__(self):
        #member variables = self...
        self.responses = []
        self.root = Tk()

        self.root.geometry("800x600")

        frm = ttk.Frame(self.root, padding=10)
        ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
        ttk.Button(frm, text="Quit", command=self.root.destroy).grid(column=1, row=0)

        self.root.mainloop()

    #response = list
    def addResponse(self, response):
        self.responses.append(response)