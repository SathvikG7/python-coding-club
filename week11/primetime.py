import math
def isPrime(n):
#    for i in range(2,math.ceil(math.sqrt(n))):
    for x in range(2,int(n/2)+1):
        division = n%x
        if division == 0:
            return False
    return True
      
num = int(input("Enter a number: "))
for i in range(2,num):
    if isPrime(i):
        print(i,"is a prime number")