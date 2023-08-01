#create class from what has been built in secret_message.py
from tkinter import Tk,simpledialog,messagebox
class Secret_message:
    ROOT = Tk()
    ROOT.withdraw()
    def __init__(self):
        self.message = simpledialog.askstring('Message',"Enter the secret message: ")
        