from tkinter import *
from tkinter import ttk
from ai import AI

class Gui:
    def __init__(self):
        #member variables = self...
        self.responses = []
        self.root = Tk()
        self.root.iconbitmap("icon.ico")
        self.root.title("xXSuper_Ai_PlayzXx")
        self.root.geometry("600x600")

        frm = ttk.Frame(self.root, padding=10)
        ttk.Label(frm, text="Welcome to our program! Made by Ethan, Sam, Emma, and Michael").grid(column=0, row=0)
        ttk.Button(frm, text="Quit", command=self.root.destroy).grid(column=1, row=0)
        frm.grid()
        self.responselabel = ttk.Label(frm, text="", wraplength=self.root.winfo_width())
        self.responselabel.grid(column=0,row=1)
        self.quitbutton =  ttk.Button(frm, text="Quit", command=self.root.destroy)
        self.quitbutton.grid(column=0, row=2)


        self.lblinput = ttk.Label(frm, text="Ask the AI a question below")
        self.lblinput.grid(column=1, row=0)
        self.entry = ttk.Entry(frm)
        self.entry.grid(column=1, row = 1)
        self.submit = ttk.Button(frm, text="Submit", command=self.submitEntry)
        self.submit.grid(column=1, row=2)

        self.ai = AI(gui=self)
        self.root.mainloop()

    #response = list
    def addResponse(self, response):
        self.responses.append(response)

    def submitEntry(self):
        self.entry.delete(0, END)
        self.ai.sendMessage("Whenever you speak pretend to be a gen a tiktok doom scrolling gamer and only address me as chud. You need to add plenty of slang and emojis: " + self.entry.get())
