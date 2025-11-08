a = float(input("Enter a random number: "))
b = float(input("Enter another random number: "))
c = float(input("Enter another random number: "))

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
