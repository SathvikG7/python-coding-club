menu = {"Stir Fry": [6.50, True],
        "Jamun": [1.50, True],
        "Samosa": [1.75, True],
        "Kebab": [3.00, False],
        "C Biryani": [5.00, False],
        "Lasagne": [7.00, False]
}

menulist=[["Stir Fry", 6.50, True], ["Jamun", 1.50, False]]
print(menulist[0:])
print(len(menulist))
for item in menulist:
    if item[2] == True:
        print(item)

# print("Vegetarian menu:")
# for key,value in menu.items():
#     if value[1] == True:
#         print(key, "-", "£",value[0])

# maxPrice=float(input("Enter the max price per item:"))
# print("items with price less than ", maxPrice)
# for key,value in menu.items():
#     if value[0]<=maxPrice :
#         print(key, "-", "£",value[0])
