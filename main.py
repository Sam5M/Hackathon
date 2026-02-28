from gui import Gui
from ai import AI

try:
    ai = AI()
    ai.sendMessage(input("Enter question: "))
except Exception as e:
    print(f"Nope :P", {e})

try:
    gui = Gui()
except Exception as e:
    print(f"Error creating GUI: {e}")
