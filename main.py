print("Welcome to Name the Song Lyric")
print()
print("Figure out the missing word as quickly as you can!")
print()

counter = 1
while True:
    lyrics = input("I don't wanna ______ a thing. ")
    if lyrics == "miss" or lyrics == "Miss":
        print("You got it!")
        break
    else:
        print("Nope! Try again!")
        counter += 1

print("Thanks for playing!")
print("You got the correct first lyrics in", counter, "attempt(s).")
print()
print("Time to guess the second lyrics")
counter2 =1
while True:
  lyrics2 = input("Take me to ______ . ")
  if lyrics2 == "church" or lyrics2 == "Church":
      print("You got it!")
      break
  else:
      print("Nope! Try again!")
      counter2 += 1
print()
print("Thanks for playing the second round!")
print("You got the correct second lyrics in", counter2, "attempt(s).")
