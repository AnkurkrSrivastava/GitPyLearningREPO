num = int(input("Enter a number to know it's multiplication table: "))
while (num > 0):
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")
    break
else:
    print("Please enter a positive number")