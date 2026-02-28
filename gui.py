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
T = Text(Tk(), height=50, width=150)
T.insert(END, print(main.subprocess.getoutput(main.cmd)))
T.insert(END, print(main.json_data["response"], end="", flush=True))
root.mainloop()
