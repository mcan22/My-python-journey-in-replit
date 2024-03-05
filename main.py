print("5 Days Down- What did you think?")
print()
for i in range(1, 6):
  print("Day",i,":")
  userInput=input()
  print("      You thougt Day",i,"was",userInput)  # Aligned output



print()

print("10 Days Down - What did you think?")
print()
for i in range(1, 11):
  thought = input(f"Day {i}:\n")
  print()
  myText = f"You thought Day {i} was"
  print(f"{myText:^35}")
  print(f"{thought:^35}")
  print()

