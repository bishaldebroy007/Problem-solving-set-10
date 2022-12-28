# Write Python code of a program that reads an integer, and prints the integer if it is a multiple of NEITHER 2 NOR 5.

# For example, 1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39 …

# ==========================================================

# hint(1): use the modulus (%) operator for checking the divisibility

# hint(2): You can consider the number to be an integer

# ==========================================================

# Example01:

# Input:
# 3

# Output:
# 3

# ==========================================================

# Example02:

# Input:
# 19

# Output:
# 19

number = int(input("Enter the number:"))

if(not(number % 2 ==0 or number % 5 ==0)):
    print(number)
else:
    print("No")