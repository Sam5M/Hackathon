from tkinter import *
from tkinter import ttk
import main
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
mn = main()
ttk.Frame
#T = Text(Tk(), height=50, width=150)
#T.insert(END, print(main.subprocess.getoutput(main.cmd)))
#T.insert(END, print(main.json_data["response"], end="", flush=True))
root.mainloop()
from AI import AI

class Gui:
    def __init__(self):
        #member variables = self...
        self.responses = []
        self.root = Tk()
        
        self.root.geometry("600x600")

        frm = ttk.Frame(self.root, padding=10)
        ttk.Label(frm, text="Welcome to our program! Made by Ethan, Sam, Emma, and Michael").grid(column=0, row=0)
        ttk.Button(frm, text="Quit", command=self.root.destroy).grid(column=1, row=0)
        ai = AI()
        self.count = 0
        self.responses = ai.getResponses()
        for i in self.responses:
            self.count += 1
            ttk.Label(frm, text=i).grid(column=0, row=self.count)

            T = Text(Tk(), height=50, width=150)
            T.insert(END, print(main.subprocess.getoutput(main.cmd)))
            T.insert(END, print(main.json_data["response"], end="", flush=True))

        self.root.mainloop()

    #response = list
    def addResponse(self, response):
        self.responses.append(response)
