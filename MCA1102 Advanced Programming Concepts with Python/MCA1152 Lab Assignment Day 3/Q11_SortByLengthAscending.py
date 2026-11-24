# 11. Sort a list of words first by their length, smallest to largest, and then alphabetically to break 
# ties among words of the same length (using sorted() and lambda).  
# Sample  
# Input: ['mtech', 'btech', 'mca', 'dsc', 'diploma', 'bca'] 
# Output: ['bca', 'dsc', 'mca', 'btech', 'mtech', 'diploma']

courses = ['mtech', 'btech', 'mca', 'dsc', 'diploma', 'bca']

# x is there because of tie-breaking. x is there to sort alphabetically when length same 
sorted_courses = sorted(courses, key= lambda x: (len(x), x))

print(sorted_courses)