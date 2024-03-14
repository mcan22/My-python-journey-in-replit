import os, time, random

print("TOP TRUMPS")
print("----------")
print()
print("Characters")
print()
print("Mr Spock")
print("David")
print("Monica from Friends")
print("Professor X")

# Karakterler ve özelliklerini içeren bir sözlük
characters = {
    "Mr Spock": {"Intelligence": 90, "Speed": 70, "Power": 80, "Lightning": 85},
    "David": {"Intelligence": 75, "Speed": 60, "Power": 65, "Lightning": 70},
    "Monica from Friends": {"Intelligence": 80, "Speed": 65, "Power": 70, "Lightning": 75},
    "Professor X": {"Intelligence": 95, "Speed": 55, "Power": 90, "Lightning": 80}
}

charlist = list(characters.keys())

print()

character = input("Pick your character\n> ")
if character in charlist:
    print(f"You have picked {character}")
else:
    print("You have picked an invalid character")

print()

computer_pick = random.choice(charlist)
print(f"Computer picked {computer_pick}")

stat = input("Choose your stat: Intelligence, Speed, Power, or Lightning\n> ")

# Seçilen karakterlerin özelliklerini alıp karşılaştırma yapmak için
player_stat = characters[character][stat]
computer_stat = characters[computer_pick][stat]

print(f"Your {stat}: {player_stat}")
print(f"Computer's {stat}: {computer_stat}")

if player_stat > computer_stat:
    print("You win!")
elif player_stat < computer_stat:
    print("Computer wins!")
else:
    print("It's a tie!")
# More Advanced way of writing it is shown below


#import os, time, random

trumps = {}
trumps["David"] = {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness Level": 99}
trumps["Mr Spock"] = {"Intelligence": 200, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Moica from Friends"] = {"Intelligence": 150, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Professor X"] = {"Intelligence": 250, "Speed": 1, "Guile": 200, "Baldness Level": 101}

while True:
  print("TOP TRUMPS")
  print()
  print("Characters")
  print()
  for key in trumps:
    print(key)
  user = input("Pick your character\n> ")
  comp = random.choice(list(trumps.keys()))
  print("Computer has picked", comp)

  print("Choose your stat: Intelligence, Speed, Guile & Baldness Level")

  answer = input("> ")

  print(f"{user}: {trumps[user][answer]}")
  print(f"{comp}: {trumps[comp][answer]}")

  if trumps[user][answer] > trumps[comp][answer]:
    print(user, "wins")
  elif trumps[user][answer] < trumps[comp][answer]:
    print(comp, "wins")
  else:
    print("Draw")


  time.sleep(2)
  os.system("clear")

