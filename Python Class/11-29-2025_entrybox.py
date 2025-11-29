from tkinter import *

root = Tk()

# associate it with a function in our case geometry
root.geometry("300x300")


# add a label name
s = Label(root, text = "Enter Your Name: ", font = ("Times New Roman", 20), fg="red", bg="blue")

# connect label with object
s.pack()

# insert the entry
box = Entry(root)

# space between all different things
box.pack(pady=20)

# add a button
button = Button(root, text = "Click")

# connect the button to the object
button.pack(pady = 50)

# keeps the window open
root.mainloop()