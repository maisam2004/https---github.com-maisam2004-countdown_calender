from tkinter import Tk,messagebox,simpledialog

def get_task():
    return simpledialog.askstring('Task','Do you want to encrypt or decrypt ? ')

def get_message():
    return simpledialog.askstring('Message',"Enter the secret message: ")

root = Tk


def is_even(num)
    return num % 2 == 0  #True or false message will come

def get_even_ltters(message): #produces a list containing all the even-numbered letters.
    even_letters = []
    for counter in range(len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

while True:
    task = get_task()

    if task == 'encrypt':
        message =get_message()
        messagebox.showinfo('Message to encrypt is : ',message)
    elif task == 'decrypt':
        message = get_message()
        messagebox.showinfo('Message to decrypt is :',message)
    else:
        break
root.mainloop()