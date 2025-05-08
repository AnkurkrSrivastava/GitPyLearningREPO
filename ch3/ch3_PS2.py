# Problem Statement 2: String Formatting

name = input("Enter your name: ")
date = input("Enter the date: ")

letter = '''Dear {name},
you are selected!
{date}'''
print(letter.format(name=name, date=date))
