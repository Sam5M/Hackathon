
import requests
import json

class AI:
    def __init__(self):
        self.host = "http://164.152.25.35:11434/api/"
        self.chat_mem = ""
        self.responses = ""

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
