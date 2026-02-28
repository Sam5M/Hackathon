
import requests
import json
import threading

class AI:
    def __init__(self, gui):
        self.host = "http://164.152.25.35:11434/api/"
        self.chat_mem = ""
        self.responses = ""
        self.gui = gui

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

    # input("Enter question: ")
    def sendMessage(self, message: str):


        question = f'{{"role": "user", "content": "{message.replace("\n", "\\n")}"}}'
        print('Request:', f'{{"model": "gemma3", "messages": [{self.chat_mem} {question}]}}')
        response = requests.post(url=f"{self.host}chat", data=f'{{"model": "gemma3", "messages": [{self.chat_mem}{question}]}}', stream=True)

        print(response.status_code, response.reason)
        # print(response.text)
        system_response = ""
        for line in response.iter_lines():
            if line:
                # print(line)
                json_data = json.loads(line)
                print(json_data["message"]["content"], end="", flush=True)
                self.responses += json_data["message"]["content"]
                system_response += json_data["message"]["content"]
        self.chat_mem += f'{question}, {{"role": "system", "content": "{system_response.replace("\n", "\\n")}"}},'
        print("Chat Mem:", self.chat_mem)
