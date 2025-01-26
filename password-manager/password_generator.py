#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


nr_letters= random.randint(8,10)
nr_symbols = random.randint(2,4)
nr_numbers = random.randint(2,4)

passwordlist = []

for char in range(1, nr_letters + 1):
  randomchar = random.choice(letters)
  passwordlist.append(randomchar)

for sym in range(1, nr_symbols + 1):
  randomsym = random.choice(symbols)
  passwordlist.append(randomsym)

for num in range(1, nr_numbers + 1):
  randomnum = random.choice(numbers)
  passwordlist.append(randomnum)

random.shuffle(passwordlist)

password = ""
for char in passwordlist:
  password += char


#######_________________________________

website = website_entry.get()
try:
  with open("data.json") as data_file:
    data = json.load(data_file)
except FileNotFoundError:
  messagebox.showinfo(title="Error", message="No Data File Found.")
else:
  if website in data:
    email = data[website]["email"]
    password = data[website]["password"]
    messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
  else:
    messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
  
