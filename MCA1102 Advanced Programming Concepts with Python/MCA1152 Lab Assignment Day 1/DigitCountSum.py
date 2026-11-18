# 2. Write a Python script that accepts a non-negative integer from a user, and prints the
# number of digits in the integer and also the sum of the digits of the integer.

user_input = int(input("Enter a non-negative integer: "))

# Check if the input is a non-negative integer (Greater than or equal to zero.)
if user_input >= 0:

    if user_input == 0:
        print("Number of digits: 1")
        print("Sum of digits: 0")

    if user_input != 0:  # user_input > 0
        # sum of digits
        digit_sum = 0

        count = 0

        while user_input > 0:  # loop until the user_input becomes 0 its a condition
            # each time the loop runs, count it
            count = count + 1

            digit = user_input % 10  # Get the last digit
            digit_sum = digit_sum + digit
            user_input //= 10  # Remove the last digit

        print("Number of digits:", count)
        print("Sum of digits:", digit_sum)
