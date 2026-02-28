from tkinter import *
from tkinter import ttk
from turtle import color
from ai import AI

class Gui:
    def __init__(self):
        #member variables = self...
        self.responses = []
        self.root = Tk()
        self.root.config(background="#c071b3")
        self.root.iconbitmap("icon.ico")
        self.root.title("xXSuper_Ai_PlayzXx")
        self.root.geometry("600x600")

        # frm = ttk.Frame(self.root, padding=10)
        ttk.Label(self.root, text="Welcome to our program! Made by Ethan, Sam, Emma, and Michael").pack(fill="x")
        self.responselabel = ttk.Label(self.root, text="", wraplength=self.root.winfo_width())
        self.responselabel.pack(fill="both")
        self.responselabel.config(background="#c071b3", font=("Arial", 16, "bold"), padding=20)

        frame = ttk.Frame(self.root)
        frame.pack(fill="x", side="bottom", expand=False)

        self.lblinput = ttk.Label(frame, text="Ask the AI a question below")
        self.lblinput.pack(fill="x")
        self.entry = ttk.Entry(frame)
        self.entry.pack(fill="x")
        self.submit = ttk.Button(frame, text="Submit", command=self.submitEntry)
        self.submit.pack(fill="x")
        self.quitbutton =  ttk.Button(frame, text="Quit", command=self.root.destroy)
        self.quitbutton.pack(fill="x")

        self.ai = AI(gui=self)
        self.root.mainloop()

    #response = list
    def addResponse(self, response):
        self.responses.append(response)

    def submitEntry(self):
        self.ai.sendMessage(self.entry.get())

        self.entry.delete(0, END)
        self.ai.sendMessage("Whenever you speak pretend to be a gen a tiktok doom scrolling gamer and only address me as chud. You need to add plenty of slang and emojis: " + self.entry.get())
