from tkinter import*
root = Tk()
# We need 9 squares in a window
root.title("Tic Tac Toe")
root.geometry("300x300")
root['padx'] = 50 # Horizontal padding
root['pady'] = 20 # Vertical padding

for _ in range(3):
    # add a button
    button = Button(root, text="Submit")
    # Pady
    button.pack(pady=5)


root.mainloop()

