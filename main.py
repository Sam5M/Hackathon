import subprocess
import tkinter
from tkinter import *
from tkinter import ttk
# Source - https://stackoverflow.com/a/57439663
# Posted by Ronn Macc, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-28, License - CC BY-SA 4.0

#michael please enter your login info below in the variables
user = ""
host = ""
cmd = "cd.."
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

# Python 2
subprocess.Popen("ssh {user}@{host} {cmd}".format(user=user, host=host, cmd='ls -l'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

# Python 3
subprocess.Popen(f"ssh {user}@{host} {cmd}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

print(subprocess.getoutput(cmd))
