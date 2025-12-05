from tkinter import *

master = Tk()

master.title("Grid Tkinter")
master.geometry("150x150")

#label  creation
label1 = Label(master, text="First Name")
label2 = Label(master, text="Last Name")

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

#entry creation
entry1 = Entry(master)
entry2 = Entry(master)

#place entries with grid function
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)



master.mainloop()
