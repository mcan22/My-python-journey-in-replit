print("List Generator")
print()
print()

startat=int(input("Start at:"))
Endbefore=int(input("End before:"))
Increment=int(input( "Increment between values:"))

for i in range(startat,Endbefore,Increment):
  print(i)

print("Welcome to my number list generator.")
print()
print("You are going to give me a number you want to start with, an ending number, and by how many you want me to add each time.")
print()

x = int(input("What number do you want to start with? "))
y = int(input("What number do you want to end with? "))
z = int(input("How many should I add each time? "))

for i in range(x, y, z):
  print(i)
