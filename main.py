print("Math Game!")
print()

multiples = int(input("Name your multiples: "))
print()

counter=0
for i in range(1,11):
  correct_answer = i*multiples
  print(i, "x", multiples,"=")
  answer = int(input("> "))
  if answer == correct_answer:
    counter+=1
  else:
    print("That's not correct. It should have been", correct_answer)
if counter > 5:
  print("You scored", counter, "out of 10. Amazing!")
  
