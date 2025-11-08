fname = str(input("Enter your first name: "))
sname = str(input("Enter your second name: "))

fname = fname[0:2].upper()
sname = sname[0:2].upper()
full_name = fname + sname

print(f"{full_name}@my.strschool.co.uk")

full_name_2 = full_name.replace("A","1")

print(f"{full_name_2}@MY.STRSCHOOL.CO.UK")
