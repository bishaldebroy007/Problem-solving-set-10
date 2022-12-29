# Write Python code of a program to compute and display a person’s weekly salary as determined by the following conditions: If the hours worked are less than or equal to 40, the person receives Tk200.00 per hour, else the person receives Tk8000.00 plus Tk300.00 for each hour worked over 40 hours. The program should request the hours worked as input and should display the salary as output.

# ==========================================================

# hint: You can consider the hour(the user input) to be an integer

# ==========================================================

# Example1:
# Input: 100
# Output: 26000

# ==========================================================

# Example2:
# Input: 30
# Output: 6000

#Solution:
hours = int(input("Enter the working duration in hour:"))

ver_1 =hours * 200
ver_2 =(hours-40)
if(1 <= hours <= 40):
    print(ver_1)
elif(hours > 40):
    print(8000+(ver_2)*300)
else:
    print("Invalid")
