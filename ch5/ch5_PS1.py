# Python program to create a dictionary and translate words from Hindi to English

Trans = {"Jagah":"Place",
         "Gazab":"Amazing",
         "Jabardast":"Awesome"
        }
if input("Do you want to see the list of words in the dictionary? (yes/no): ").lower() == "yes":
    print("The list of words in the dictionary is:", Trans.keys())

a = input("Enter the word you want to translate: ")
write = "The meaning of word {a} is"
print(write.format(a=a), Trans[a])
