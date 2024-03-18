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

# MORE ADVANCED CODE

# | Name | Date | Priority
import os, time
todo = []
f = open("to.do", "r")
todo = eval(f.read())
f.close()

def add():
  time.sleep(1)
  os.system("clear")
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def view():
  time.sleep(1)
  os.system("clear")
  options = input("1: All\n2: By Priority\n> ")
  if options=="1":
    for row in todo:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority? > ").capitalize()
    for row in todo:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
  time.sleep(1)

def edit():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to edit > ")
  found = False
  for row in todo:
    if find in row:
      found = True
  if not found:
    print("Couldn't find that")
    return
  for row in todo:
    if find in row:
      todo.remove(row)
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  todo.append(row)
  print("Added")

def remove():
  time.sleep(1)
  os.system("clear")
  find = input("Name of todo to remove > ")
  for row in todo:
    if find in row:
      todo.remove(row)

while True:
  menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  else:
    remove()

  time.sleep(1)
  os.system("clear")
  f = open("to.do", "w")
  f.write(str(todo))
  f.close()
