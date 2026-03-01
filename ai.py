
import requests
import json


def __init__(self):
    self.responses = []
    self.user = ""
    self.host = "http://164.152.25.35:11434/api/"
    self.cmd = "cd .."

    # To chat: curl http://164.152.25.35:11434/api/generate -d '{"model": "gemma3", "prompt": "Why is the sky blue?"}'
    response = requests.post(url=f"{self.host}generate", data='{"model": "gemma3", "prompt": "Reply with Hello! to this message"}', stream=True)

    for line in response.iter_lines():
        if line:
            json_data = json.loads(line)
            print(json_data["response"], end="")
            self.responses.append(json_data["response"])


#getters and settters
def getResponses(self):
    return self.responses

def setResponses(self, responses):
    self.responses = responses