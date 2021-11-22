'''a = int(input("1 \n"))
b = int(input("2 \n"))
c = int(input("3 \n"))
d = int(input("4 \n"))
if a > b and a > c and a > d:
    print(a)
elif b > c and b > d:
    print(b)
elif c > d:
    print(c)
else:
    print(d)'''
"""FLOORS = 9
ENTRANCE = 4
NUM_FLATS = 4
apartment_number = int(input("enter the house number \n"))-1
entrance_number = (apartment_number // (FLOORS * ENTRANCE))+1
FLOOR_NUMBER = (apartment_number // NUM_FLATS - (entrance_number - 1) * FLOORS) + 1
if apartment_number <= 143:
    print("entrance number is", entrance_number, "floor number is ", FLOOR_NUMBER, sep="\n")
else:
    print("there is no such apartment in this house")"""
# Exercise 1.
"""number = list(input("Enter number "))
if int(number[0])+int(number[1]) == int(number[-2]) + int(number[-1]):
    print("happy ticket")
else:
    print("failure")"""
# Exercise 2.
"""number = list(input("Enter number "))
number_reverse = number[::-1]
if number == number_reverse:
    print("True")
else:
    print("False")"""
# Exercise 3.
"""RADIUS = 4
import math
x_point, y_point = float(input("x = ")), float(input("y = "))
if math.sqrt(x_point ** 2 + y_point ** 2) <= RADIUS:
    print("The point belongs to the circle")
else:
    print("The point does NOT belong to the circle")"""
