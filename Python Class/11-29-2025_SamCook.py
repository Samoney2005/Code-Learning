from tkinter import *

root = Tk()

# associate it with a function in our case geometry
root.geometry("300x300")

# add a label for last name
s = Label(root, text = "Enter Your Last Name: ", font = ("Times New Roman", 20), fg="green", bg="orange")

# connect label with object
s.pack()

# insert the entry box
box1 = Entry(root)

# space between all different things
box1.pack(pady=20)

# add a label for middle name
a = Label(root, text = "Enter Your Middle Name: ", font = ("Times New Roman", 20), fg="purple", bg="pink")

# connect label with object
a.pack()

# insert the entry box
box2 = Entry(root)

# space between all different things
box2.pack(pady=20)

# add a label for first name
c = Label(root, text = " Enter your First Name: ", font = ("Times New Roman", 20), fg="red", bg="blue")

# connect label with object
c.pack()

# insert the entry box
box3 = Entry(root)

# space between all different things
box3.pack(pady=20)

# add a button
button = Button(root, text = "Start")

# connect the button to the object
button.pack()

# keeps the window open
root.mainloop()