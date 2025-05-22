def convert():
    num = int(input("Enter inch to convert into cm:"))
    if num > 0:
        cm = num * 2.54
        print(f"{num} inches = {cm} cm")
    else:
        print("Please enter a positive number")
convert()           