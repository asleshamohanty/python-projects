from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height = 300)
window.config(padx = 20, pady = 20)

my_label = Label(text="My First Label", font=("Times New Roman", 15, "bold"))
my_label.grid(column = 0, row = 0)
my_label.config(padx = 20, pady = 20)

#my_label["text"] = "New Text"
#label.config(text = "New Text Again")

input = Entry(width = 10)
input.grid(column = 2, row = 0)

def button_clicked():
    x = (input.get())
    my_label.config(text= x)
    my_label.grid(column = 0, row = 0)

button = Button(text = "Click Me", command = button_clicked).grid(column = 2, row = 1)

#Entry










window.mainloop() #has to be at the end