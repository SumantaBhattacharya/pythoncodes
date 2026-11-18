# 4. Write a Python script that accepts an integer from a user, and checks whether that 
# number is an Armstrong number or not. [An Armstrong number is a number that equals the sum of its digits, where each digit is raised to the power of the total number of digits. 
# e.g. 153, # 370, 371, 1634, …]   
# 153 has 3 digits:
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

# Accept input from the user
user_input = int(input("Enter an integer: "))
    
if user_input < 0:
    print("Armstrong numbers are typically non-negative integers.")
else:
    # to get the exponent we have to first count the number of digits
    num = user_input
    count = 0
    while num > 0:  # loop until the user_input becomes 0 its a condition
            count = count + 1
            num //= 10 # Remove the last digit

    nums = user_input

    sumDigits = 0
    while(nums > 0):
        digit = nums % 10# get 1, 2, 3
        expo = digit**count
        sumDigits = sumDigits + expo
        nums //= 10 # Remove the last digit

    if sumDigits == user_input:
        print(f"{user_input} is an Armstrong number.")
    else:
        print(f"{user_input} is not an Armstrong number.")