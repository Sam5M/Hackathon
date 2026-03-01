import subprocess
import requests
import json
from gui import gui

user = ""
host = "http://164.152.25.35:11434/api/"
cmd = "cd .."

print(subprocess.getoutput(cmd))
response = requests.post(url=f"{host}generate", data='{"model": "gemma3", "prompt": "Why is the sky blue"}', stream=True)

# print(response.status_code, response.reason)
# print(response.text)


for line in response.iter_lines():
    if line:
        json_data = json.loads(line)
        print(json_data["response"], end="")

gui = gui()

# To chat: curl http://164.152.25.35:11434/api/generate -d '{"model": "gemma3", "prompt": "Why is the sky blue?"}'
