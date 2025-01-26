with open("./Input/Names/invited_names.txt", "r") as file_invitednames:
    invited_names = file_invitednames.readlines()
    print(invited_names)

with open("./Input/Letters/starting_letter.txt", "r") as file_letter:
    letter = file_letter.read()

for name in invited_names:
    formatted_name = name.strip("\n")
    new_letter = letter.replace("[name]", formatted_name)
    with open(f"./Output/ReadyToSend/{formatted_name}.txt", "w") as new_file:
        new_file.write(new_letter)