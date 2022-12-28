# Write Python code of a program that reads the radius of a circle and prints its circumference and area.

# ==========================================================

# hint(1): import math and then use math.pi for getting the value of pi.
# For details read from https://docs.python.org/3/library/math.html

# hints(2): You can import math and use math function for making squares math.pow(number, power) Or you can simply write using power opeartor. For example: S**2.

# ==========================================================

# Example01:

# Input: 4

# Output:
# Area is 50.26548245743669
# Circumference is 25.132741228718345

# ==========================================================

# Example02:

# Input: 3.5

# Output:
# Area is 38.48451000647496
# Circumference is 21.991148575128552

# ==========================================================

# For your explanation, the the first part of the question(area calculation) is done below.

#Solution:
import math 

#taking input from the user, then converting it to float.
#Since radius can be a floating point value

radius  = float(input("please enter the radius value:")) 


# squares can be made using this 3 ways, as written in hints. 
# all 3 ways, generates the same result of area

area = math.pi * radius **2 
print("Area result is:", area)

area = math.pi * math.pow(radius, 2)
print("Area result is:", area)

area = math.pi * radius * radius
print("Area result is:", area)

circumference = 2 * math.pi * radius      # circumference(Circle): 2*pai*r
print("Circumference is:", circumference)