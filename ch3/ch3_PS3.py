# This program will ask the user to enter their name and then print the name with extra spaces removed.

name =  input("Enter your name: ")
print(name.find("  "))
print(name.replace("  ", " "))