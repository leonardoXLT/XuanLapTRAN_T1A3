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

def add_mempal(existing_loci=None):
    loci = existing_loci if existing_loci else []
    while True:
        locus = input(f"Locus {len(loci) + 1}?: ")
        loci.append(locus)

        while True:  # Add this loop to keep asking until a valid choice is made
            choice = input("Choose: 'Add next'(y) or 'Finish'(n): ")

            if choice.lower() == "n":
                return loci
            elif choice.lower() == "y":
                break  # Break the inner loop if a valid choice is made
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")
                continue  # Continue the inner loop if an invalid choice is made

def create_mempal(file_name):
    mempal_name = input("Enter the name of this Memory Palace: ")
    loci = add_mempal()

    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([mempal_name] + loci + [0])  # Initialize score to 0
    print("Memory Palace created successfully!")

def view_edit_mempal(file_name):
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        memory_palaces = list(reader)

    if len(memory_palaces) == 0:
        print("No Memory Palaces found.")
        return

    # Sort the memory palaces by score
    memory_palaces.sort(key=lambda x: int(x[-1]), reverse=True)

    for i, palace in enumerate(memory_palaces):
        print(f"{i+1}. {palace[0]} - Score: {palace[-1]}%")

    palace_index = input("Select a Memory Palace (number) or 'b' to go back: ")
    if palace_index.lower() == 'b':
        return
    palace_index = int(palace_index) - 1

    print(f"Memory Palace: {memory_palaces[palace_index][0]}")
    print("Loci:")
    for i, locus in enumerate(memory_palaces[palace_index][1:-1], start=1):
        print(f"{i}.{locus}")

    while True:  # Add this loop to keep asking until a valid choice is made
        choice = input("Choose: 'Add next'(y), 'Edit'(e), 'Delete'(d), or 'Finish'(n): ")

        if choice.lower() == "n":
            break
        elif choice.lower() == "y":
            new_loci = add_mempal(memory_palaces[palace_index][1:-1])
            memory_palaces[palace_index] = [memory_palaces[palace_index][0]] + new_loci + [memory_palaces[palace_index][-1]]
        elif choice.lower() == "e":
            locus_index = int(input("Enter the number of the locus to edit: "))
            if 1 <= locus_index < len(memory_palaces[palace_index]) - 1:  # Check if the index is within the valid range
                new_locus = input("Enter the new locus: ")
                memory_palaces[palace_index][locus_index] = new_locus
            else:
                print("Invalid locus number. Please enter a valid locus number.")
        elif choice.lower() == "d":
            locus_index = int(input("Enter the number of the locus to delete: "))
            if 1 <= locus_index < len(memory_palaces[palace_index]) - 1:  # Check if the index is within the valid range
                del memory_palaces[palace_index][locus_index]
            else:
                print("Invalid locus number. Please enter a valid locus number.")
        else:
            print("Invalid choice. Please enter 'y', 'e', 'd', or 'n'.")
            continue  # Continue the loop if an invalid choice is made

    # Save the changes to the file
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(memory_palaces)

def minigame(file_name):
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        memory_palaces = list(reader)

    if len(memory_palaces) == 0:
        print("No Memory Palaces found.")
        return

    # Sort the memory palaces by score
    memory_palaces.sort(key=lambda x: int(x[-1]), reverse=True)

    for i, palace in enumerate(memory_palaces):
        print(f"{i+1}. {palace[0]} - Score: {palace[-1]}%")

    palace_index = int(input("Select a Memory Palace (number) to play: ")) - 1
    loci = memory_palaces[palace_index][1:-1]  # Exclude the name and score
    questions_count = int(len(loci) * 0.6)
    questions = random.sample(loci, questions_count)

    correct_answers = 0
    for question in questions:
        answer = input(f"What is the item at locus {loci.index(question) + 1}?: ")
        if answer == question:
            correct_answers += 1

    score = int((correct_answers / questions_count) * 100)
    print(f"Your score: {score}%")

    # Update the score in the file
    scores = list(map(int, memory_palaces[palace_index][-3:]))  # Get the last 3 scores
    scores.append(score)
    if len(scores) > 3:
        scores.pop(0)  # Keep only the last 3 scores
    average_score = int(statistics.mean(scores))
    memory_palaces[palace_index][-1] = average_score
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(memory_palaces)

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
        break
    else:
        print("Invalid Input")

print("THANK YOU FOR USING MEMPAL!!")