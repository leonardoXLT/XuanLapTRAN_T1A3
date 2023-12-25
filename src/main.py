from functions import add_mempal, create_mempal, view_edit_mempal, minigame
from colorama import init, Fore, Style
from pyfiglet import figlet_format
from colored import fg, bg, attr

init()

file_name = "Mempal.csv"

try:
    mempal_file = open(file_name, "r")
    mempal_file.close()
    print("In try block")
except FileNotFoundError:
    mempal_file = open(file_name, "w")
    mempal_file.write("")
    mempal_file.close()
    print("In except block")

def menu():
    print(Fore.GREEN + figlet_format("Welcome to MemPal - your Memory Manager!", font="small") + Style.RESET_ALL)
    print("\nMenu:")
    print(Fore.BLUE + "1. Create New Memory Palace" + Style.RESET_ALL)
    print(Fore.BLUE + "2. View/Edit Memory Palace" + Style.RESET_ALL)
    print(Fore.BLUE + "3. Play the mini game" + Style.RESET_ALL)
    print(Fore.BLUE + "4. Exit" + Style.RESET_ALL)
    choice = input('%s%s%s' % (fg('yellow'), "Choose an option: ", attr('reset')))
    return choice

users_choice = ""

while users_choice != "4":
    users_choice = menu()
    if (users_choice == "1"):
        create_mempal(file_name)
    elif (users_choice == "2"):
        view_edit_mempal(file_name)
    elif (users_choice == "3"):
        minigame(file_name)
    elif (users_choice == "4"):
        break
    else:
        print("Invalid Input")

print(Fore.YELLOW + figlet_format("THANK YOU FOR USING MEMPAL!!", font="small") + Style.RESET_ALL)
