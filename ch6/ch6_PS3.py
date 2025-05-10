# Basic program to check if a message is spam or not

p1="make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

write = input("Enter a Message: ")
if(p1 in write or p2 in write or p3 in write or p4 in write):
    print("This message is spam")
else:
    print("This message is not spam")    