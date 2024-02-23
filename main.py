print("Wholesome Positivity Machine")
print("who are you?")
name = input()
if name== "David" or name== "david":
  print("What do you want to achieve?")
  goal = input()
  print("On a scale of 1 - 10 how do you feel today? (1: 😢, 10: 🥳)")
  emotion=int(input())
  if emotion>5:
    print("perfect")
  else:
    print("Can I help you?")
    getthefeedback=input()
    if getthefeedback=="yes" or getthefeedback=="Yes":
      print("Take pills")
    else:
      print("go find someone to help you then mate")
elif name=="Mark" or name=="mark":
    print("What do you want to achieve in life my dear brother?")
    goal = input()
    print("On a scale of 1 - 10 how do you feel today? (1: 😢, 10: 🥳)")
    emotion=int(input())
    if emotion>8:
      print("You gotta help me then mate i even dont feel that good?")
    else:
      print("oh dear brother what happened, can i help")
      getthefeedback=input()
      if getthefeedback=="yes" or getthefeedback=="Yes":
        print("Take a hike")
      else:
        print("go find someone to help you then mate")
else:
  print("I can only answer questions for Davids or Marks")