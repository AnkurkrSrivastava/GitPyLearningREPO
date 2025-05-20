# Floyd's Triangle

p = 0
for a in range(1, 6):
    for b in range(1, a+1):
        p = p + 1
        print(p, end=" ")
    print()    