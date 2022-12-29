# Write Python code of a program that reads a student’s mark for a single subject, and prints out the corresponding grade for that mark. The mark ranges and corresponding grades are shown in the table below. You need to make sure that the marks are valid. For example, a student cannot receive -5 or 110. So the valid marks range is 0 to 100.

# hint(1): You can consider the number to be an integer

# hint(2): This problem can be solved in two ways: top-down (starts from A) and bottom-up (starts from F)

# Marks	Grage
# 90 or above	A
# 80-89	B
# 70-79	C
# 60-69	D
# 50-59	E
# Below 50	F

# Solution:
mark =int(input("Enter the mark:"))

if(0 <= mark <=100):
    if(mark <= 49):
        print("F")
    elif(mark <= 59):
        print("E")
    elif(60 <= mark <= 69):
        print("D")
    elif(70 <= mark <= 79):
        print("C")
    elif(80 <= mark <= 89):
        print("B")
    elif(90 <= mark):
        print("A")
    else:
        print("out of range")
else:
    print("Invalid")  
