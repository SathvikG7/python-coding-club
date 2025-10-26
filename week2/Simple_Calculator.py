num1 = 0.0
num2 = 0.0
try:
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
except:
    print("Your input is not valid")

try:
    sum_of_nums = num1 / num2
except:
    print("You cannot divide by 0")

print(num1, "Plus", num2 ,"Is equal to", sum_of_nums)
print(num1, "Plus", num2 ,"Is equal to", num1 + num2)
