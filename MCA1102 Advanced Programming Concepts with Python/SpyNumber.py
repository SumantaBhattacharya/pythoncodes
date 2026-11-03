# 3. Write a Python script that accepts a positive integer from a user, and checks whether 
# that number is a Spy number or not. [A Spy number is a positive integer where the sum of 
# its digits equals the product of its digits e.g. 123 is a Spy number since 1+2+3=6 and 1*2*3=6, 132, 1412, …]  

# Accept input from the user
user_input = int(input("Enter a positive integer: "))

# Check if the input is a positive integer (Greater than zero.)
if user_input <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize variables for sum and product of digits
    digit_sum = 0
    digit_product = 1

    num = user_input  

    while num > 0:  # loop until the user_input becomes 0 its a condition
        digit = num % 10  # Get the last digit
        digit_sum = digit_sum + digit
        digit_product = digit_product * digit  # Multiply to product
        num //= 10 # Remove the last digit

    # Check if the sum equals the product
    if digit_sum == digit_product:#we just need to compare the sum and product is equal or not thats it
        print(f"{user_input} is a Spy number.")
    else:
        print(f"{user_input} is not a Spy number.")