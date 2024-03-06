print("ToDo List Manager")
print()

itemList = []

def printList():
    print()
    for item in itemList:
        print(item)
    print()

while True:
    menu = input("Do you want to view, add, or edit your to-do list? ")

    if menu == "view":
        printList()

    elif menu == "add":
        item = input("What do you want to add? ")
        itemList.append(item)

    elif menu == "edit":
        item = input("What do you want to remove? ")

        if item in itemList:
            itemList.remove(item)
            new_item = input("What do you want to add instead of the removed one? ")
            itemList.append(new_item)
        else:
            print(f"{item} was not in the list")

    else:
        print("Invalid option. Please choose 'view', 'add', or 'edit'.")

  
