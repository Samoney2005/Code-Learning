from tkinter import*
root = Tk()
# We need 9 squares in a window
root.title("Tic Tac Toe")
root.geometry("300x300")
root['padx'] = 50 # Horizontal padding
root['pady'] = 20 # Vertical padding
"""
button1 = Button(root, text="Submit")
button1.grid(row=0, column=0)
button2 = Button(root, text="Submit")
button2.grid(row=0, column=1)
button3 = Button(root, text="Submit")
button3.grid(row=0, column=2)


button4.grid(row=1, column=0)
button5 = Button(root, text="Submit")
button5.grid(row=1, column=1)
button6 = Button(root, text="Submit")
button6.grid(row=1, column=2)
"""

for rowi in range(3):
    for colj in range(3):
        # add a button
        button = Button(root, text="Submit")
        # grid
        button.grid(row = rowi, column = colj)
        print(f"The value of the column is {colj}")
        print(f"The value of the row is {rowi}")

root.mainloop()

