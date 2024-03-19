import os, time
pizza = []


try:
  f = open("pizza.txt", "r")
  pizza = eval(f.read())
  f.close()
except:
  print("ERROR: No existing pizza lsit using a blank list")

def addPizza():
  time.sleep(1)
  os.system("clear")
  name = input("Name: ")
  size = input("Size (s/m/l): ").lower()
  while True:
    try:
      qty = int(input("Quantity: "))
      break
    except:
      print("Error: Quantity must be a whole number")
  cost = 0
  if size == "s":
    cost = 5.99
  elif size == "m":
    cost = 9.99
  else:
    cost = 14.99
  total = cost * qty
  total = round(total, 2)
  row = [name, size, qty, total]
  pizza.append(row)

def viewPizza():
  h1 = "Name"
  h2 = "Size"
  h3 = "Quantity"
  h4 = "Total"
  print(f"{h1:^10}{h2:^20}{h3:^10}{h4:^10}")
  for row in pizza:
    print(f"{row[0]:^10}{row[1]:^20}{row[2]:^10}{row[3]:^10}")
  time.sleep(2)

while True:
  time.sleep(1)
  os.system("clear")
  print("Rominos Pizza")
  print()
  menu = input("1: Add Pizza\n2: View Pizza\n> ")
  if menu == "1":
    addPizza()
  else:
    viewPizza()
  f = open("pizza.txt", "w")
  f.write(str(pizza))
  f.close()
