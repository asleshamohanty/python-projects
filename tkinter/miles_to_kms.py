from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width = 300, height = 50)
window.config(padx = 20, pady = 20)
FONT = ("Times New Roman", 12, "normal")

miles_entry = Entry(width = 10)
#miles_entry.config(padx = 5, pady = 5)
miles_entry.grid(column = 0, row = 1)



def convert():
    miles = int(miles_entry.get())
    kms = round((miles * 1.609), 2)
    kms_ans = Label(text=kms, font=FONT)
    kms_ans.grid(column=2, row=1)


label_equal = Label(text="is equal to", font=FONT)
label_equal.grid(column = 1, row = 1)

label_equal = Label(text="kms", font=FONT)
label_equal.grid(column = 3, row = 1)
Button = Button(text = "Convert to kilometres", command = convert, width = 19, font=FONT).grid(column = 1, row = 2)

window.mainloop()