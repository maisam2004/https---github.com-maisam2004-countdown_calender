from tkinter import Tk,messagebox,simpledialog

def get_task():
    while True:#validate entered input
        task = simpledialog.askstring('Encrypt or Decrypt', 'Do you want to encrypt or decrypt?')
        
        if task or task.lower() in ['encrypt', 'decrypt']:
            return task.lower()
        messagebox.showerror('Invalid Input', 'Please enter "encrypt" or "decrypt".')

def get_message():
    return simpledialog.askstring('Message',"Enter the secret message: ")

root = Tk()
root.withdraw()


def is_even(num):
    return num % 2 == 0  #True or false message will come

def get_even_letters(message): #produces a list containing all the even-numbered letters.
    return [message[counter] for counter in range(len(message)) if is_even(counter)]

def get_odd_letters(message): #produces a list containing all the even-numbered letters.
    return [message[counter] for counter in range(len(message)) if not is_even(counter)]


def swap_letters(message):  # sourcery skip: merge-list-appends-into-extend
    letter_list = []

    if not is_even(len(message)):
        message = f'{message}x'
    even_letters = get_even_letters(message)
    odd_letters  = get_odd_letters(message) 

    for counter in range(len(message) // 2):#: This calculates the integer division of the length of the message string by 2.
        letter_list.extend((odd_letters[counter], even_letters[counter]))

    return ''.join(letter_list)

while True:
    task = get_task()

    if task == 'encrypt':
        message =get_message()
        encrypted = swap_letters(message)
        
        messagebox.showinfo('Ciphertext of the secret message is : ',encrypted)
    elif task == 'decrypt':
        message = get_message()
        decrypted = swap_letters(message)
        
        messagebox.showinfo('Plaintext of the secret message is: ',decrypted)
    else:
        break
root.mainloop()