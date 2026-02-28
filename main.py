import subprocess
import tkinter
from tkinter import *
from tkinter import ttk
import requests
import json
# Source - https://stackoverflow.com/a/57439663
# Posted by Ronn Macc, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-28, License - CC BY-SA 4.0

#michael please enter your login info below in the variables
user = ""
host = "http://164.152.25.35:11434/api/"
cmd = "cd .."
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

# # Python 2
# subprocess.Popen("ssh {user}@{host} {cmd}".format(user=user, host=host, cmd='ls -l'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

# # Python 3
# subprocess.Popen(f"ssh {user}@{host} {cmd}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

T = Text(Tk(), height=50, width=150)

#print(subprocess.getoutput(cmd))
T.insert(END, print(subprocess.getoutput(cmd)))
question = input("Enter question: ")
response = requests.post(url=f"{host}generate", data=f'{{"model": "gemma3", "prompt": "{question}"}}', stream=True)

# print(response.status_code, response.reason)
# print(response.text)

for line in response.iter_lines():
    if line:
        json_data = json.loads(line)
        #print(json_data["response"], end="", flush=True)
        #aiResponse = (json_data["response"], end="", flush=True)
        T.insert(END, print(json_data["response"], end="", flush=True))
        mainloop()

# To chat: curl http://164.152.25.35:11434/api/generate -d '{"model": "gemma3", "prompt": "Why is the sky blue?"}'
