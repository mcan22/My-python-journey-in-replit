while exit!="yes":
  animalPick=input("What animal do you want? ")
  if animalPick=="cow":
    print("A cow goes moo.")
  elif animalPick=="A Lesser Spotted lemur":
    print("Ummm...the Lesser Spotter Lemur goes awooga.")
  elif animalPick=="dog":
   print("A dog goes woof.")
  elif animalPick=="cat":
    print("A cat goes meow.")
  elif animalPick=="sheep":
    print("A sheep goes baa.")
  else:
    print("I don't know that animal.")
  exit=input("Do you want to exit? ")
print("I guess you didn't like the game")

for _ in range(10):
    print("I am very sad to hear that")
