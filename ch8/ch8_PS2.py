def temp():
    c = int(input("Enter temp in celsius: "))
    f = (c * 9/5) + 32
    return f

print(f"The temp in fahrenheit is {temp()}")