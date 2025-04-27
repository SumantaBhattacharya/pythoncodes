try:
    # Code that may cause exception
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator / denominator
    print(result)
except ZeroDivisionError:
    # Code to run when a ZeroDivisionError occurs
    print("Denominator cannot be zero (0), please try again.")


try:
    # Code that may cause IndexError
    my_list = [1, 2, 3]
    i = int(input("Enter the index: "))
    element = my_list[i]
    print(element)
    
except IndexError:
    # Code to run when an IndexError occurs (e.g., index out of range)
    print("Index cannot be greater than the size of the list.")

print("program ends")
