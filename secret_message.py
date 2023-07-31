from tkinter import Tk,messagebox,simpledialog

def get_task():
    return simpledialog.askstring('Task','Do you want to encrypt or decrypt ? ')

def get_message():
    return simpledialog.askstring('Message',"Enter the secret message: ")

root = Tk


def is_even(num):
    return num % 2 == 0  #True or false message will come

def get_even_ltters(message): #produces a list containing all the even-numbered letters.
    even_letters = []
    for counter in range(len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters
def get_odd_ltters(message): #produces a list containing all the even-numbered letters.
    odd_letters = []
    for counter in range(len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):  # sourcery skip: merge-list-appends-into-extend
    letter_list = []
    check_letter_list = []
    if not is_even(len(message)):
        message = f'{message}x'
    even_letters = get_even_ltters(message)
    odd_letters  = get_odd_ltters(message) 

    for counter in range(len(message) // 2):#: This calculates the integer division of the length of the message string by 2.
        letter_list.extend((odd_letters[counter], even_letters[counter]))
        check_letter_list.append(odd_letters[counter])
        check_letter_list.append(even_letters[counter])
    new_message =''.join(letter_list)
    return new_message

while True:
    task = get_task()

    if task == 'encrypt':
        message =get_message()
        encrypted = swap_letters(message)
        #messagebox.showinfo('Message to encrypt is : ',message)
        messagebox.showinfo('Ciphertext of the secret message is : ',encrypted)
    elif task == 'decrypt':
        message = get_message()
        decrypted = swap_letters(message)
        
        messagebox.showinfo('Plaintext of the secret message is: ',decrypted)
    else:
        break
root.mainloop()