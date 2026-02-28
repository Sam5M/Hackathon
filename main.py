from gui import Gui

try:
    gui = Gui()
except Exception as e:
    print(f"Error creating GUI: {e}")