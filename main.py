import random, os, time

def rollDice(sides):
  result = random.randint(1, sides)
  return result

def calculate_health():
  roll_6_sided_dice = rollDice(6)
  roll_12_sided_dice = rollDice(12)
  health_value = ((roll_6_sided_dice * roll_12_sided_dice) / 2) + 12
  return health_value

def calculate_strength():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  strength_value = ((roll_6_sided_dice * roll_8_sided_dice) / 2) + 12
  return strength_value


haveACharacter = "yes"
while haveACharacter.lower() == "yes":
  print("⚔️ Character Stats Generator ⚔️")
  print()
  character = input("Name your warrior: ")
  character_type = input("Character type (Human, Elf, Wizard, Orc): ")
  character_health = str(calculate_health())
  character_strength = str(calculate_strength())
  print(character,"the",character_type)
  print("Their health is", character_health, "hp")
  print("Their strength is", character_strength, "hp")
  print()
  haveACharacter = input("Want to create another character? ")

  if haveACharacter.lower() == "yes":
    time.sleep(1)
    os.system("clear")
    continue
  else:
    break

