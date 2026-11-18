# Write  a  Python  script  that  prompts  the  user  to  input  a  year  and  determine  whether 
# that year is a leap year or not.

# Check if the year is divisible by 100 
#     i. if yes divide the year with 400 
#     ii. if its fails to be divisible by 100 
#     ii.i then check if its divisible by 4

year = int(input("Enter a year: "))

if(year % 100 == 0):
    if(year % 400 == 0):
        print("Leap year")
    else:
        print("Not a leap year")
else:
    if(year % 4 == 0):
        print("Leap year")
    else:
        print("Not a leap year")