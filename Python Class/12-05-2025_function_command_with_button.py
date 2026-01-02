from tkinter import *


#window creation
desoto = Tk()
desoto.title("Entry function")

def show_name():
    name = entry1.get()
    label.config(text=f"Hi, {name}")

#entry creation
entry1 = Entry(desoto)
entry1.pack(pady=10)

#add button
button = Button(desoto, text="Submit", command = show_name)
#button = Button(desoto, text="Submit")
button.pack()

#label
label = Label(desoto, text="")
label.pack(pady=10)


#main window loop
desoto.mainloop()
