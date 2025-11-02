import math
is_prime = True
num1 = int(input("Enter any number: "))
for i in range(2,(num1//2)):
    if num1%i == 0:
        print("(IF) The value of i is:",i)
        is_prime = False
        break
    else:
        print("(ELSE) The value of i is:", i)
if is_prime:
    print("It is a prime number")

else:
    print("It is not a prime number")
