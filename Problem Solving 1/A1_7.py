
# Write Python code of a program that reads an integer, and prints the integer it is a multiple of either 2 or 5 but not both.

# For example, 2, 4, 5, 6, 8, 12, 14, 15, 16, 18, 22 …

# ==========================================================

# hint(1): use the modulus (%) operator for checking the divisibility

# hint(2): You can consider the number to be an integer

# ==========================================================

# Example01:

# Input:
# 5

# Output:
# 5

# ==========================================================

# Example02:

# Input:
# 10

# Output:
# multiple of 2 and 5 both

# ==========================================================

# Example02:

# Input:
# 44

# Output:
# 44

#Solution:

number = int(input("Enter the number:"))
if(number % 2 ==0 and number % 5 ==0):
    print("Multiple of both 2 and 5")
elif(number % 2 ==0 or number % 5 ==0):
    print(number)
else:
    print("Other")