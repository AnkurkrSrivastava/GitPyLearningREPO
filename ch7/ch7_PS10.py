# program to print the multiplication table of a number in reverse order

num = int(input("Enter a number: "))
if num > 0:
    for i in range(10,0,-1):
        print(f"{num} X {i} = {num*i}")
