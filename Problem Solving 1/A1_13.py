# hint(1): The user input will be an integer value

# hint(2): 1 hour = 60 mins = 3600 seconds
# 1min = 60 seconds

# ==========================================================

# Example01:
# Input: 10000
# Output: Hours: 2 Minutes: 46 Seconds: 40

# ==========================================================

# Example02:
# Input: 500
# Output: Hours: 0 Minutes: 8 Seconds: 20

#Solution:
value = int(input("Enter seconds:"))

var_hour =(value//3600)
var_min =((value-(var_hour*3600))//60)
var_sec =(value-(var_hour*3600)-(var_min*60))
print("Hours:",var_hour,end=" ")
print("Minutes:",var_min,end=" ")
print("Seconds:",var_sec,end=" ")
