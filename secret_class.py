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
        return [message[counter] for counter in range(len(message)) if self.is_even(counter)]

    def get_odd_letters(self,message): #produces a list containing all the even-numbered letters.
        return [message[counter] for counter in range(len(message)) if not self.is_even(counter)] 

    def swap_letters(self,message):  # sourcery skip: merge-list-appends-into-extend
        letter_list = []

        if not self.is_even(len(message)):
            message = f'{message}x'
        even_letters = self.get_even_letters(message)
        odd_letters  = self.get_odd_letters(message) 

        for counter in range(len(message) // 2):#: This calculates the integer division of the length of the message string by 2.
            letter_list.extend((odd_letters[counter], even_letters[counter]))

        return ''.join(letter_list)
    
    def get_message():
        return simpledialog.askstring('Message',"Enter the secret message: ")


    def output(self):
        task = simpledialog.askstring('Encrypt or Decrypt', 'Do you want to encrypt or decrypt?')
        message = self.get_message
        
        if task =='encrypt':
            #message = simpledialog.askstring('Message',"Enter the secret message: ")
            
            encrypted = self.swap_letters(message)
            messagebox.showinfo('Ciphertext of the secret message is : ',encrypted)
        elif task == "Decrypt":
            #message = simpledialog.askstring('Message',"Enter the secret message: ")
            
            decrypted = self.swap_letters(message)
            messagebox.showinfo('Plaintext of the secret message is: ',decrypted)

    ROOT.mainloop()

