from tkinter import Tk,Canvas
from datetime import date,datetime

root = Tk
c = Canvas(root, width=500 ,height=500 bg= "grey")
c.pack()
c.create_text(100,50 ,anchor='w',fill="blue",font="courier 28 bold")

def grab_events():
    list_e = []

    with open("events.txt",'r')as ev:
        for line in ev:
            line = line.rstrip('\n')
            current = line.split(',')

            evn_date = datetime.strptime(current[1],"%d/%m/%Y")
            current[1] = evn_date

            list_e.append[current[1]]
        return list_e