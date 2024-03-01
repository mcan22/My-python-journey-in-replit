def logSystem():
  print("Welcome to the log system")
  print("Please enter your username and password")
  username = input("Username: ")
  password = input("Password: ")
  if username == "admin" and password == "admin":
    print("Welcome admin")
  elif username == "user" and password == "user":
    print("Welcome user")
  else:
    print("Invalid username or password")

logSystem()


def login():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password? ")
    if username == "David" and password == "Replit4ev#r":
      print("Welcome David!")
      break
    else:
      print("That is not the correct username or password. Try again!")
      continue
    
print("REPLIT LOGIN SYSTEM")
login()
