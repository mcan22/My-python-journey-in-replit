import random
import os
from datetime import datetime

def add_idea():
    idea = input("Enter your idea: ")
    with open("my.ideas", "a") as file:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}: {idea}\n")
    print("Idea added successfully!")

def load_random_idea():
    try:
        with open("my.ideas", "r") as file:
            ideas = file.readlines()
            if ideas:
                random_idea = random.choice(ideas)
                print("Random Idea:")
                print(random_idea)
            else:
                print("No ideas found.")
    except FileNotFoundError:
        print("No ideas found.")

def main():
    while True:
        print("\nOptions:")
        print("1. Add an idea")
        print("2. Load a random idea")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_idea()
        elif choice == "2":
            load_random_idea()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
