
import requests
import json
import threading

class AI:
    def __init__(self, gui):
        self.gui = gui
        self.user = ""
        self.host = "http://164.152.25.35:11434/api/"
        self.cmd = "cd .."

        threading.Thread(target=self.run_ai, daemon=True).start()


    def run_ai(self):
        # To chat: curl http://164.152.25.35:11434/api/generate -d '{"model": "gemma3", "prompt": "Why is the sky blue?"}'
        response = requests.post(url=f"{self.host}generate", data='{"model": "gemma3", "prompt": "What is your name?"}', stream=True)

        res = ""
        for line in response.iter_lines():
            if line:
                json_data = json.loads(line)
                print(json_data["response"], end="", flush=True)
                res+=json_data["response"]
                #self.gui.responselabel.text=res
                self.gui.responselabel.config(text=res)
                self.gui.root.update()
                #self.root.after(0, lambda: self.gui.responselabel.config(text=res))

    #getters and settters
    def getResponses(self):
        return self.responses

    def setResponses(self, responses):
        self.responses = responses