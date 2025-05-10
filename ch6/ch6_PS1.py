# rite a Python program to find the largest of four numbers.

a  = [int(input("Enter 4 numbers:"))for i in range(4)]   
if (a[0] > a[1] and a[0] > a[2] and a[0] > a[3]):
    print("The largest number is: ", a[0])
elif (a[1] > a[0] and a[1] > a[2] and a[1] > a[3]):
    print("The largest number is: ", a[1])
elif (a[2] > a[0] and a[2] > a[1] and a[2] > a[3]):
    print("The largest number is: ", a[2])
elif (a[3] > a[0] and a[3] > a[1] and a[3] > a[2]):
    print("The largest number is: ", a[3])
else:
    print("All numbers are equal")            
