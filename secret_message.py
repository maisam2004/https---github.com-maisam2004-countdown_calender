from tkinter import Tk,messagebox,simpledialog

def get_task():
    task = simpledialog.askstring('Task','Do you want to encrypt or decrypt ? ')
    return task