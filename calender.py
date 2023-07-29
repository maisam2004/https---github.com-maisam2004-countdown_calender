from tkinter import Tk,Canvas
from datetime import date,datetime


root = Tk()
c = Canvas(root,width=800,height=800,bg='gray')
c.pack()

c.create_text(100,50,anchor='w',fill='blue', font='Arial 28 bold underline' ,text="My Countdown Calendar")

def get_events():
    list_events = []
    name_events = []
    with open('events.txt','r') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            
            event_date = datetime.strptime(current_event[1], "%d/%m/%Y").date()
            current_event[1] = event_date
            
            list_events.append(current_event)
            #name_events.append(current_event[0])
    return list_events

def days_between_dates(date1,date2):
    time_between = str(date1-date2)
    number_of_days = time_between.split(' ')
    return number_of_days[0]

events = get_events()
events.sort(key=lambda x:x[1]) #Sort the list in order of days to go and not by the name of the events
today  = date.today()
vertical_space = 100
horzintal = 100
colors_events = ['white','black','blue','purple','orange']
for i,event in enumerate(events):
    event_name = event[0]
    
    days_until = days_between_dates(event[1],today)
    display = f"It is {days_until} days until {event_name}"
    color_index = i%len(colors_events)

    c.create_text(horzintal,vertical_space,anchor='w',fill=colors_events[color_index], \
                  font='Arial 26 bold' ,text=display)
    vertical_space = vertical_space + 40
    horzintal=horzintal + 10
root.mainloop()
