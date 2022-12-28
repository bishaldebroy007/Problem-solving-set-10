# Write Python code of a program that reads two numbers from the user. Your program should then print "First is greater" if the first number is greater, "Second is greater" if the second number is greater, and "The numbers are equal" otherwise.

# ==========================================================

# Example:

# Input:
# -4
# -4

# Output:
# The numbers are equal

# ==========================================================

# Example:

# Input:
# -40
# -4

# Output:
# Second is greater

# ==========================================================

# hint: You can consider the numbers to be floating point values
#Solution:

first_number =float(input("Enter the first number:"))
second_number =float(input("Enter the second number:"))

if(first_number > second_number):
    print("First is greater")
elif(first_number < second_number):
    print("Second is greater")
else:
    print("The numbers are equal")