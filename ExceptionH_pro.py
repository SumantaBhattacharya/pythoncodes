try:

    language = [1, 2, 3]
    i = int(input("Enter the index: "))
    print(language[i])

except IndexError:
    # Code to run when an IndexError occurs (e.g., index out of range)
    print("Index cannot be greater than the size of the list.")

print("Program ends")
