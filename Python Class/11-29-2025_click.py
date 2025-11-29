from tkinter import *

root = Tk()

# associate it with a function in our case geometry
root.geometry("100x100")

# add a label name
s = Label(root, text = "How are you! ", font = ("Times New Roman", 20))

# add a button
button = Button(root, text = "Click")

# connect label with object
s.pack()

# connect the button to the object
button.pack(pady = 50)

# keeps the window open
root.mainloop()