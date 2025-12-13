from tkinter import*

# title
conver = Tk()
conver.title("Miles Converter")
conver.geometry("400x400")

# have a def for the button
def when_click():
    distan = entry_main.get()
    label.config({distan})

# label creation
label = Label(conver, text="")
label.grid(row = 1, column = 2)

# entry creation
# entry is not equal to the kilometers calculation
entry_main = Entry(conver)
entry_main.grid(row = 0, column = 2)

# calculation formula and rules
# formula: Distance in kilometers = Distance in miles × 1.609344
i = 1.609344
while entry_main == label:
    form =  en * i
    print(form)
else:
    print("Error")





# button commands
button = Button(conver, text = "calculate", command = when_click)

# connect the button (entries) to object
button.grid(row = 2, column = 2)

# label creation for other elements
miles = Label(conver,text = "Miles")
equal = Label(conver,text = "is equal to")
km = Label(conver,text = "Km")
press = Label(conver,text = "please press the button above to calculate!")

# label grid for position of the label
miles.grid(row = 0,column = 3)
equal.grid(row = 1,column = 1)
km.grid(row = 1,column = 3)
press.grid(row = 3, column = 2)

conver.mainloop()




