def sum(n):
    if (n == 1):
        return 1
    return sum(n-1) + n

num = int(input("Enter a number to get sum of that much number: "))
print(sum(num))