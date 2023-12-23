
file_name = "Mempal.csv"

try:
    # open the file in read mode
    todo_file = open(file_name, "r")
    todo_file.close()
    print("In try block")
    # if it throws error, it means the file doesn't exist
    # if no error, it means the file exist
except FileNotFoundError:
    # Now, we know the file doesn't exist
    # Create the file
    todo_file = open(file_name, "w")
    # We can also insert the first line into the file
    todo_file.write("title,completed\n")
    todo_file.close()
    print("In except block")

def menu():
    print("1. Create New Memory Palace")
    print("2. View/Edit Memory Palace")
    print("3. Play the mini game")
    print("4. Exit")
    choice = input("Choose an option: ")
    return choice

users_choice = ""

while users_choice != "4":
    users_choice = menu()
    if (users_choice == "1"):
        print("1")
    elif (users_choice == "2"):
        print("2")
    elif (users_choice == "3"):
        print("3")
    elif (users_choice == "4"):
        continue
    else:
        print("Invalid Input")