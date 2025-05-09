# Python program to create a dictionary and print the favorite language of a person
#2 names are same and their languages are different

s = {} # empty dictionary
name = [input("Enter the name of people: ")for i in range(4)]
lang = [input("Enter your favorite language as value of dictionary: ") for i in range(4)]

for i in range(4):
    s[name[i]] = lang[i] # dictionary creation

person = input("Enter the name of the person whose favorite language you want to know: ")
if person in s:
    write = "Favorite of {per} is {fav}"
    print(write.format(per=person, fav=s[person]))
else:
    print("The name is not in the dictionary", person)

    