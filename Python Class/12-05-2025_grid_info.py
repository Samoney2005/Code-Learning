from tkinter import *

legend = Tk()
legend.title("Grid Information")
legend.geometry("400x150")

# label creation
label1 = Label(legend,text="Last Name")
label2 = Label(legend,text="First Name")
label3 = Label(legend,text="Age")
label4 = Label(legend,text="City")

# use grid here for each label
# note: if you use grid you cant use pad x ,y
label1.grid(row = 0,column = 0)
label2.grid(row = 1,column = 0)
label3.grid(row = 0,column = 3)
label4.grid(row = 1,column = 3)

# Entries here
entry1 = Entry(legend)
entry2 = Entry(legend)
entry3 = Entry(legend)
entry4 = Entry(legend)

# Note: The labels and the entries each have different coordinates
# They can have the same row but not the same column
# place the entries in the grid
entry1.grid(row = 0,column = 1)
entry2.grid(row = 1,column = 1)
entry3.grid(row = 0,column = 4)
entry4.grid(row = 1,column = 4)

# add a button
button = Button(legend, text = "click")

# connect the button to the object
button.grid(row = 2, column = 2)

legend.mainloop()