num = int(input("Enter a number to know its factorial:"))
fact = 1
i =1
for i in range(1, num+1):
    fact = fact * i
print("Factorial of", num, "is", fact)