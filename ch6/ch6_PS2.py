a = [int(input("Enter marks of 3 subjects in percent:")) for i in range(3)]
if (a[0] and a[1] and a[2] >= 33):
    b = (a[0] + a[1] + a[2]) * 100 / 300
    if (b >= 40):
        print("You are pass with percentage: ", b)
    else:
        print("You are fail with percentage: ", b)
else:
    b = (a[0] + a[1] + a[2]) * 100 / 300  # Ensure b is defined
    print("You are fail with percentage: ", b)        

