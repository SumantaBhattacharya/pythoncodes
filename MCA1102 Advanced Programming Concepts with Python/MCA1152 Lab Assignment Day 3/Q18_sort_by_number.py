# 18. Write a function that takes a list of tuples, where each tuple is an ordered pair of a string and 
# a number. Sort the list of tuples based on the numeric value in ascending order and return 
# the sorted list. 

def sort_by_number(data):
    return sorted(data, key=lambda item: item[1])

data = [("Sumanta", 52.6), ("Sudip", 69.8), ("Anita", 75.9), ("Suman", 52.6)]
result = sort_by_number(data)

print(result)