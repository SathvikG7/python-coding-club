a = int(input("Enter a random number: "))
b = int(input("Enter another random number: "))
c = int(input("Enter another random number: "))

if a >= b and a >= c:
    print(f"The largest number is a = {a}")

elif b >= a and b >= c:
    print(f"The largest number is b = {b}")

else:
    print(f"The largest number is c = {c}")


largest = 0
if a >= b and a >= c:
    largest = a

elif b >= a and b >= c:
    largest = b

else:
    largest = c


print(largest)
