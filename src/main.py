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