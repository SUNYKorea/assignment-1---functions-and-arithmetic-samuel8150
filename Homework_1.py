# Name: Jinwan Kim
# SBUID: 110602105
##################### SCORE ######################
####### Score:  6/10
#################################################
# Remove the ellipses (...) when writing your solutions.
#### Your output:
# (base) D:\CSE 101 Ass1\Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27>D:/anaconda/python.exe "d:/CSE 101 Ass1/Assignment 1 - Functions and Arithmetic-04-05-2023-05-19-27/samuel8150/Homework_1.py"
# wear Sweater--> correct
# The area of the triangle is : 32.0 --> correct , its perimeter is : 130.0--> wrong
# The area of the polygon is : 2.580488365589943-> wrong
# ---------------------------- Exercise I ---------------------------------------
# ----------------- Convert Fahrenheit to Celsius -------------------------------
# TODO: Complete the implementation of fahrenheit2celsius () and what_to_wear(). 

def fahrenheit2celsius(fahrenheit): 
#    fahrenheit = int(input("input F : "))
#    celsius = int(((5 / 9)*(fahrenheit - 32)))
#    print("Celcius : " + str(celsius))
#    return fahrenheit

    celsius = ((5 / 9)*(fahrenheit - 32))
    return celsius

fahrenheit2celsius(100)

def what_to_wear(celsius):
    clothe_list = ['Puffy Jacket', 'Scarf', 'Sweater', 'Light Jacket', 'T-shirt']
    if celsius < -11:
        print("wear " + clothe_list[0])
    elif -10 < celsius < 0:
        print("wear " + clothe_list[1])
    elif 1 < celsius < 10:
        print("wear " + clothe_list[2])
    elif 11 < celsius < 20:
        print("wear " + clothe_list[3])
    else:
        print("wear " + clothe_list[4])
    return celsius

# ---------------------------- Exercise II --------------------------------------
# ----------------- Area and perimeter of a triangle  ---------------------------
# TODO: Fill the functions shoelace_triangle_area, euclidean_distance and
# compute_triangle_perimeter from scratch  

def shoelace_triangle_area(x1, y1, x2, y2, x3, y3):
    area = abs((((x1 * y2) + (x2 * y3) + (x3 * y1)) - ((x1 * y3) + (x2 * y1) + (x3 * y2)))/2)
    return area

s_area = shoelace_triangle_area(10, 8, 6, 5, 7, 9)


def euclidean_distance(x1, y1, x2, y2):
    distance = (((( x1 - x2 )**2) +(( y1 - y2 )**2) )**1/2)
    return distance

E_dis = euclidean_distance(10, 8, 6, 5)

def compute_triangle_perimeter(x1, y1, x2, y2, x3, y3):
    s1 = (((( x1 - x2 )**2) +(( y1 - y2 )**2) )**1/2)
    s2 = (((( x2 - x3 )**2) +(( y2 - y3 )**2) )**1/2)
    s3 = (((( x3 - x1 )**2) +(( y3 - y1 )**2) )**1/2)
    primeter = s1 + s2 + s3
    return primeter

compute_triangle_perimeter(10, 8, 6, 5, 7, 9) 

# ---------------------------- Exercise III -------------------------------------
# ----------------- Compute the area of a regular polygon -----------------------
# TODO: Fill the functions deg2rad, apothem  and polygon_area 

import math
def deg2rad(deg):
    # deg = int(input("degree : "))
    # rad = int(deg * math.pi/180)
    # print("radius : " + str(rad))

    radian = (deg * math.pi/180)
    return radian

deg2rad(180)

def apothem(number_sides, length_side):
    apo = (length_side/(2 * math.tan(180/number_sides)))
    return apo

apothem(5, 5)


def polygon_area(number_sides, length_side):
    apo = (length_side/(2 * math.tan(180/number_sides)))
    area_pol = ((number_sides * length_side) * (apo)/2)
    return area_pol

polygon_area(5, 5)

# ---------------------------- Test -------------------------------------
# The following lines are for testing purposes, and will not be part of
# your grade. You may freely modify the following codes.

# Exercise 1 test
fahrenheit = 40
what_to_wear(fahrenheit2celsius(fahrenheit))

# Exercise 2 test
x1, x2, x3, y1, y2, y3 = -4, -5, 3, -4, 5, -3 # declaration of the vertices of the triangle
area = shoelace_triangle_area(x1, y1, x2, y2, x3, y3)
perimeter = compute_triangle_perimeter(x1, y1, x2, y2, x3, y3)
print("The area of the triangle is : " + str(area) + " , its perimeter is : " + str(perimeter) )

# Exercise 3 test
number_sides = 5
length_side = 4
print ("The area of the polygon is : " + str(polygon_area(number_sides, length_side)))

