num = int(input("Enter a number to know it's multiolication table: "))
if num > 0:
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")
else:
    print("Please enter a positive number")