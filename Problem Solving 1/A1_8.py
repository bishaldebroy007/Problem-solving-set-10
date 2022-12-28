# Write Python code of a program that reads an integer, and prints the integer if it is a multiple of 2 and 5.

# ==========================================================

# For example, 10, 20, 30, 40, 50 …

# hint(1): use the modulus (%) operator for checking the divisibility

# hint(2): You can consider the number to be an integer

# ==========================================================

# Example01:

# Input:
# 5

# Output:
# Not multiple of 2 and 5 both

number = int(input("Enter the number:"))

if(number % 2 ==0 and number % 5 ==0):
    print(number)
else:
    print("Not a multiple of both 2 and 5")