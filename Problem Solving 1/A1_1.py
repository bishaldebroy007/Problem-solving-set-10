# Write Python code of a program that reads two numbers from the user, and prints their sum, product, and difference.

# ==========================================================

# hint: Subtract the second number from the first one

# ==========================================================

# Example01:

# Input:
# 4
# 5

# Output:
# Sum = 9
# Product = 20
# Difference = -1

# ==========================================================

# Example02:

# Input:
# 30
# 2

# Output:
# Sum = 32
# Product = 60
# Difference = 28

# ==========================================================

# For your explanation, the first question's code is done below. Try relating the block of code with the lesson you have learned and understand the significance of each line. You're most welcome to play around with the code. This will strengthen your understanding.

#Solution:

### Take input of 2 numbers from the user
var_1 = input('Please Enter Your First Number')
var_2 = input('Please Enter Your Second Number')

#Since input() function converts everything to String,
#for performing any kind of mathematical operation you need to convert them to int.
#For this conversion, we need to use int() function


# First, let's clarify whether the inputs are actually Strings or not. 
print(type(var_1))
print(type(var_2))


# Convert Strings to integer using the int() function
var_3 = int(var_1)
var_4 = int(var_2)

#===============================================================
#input taking and conversion can be done in a single sentense
#var_1 = int(input('Please Enter Your First Number'))
#var_2 = int(input('Please Enter Your Second Number'))

#===============================================================

# Perform Addition
sum = var_3 + var_4

# Perform Multiplication 
product = var_3 * var_4

# Perform Substraction 
difference = var_3 - var_4


print("Sum =", sum)
print("Product =", product)
print("Difference =", difference)