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
  
