from turtle import *
import math

while True:
    lengthOfSquare=int(input("Enter the length of square: "))
    raduisOfCircle=int(input("Enter the radius of the circle: "))
    diameterOfCircle = raduisOfCircle*2

    if lengthOfSquare < diameterOfCircle:
        print("Invalid input")

    else:
        pencolor("red")
        for i in range(4):
            forward(lengthOfSquare)
            right(90)

        halfOfLength=lengthOfSquare/2
        startOfCircle=halfOfLength-raduisOfCircle

        penup()
        forward(startOfCircle)
        right(90)
        forward(halfOfLength)
        pendown()
        circle(raduisOfCircle)
        done()

        areaOfSquare=lengthOfSquare**2
        areaOfCircle=math.pi*(raduisOfCircle**2)

        print("the area of square is :", areaOfSquare)
        print("the area of circle is :", areaOfCircle)
        print("The remaining area is : ", areaOfSquare-areaOfCircle)
        break