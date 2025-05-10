write = input("Entr your User name: ")
if (len(write) == 10):
    print("contains 10 digits")
elif (len(write) > 10):
    print("contains more than 10 digits")
elif (len(write) < 10):
    print("contains less than 10 digits")    
else:
    print("Invalid input")    