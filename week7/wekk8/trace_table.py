evenSum=0
oddSum=0
total=0
for i in range(1,11):
    total += i
    if i%2 == 0:
        evenSum += i
    else:
        oddSum = oddSum + i
    print("evenSum:", evenSum)
    print("oddSum:", oddSum)
    print("total:", total)

