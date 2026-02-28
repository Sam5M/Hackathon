import subprocess
import requests
# Source - https://stackoverflow.com/a/57439663
# Posted by Ronn Macc, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-28, License - CC BY-SA 4.0

#michael please enter your login info below in the variables
user = ""
host = "http://164.152.25.35:11434/api/"
cmd = "cd .."

# # Python 2
# subprocess.Popen("ssh {user}@{host} {cmd}".format(user=user, host=host, cmd='ls -l'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

# # Python 3
# subprocess.Popen(f"ssh {user}@{host} {cmd}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

print(subprocess.getoutput(cmd))
response = requests.post(url=f"{host}generate", data='{"model": "gemma3", "prompt": "Why is the sky blue"}', stream=True)

# print(response.status_code, response.reason)
# print(response.text)

for line in response.iter_lines():
    if line:
        print(line)

# To chat: curl http://164.152.25.35:11434/api/generate -d '{"model": "gemma3", "prompt": "Why is the sky blue?"}'
