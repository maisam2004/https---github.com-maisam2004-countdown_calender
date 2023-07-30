from tkinter import Tk,Canvas
from datetime import date,datetime

root = Tk()
c = Canvas(root, width=500 ,height=500, bg= "grey")
c.pack()
c.create_text(100,50 ,anchor='w',fill="blue",font="courier 28 bold",text="Count down events")

def grab_events():
    list_e = []

    with open("events.txt",'r')as ev:
        for line in ev:
            line = line.rstrip('\n')
            current = line.split(',')

            evn_date = datetime.strptime(current[1],"%d/%m/%Y").date()
            current[1] = evn_date

            list_e.append(current)
    return list_e
#to calculate date how many days 

def subtract_dates(d1,d2):
    between = str(d1-d2)
    days_number  = between.split(' ')
    return days_number[0]

this_day = date.today()
events = grab_events()
events.sort(key=lambda f : f[0])
hor = 100
ver = 100
for i,e in enumerate(events) :
    ev_name = e[0]
    until = subtract_dates(e[1],this_day)
    display = f"it is {until} days to {ev_name}"
    c.create_text(hor,ver ,anchor="w",fill = 'black' ,\
                  font= "Arial 24 bold",text=display)
    ver = ver + (40 + i)

root.mainloop()