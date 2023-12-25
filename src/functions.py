import csv
import random
from colorama import Fore, Style, init
from pyfiglet import figlet_format
from colored import fg, bg, attr

init()

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
    print(Fore.GREEN + figlet_format("Creating New Memory Palace", font="small") + Style.RESET_ALL)
    mempal_name = input("Enter the name of this Memory Palace: ")
    loci = add_mempal()

    with open(file_name, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([mempal_name] + loci + [0, 0])  # Initialize score and average score to 0
    print("Memory Palace created successfully!")


def view_edit_mempal(file_name):
    print(Fore.GREEN + figlet_format("Viewing/Editing Memory Palace", font="small") + Style.RESET_ALL)
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            memory_palaces = list(reader)

        if len(memory_palaces) == 0:
            print("No Memory Palaces found.")
            return

        # Sort the memory palaces by score
        memory_palaces.sort(key=lambda x: int(x[-1]), reverse=True)

        for i, palace in enumerate(memory_palaces):
            print(f"{Fore.GREEN}{i+1}. {palace[0]} - Score: {palace[-1]}%{Style.RESET_ALL}")

        while True:  # Add this loop to keep asking until a valid choice is made
            try:
                palace_index = input('%s%s%s' % (fg('red'), "Select a Memory Palace (number) or 'b' to go back: ", attr('reset')))
                if palace_index.lower() == 'b':
                    return
                palace_index = int(palace_index) - 1
                break  # Break the loop if a valid choice is made
            except ValueError:
                print("Invalid input. Please enter a number or 'b' to go back.")
                continue # Continue the loop if an invalid choice is made

        print(f"Memory Palace: {memory_palaces[palace_index][0]}")
        print("Loci:")
        for i, locus in enumerate(memory_palaces[palace_index][1:-2], start=1):  # Exclude the name and scores
            print(f"{i}.{locus}")

        while True:  # Add this loop to keep asking until a valid choice is made
            try:
                choice = input('%s%s%s' % (fg('blue'), "Choose: 'Add next'(y), 'Edit'(e), 'Delete'(d), 'Remove Memory Palace'(r), or 'Finish'(n): ", attr('reset')))

                if choice.lower() == "n":
                    break
                elif choice.lower() == "y":
                    new_loci = add_mempal(memory_palaces[palace_index][1:-2])
                    memory_palaces[palace_index] = [memory_palaces[palace_index][0]] + new_loci + memory_palaces[palace_index][-2:]
                elif choice.lower() == "e":
                    locus_index = int(input("Enter the number of the locus to edit: "))
                    if 1 <= locus_index < len(memory_palaces[palace_index]) - 2:  # Check if the index is within the valid range
                        new_locus = input("Enter the new locus: ")
                        memory_palaces[palace_index][locus_index] = new_locus
                    else:
                        print("Invalid locus number. Please enter a valid locus number.")
                elif choice.lower() == "d":
                    locus_index = int(input("Enter the number of the locus to delete: "))
                    if 1 <= locus_index < len(memory_palaces[palace_index]) - 2:  # Check if the index is within the valid range
                        del memory_palaces[palace_index][locus_index]
                    else:
                        print("Invalid locus number. Please enter a valid locus number.")
                elif choice.lower() == "r":
                    del memory_palaces[palace_index]
                    print("Memory Palace removed successfully!")
                    break
                else:
                    print("Invalid choice. Please enter 'y', 'e', 'd', 'r', or 'n'.")
                    continue
            except Exception as e:
                print(f"An error occurred: {e}")
                continue  # Continue the loop if an invalid choice is made

        # Save the changes to the file
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(memory_palaces)
    except Exception as e:
        print(f"An error occurred: {e}")


def minigame(file_name):
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            memory_palaces = list(reader)

        if len(memory_palaces) == 0:
            print("No Memory Palaces found.")
            return
        
        # Sort the memory palaces by score
        memory_palaces.sort(key=lambda x: int(x[-1]), reverse=True)

        print(Fore.GREEN + figlet_format("Welcome! to MemPal minigame", font="speed") + Style.RESET_ALL)

        for i, palace in enumerate(memory_palaces):
            print(f"{Fore.GREEN}{i+1}. {palace[0]} - Score: {palace[-1]}%{Style.RESET_ALL}")

        while True:  # Add this loop to keep asking until a valid choice is made
            try:
                palace_index = input('%s%s%s' % (fg('yellow'), "Select a Memory Palace (number) to play or 'b' to go back: ", attr('reset')))
                if palace_index.lower() == 'b':
                    return
                palace_index = int(palace_index) - 1
                break  # Break the loop if a valid choice is made
            except ValueError:
                print("Invalid input. Please enter a number or 'b' to go back.")
                continue  # Continue the loop if an invalid choice is made

        loci = memory_palaces[palace_index][1:-2]  # Exclude the name and scores
        questions_count = int(len(loci) * 0.75)  # Change to 75% of the total number of loci
        questions = random.sample(loci, questions_count)

        correct_answers = 0
        for question in questions:
            answer = input(f"What is the item at locus {loci.index(question) + 1}?: ")
            if answer == question:
                correct_answers += 1

        score = int((correct_answers / questions_count) * 100)
        print(f"Your score: {score}%")

        # Update the score in the file
        previous_score = int(memory_palaces[palace_index][-2])  # Get the previous score
        average_score = int((previous_score + score) / 2)  # Calculate the average of the recent score and the previous score
        memory_palaces[palace_index] = memory_palaces[palace_index][:1] + loci + [score, average_score]
        with open(file_name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(memory_palaces)
    except Exception as e:
        print(f"An error occurred: {e}")