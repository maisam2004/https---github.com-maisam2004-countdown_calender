#create class from what has been built in secret_message.py
from tkinter import Tk,simpledialog,messagebox
class Secret_message:
    ROOT = Tk()
    ROOT.withdraw()
    def __init__(self):
        self.message = simpledialog.askstring('Message',"Enter the secret message: ")
        self.task = simpledialog.askstring('Encrypt or Decrypt', 'Do you want to encrypt or decrypt?')

    def is_even(self,num):
        return num % 2 == 0

    def get_even_letters(self,message): #produces a list containing all the even-numbered letters.
        return [message[counter] for counter in range(len(message)) if is_even(counter)]

    def get_odd_letters(self,message): #produces a list containing all the even-numbered letters.
        return [message[counter] for counter in range(len(message)) if not is_even(counter)]    