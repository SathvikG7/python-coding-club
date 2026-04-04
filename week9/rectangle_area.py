PI=3.14

def calculateArea(l,w):
    global length
    area = l*w
   # print(area)
    print("length:", length)
    length=length+10
    return area

def circleArea(r):
    return PI*r*r

length=15
breadth=10
area = calculateArea(length,breadth)
print(length)
print(area)
length=27
length=length+5
breadth=3
area1 = calculateArea(length,breadth)
print(length)
print(area1)

areaOfCircle=circleArea(6)
print("circle:", areaOfCircle)
