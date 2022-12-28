# Write Python code of a program that reads a number, and prints "The number is even" or "The number is odd", depending on whether the number is even or odd.

# hint(1): use the modulus (%) operator

# hint(2): You can consider the number to be an integer

# ==========================================================

# Example:

# Input:
# 5

# Output:
# The number is odd

# ==========================================================

# Example:

# Input:
# -44

# Output:
# The number is even

#Solution:

number = int(input("Enter the number:"))

if(number % 2 ==0):
    print("The number is even")
else:
    print("The number is odd")