# Program to check if a name is in the list and starts with 'S'

l1 = ["Ankur", "Sachin", "Sahil", "Rahul"]
name = input("Enter a name: ")
if (name in l1 and name.startswith("S")):
    print(f"Hello and good morning {name}")
else:
    print("You are not in the list or your name does not start with 's'")