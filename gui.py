from tkinter import *
from tkinter import ttk
from ai import AI

class Gui:
    def __init__(self):
        #member variables = self...
        self.responses = []
        self.root = Tk()
        
        self.root.geometry("600x600")

        frm = ttk.Frame(self.root, padding=10)
        ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
        ttk.Button(frm, text="Quit", command=self.root.destroy).grid(column=1, row=0)
        ai = AI()
        self.count = 0
        self.responses = ai.getResponses()
        for i in self.responses:
            self.count += 1
            ttk.Label(frm, text=i).grid(column=0, row=self.count)

        self.root.mainloop()

    #response = list
    def addResponse(self, response):
        self.responses.append(response)
