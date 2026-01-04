ls = (12, 15, 5, 2, 7, 3, 23, 32, 1, 33)
se = int(input("What number are you searching for: "))
print(ls)

for i in range(0,len(ls)):
    print("Step", i +1)
    if ls[i] == se:
        print(se,"has been located")
        print("Number of iterations is:", i+1)
        break

    elif i == len(ls)-1:
        print("Element",se,"not found")
        break
