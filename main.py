import os
import time

toDoList = []
file_name = "to_do.txt"

def printList():
    print()
    for item in toDoList:
        print(item)
    print()

def saveList():
    with open(file_name, "w") as f:
        for item in toDoList:
            f.write(item + "\n")

def loadList():
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            for line in f:
                toDoList.append(line.strip())

# Program başlangıcında dosyadan verileri yükle
loadList()

while True:
    menu = input("ToDo List Manager\nDo you want to view, add, edit, remove or delete the todo list?\n").lower()
    if menu == "view":
        printList()
    elif menu == "add":
        item = input("What do you want to add?\n").title()
        toDoList.append(item)
        saveList()
    elif menu == "remove":
        item = input("What do you want to remove?\n").title()
        check = input("Are you sure you want to remove this?\n").lower()
        if check.startswith("y"):
            if item in toDoList:
                toDoList.remove(item)
                saveList()
    elif menu == "edit":
        item = input("What do you want to edit?\n").title()
        new = input("What do you want to change it to?\n").title()
        for i in range(len(toDoList)):
            if toDoList[i] == item:
                toDoList[i] = new
        saveList()
    elif menu == "delete":
        toDoList = []
        saveList()
    time.sleep(1)
    os.system('clear')
