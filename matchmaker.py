from random import shuffle 
import time
from tkinter import Tk,Button,DISABLED

root =Tk()
root.title("Matchmaker")
root.resizable(width=False,height=False)

root.mainloop()
buttons = {}
first = True #check symbol is the first in math
previousX = 0 #track last button pressed
previousY = 0

button_symbol = {}

symbols = [u'\u2702', u'\u2702', u'\u2705', u'\u2705', u'\u2708', u'\u2708',
u'\u2709', u'\u2709', u'\u270A', u'\u270A', u'\u270B', u'\u270B',
u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712',
u'\u2714', u'\u2714', u'\u2716', u'\u2716', u'\u2728', u'\u2728']