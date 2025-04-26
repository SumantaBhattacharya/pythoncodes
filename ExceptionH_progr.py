try:
    # Code that may cause exception
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator / denominator
    print(result)

       # Code that may cause IndexError
    my_list = [1, 2, 3]
    i = int(input("Enter the index: "))
    print(my_list[i])

except ZeroDivisionError:
    # Code to run when a ZeroDivisionError occurs
    print("Denominator cannot be zero (0), please try again.")
 
except IndexError:
    # Code to run when an IndexError occurs (e.g., index out of range)
    print("Index cannot be greater than the size of the list.")

finally:# try statements also have an optionalfinally block which is executed regardless an exception is occurs or not
    print("Always printed")


print("program ends")
