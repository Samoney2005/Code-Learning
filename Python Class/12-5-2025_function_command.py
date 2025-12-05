from tkinter import *

sam = Tk()
sam.title("functon button")


def on_click():
    label.config(text="Button clicked")



label = Label(sam, text="Click button below")
label.pack(pady=30)

#button
button = Button(sam, text="Click", command= on_click)

button.pack(pady=40)

sam.mainloop()
