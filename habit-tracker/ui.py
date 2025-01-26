#-------------------------------------------------------UI------------------------------------------------
window = Tk()
window.title("Habit Tracker")
window.config(padx = 50, pady = 50, bg = "white")

canvas = Canvas(width = 540, height = 352, bg = "white", highlightthickness=0)
icon_img = PhotoImage(file = "icon.png")
canvas.create_image(280, 176, image = icon_img)
canvas.grid(column = 1, row = 0, columnspan = 2)

create_account = Label(text = "Create an Account", bg = "white", font = ("Ariel", 20, "italic"))
create_account.grid(column = 0, row = 1)

username_label = Label(text = "Enter Username: ", bg = "white", font = ("Ariel", 15, "normal"))
username_label.grid(column = 0, row = 2)
username_entry = Entry(width = 30)
username_entry.grid(column = 1, row = 2, pady = 20)
USERNAME = username_entry.get()

token_label = Label(text = "Enter Password: ", bg = "white", font = ("Ariel", 15, "normal"))
token_label.grid(column = 2, row = 2)
token_entry = Entry(width = 30)
token_entry.grid(column = 3, row = 2)
TOKEN = token_entry.get()

error_label = Label(text = user_error, font = ("Ariel", 15, "normal"))


url_label = Label( text = f"Click the link to view your Graph!\n https://pixe.la/v1/users/aslesha/graphs/graph1.html", font = ("Ariel", 20, "italic"), bg = "white")
url_label.grid(column = 1, row =4, columnspan = 3)

window.mainloop()
