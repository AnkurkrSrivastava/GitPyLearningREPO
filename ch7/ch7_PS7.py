num = int(input("Enter a number to get that much line of equilateral star pattern:"))

for i in range(1, num+1):
    print(" "*(num-i), end="")
    print("*"*(2*i-1), end="")
    print()