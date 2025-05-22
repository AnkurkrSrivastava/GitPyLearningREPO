def table():
    num = int(input("Enter a number to get its multiplication table: "))
    if num > 0:
        for i in range(1, 11):
            print(f"{num} X {i} = {num*i}")
    print()

table()