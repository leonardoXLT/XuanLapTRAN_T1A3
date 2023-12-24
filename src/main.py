import csv
import random
import statistics
import os

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

def create_mempal(file_name):
    mempal_name = input("Enter the name of this Memory Palace: ")
    loci = []

    while True:
        locus = input(f"Locus {len(loci) + 1}?: ")
        loci.append(locus)

        choice = input("Choose: 'Add next'(y) or 'Finish'(n): ")

        if choice.lower() == "n":
            break
        elif choice.lower() != "y":
            print("Invalid choice. Please enter 'y' or 'n'.")

    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([mempal_name] + loci)
    print("Memory Palace created successfully!")


def view_edit_mempal(file_name):
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        memory_palaces = list(reader)

    if len(memory_palaces) == 0:
        print("No Memory Palaces found.")
        return

    for i, palace in enumerate(memory_palaces):
        print(f"{i+1}. {palace[0]} - Score: {palace[-1]}%")

    choice = input("Choose an option: [A]dd, [E]dit, [D]elete, [B]ack: ")
    if choice.lower() == "a":
        create_mempal(file_name)
    elif choice.lower() == "e":
        edit_index = int(input("Enter the number of the Memory Palace to edit: ")) - 1
        new_locus = input("Enter the new locus: ")
        memory_palaces[edit_index].append(new_locus)
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(memory_palaces)
    elif choice.lower() == "d":
        delete_index = int(input("Enter the number of the Memory Palace to delete: ")) - 1
        del memory_palaces[delete_index]
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(memory_palaces)
    elif choice.lower() == "b":
        return
    else:
        print("Invalid choice. Please enter 'a', 'e', 'd', or 'b'.")


def minigame(file_name):
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        memory_palaces = list(reader)

    if len(memory_palaces) == 0:
        print("No Memory Palaces found.")
        return

# Select a Memory Palace (number) to play:
# Ask a number of questions, equal to 60% of number of loci
# score = int((correct_answers / questions_count) * 100)

def menu():
    print("Welcome to MemPal - your Memory Manager!")
    print("\nMenu:")
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
        create_mempal(file_name)
    elif (users_choice == "2"):
        view_edit_mempal(file_name)
    elif (users_choice == "3"):
        minigame(file_name)
    elif (users_choice == "4"):
        continue
    else:
        print("Invalid Input")


print("THANK YOU FOR USING MEMPAL!!")