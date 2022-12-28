# Write Python code of a program that reads two numbers, subtracts the smaller number from the larger one, and prints the result.

# hint(1): First check which number is greater

# hint(2): You can consider the numbers to be floating point values

# ==========================================================

# Example:

# Input:
# -40
# -4

# Output:
# 36

# ==========================================================

# Example:

# Input:
# 6
# 2

# Output:
# 4

#Solution: 

number_1 = float(input("Enter the first number:"))
number_2 = float(input("Enter the second number:"))

if(number_1 > number_2):
    print(number_1 - number_2)
else:
    print(number_2 - number_1)