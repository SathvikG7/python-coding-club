person1_exp = int(input("Enter person 1 expenses:"))
person2_exp = int(input("Enter person 1 expenses:"))

def calculate_vat(exp):
    print("the expense is:", exp)
    vat = exp * 20/100
    print("The VAT is: ", vat)
    return vat

def calculate_min_day():
    return 24 * 60

person1_vat = calculate_vat(person1_exp)
print("Person1 VAT:", person1_vat)

person2_vat = calculate_vat(person2_exp)
print("Person2 VAT:", person2_vat)

print(calculate_min_day())
