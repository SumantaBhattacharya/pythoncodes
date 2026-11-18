# 5. Write  a  Python  script  that  accepts  an  integer  from  a  user,  and  checks  whether  that 
# number is a Disarium number or not. [A Disarium number is a number in which the sum 
# of the digits, each raised to the power of their respective positions, is equal to the number 
# itself e.g. 89, 175, 1306, ...]

# In Python, the input() function always returns a string (text), even if the user types a number.
num = int(input("Enter a Number to check Disarium number or not: "))

if (num > 0):

    n = num
    count = 0
    # count the total number of digits
    while(n > 0): #loop until n becomes 0
        count = count + 1
        n = n // 10

    number = num
    sum_digit = 0
    while(number > 0):
        # get the last digit
        last_digit = number % 10
        expo = last_digit ** count
        sum_digit = sum_digit + expo
        count = count - 1
        number = number // 10 # remove

    if(sum_digit == num):
        print("Disarium number")
    else:
        print("Not a Disarium number")

    