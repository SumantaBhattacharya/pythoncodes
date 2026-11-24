# 10. Sort a list of numbers based on their absolute values, writing your own function for 
# calculating absolute value of a number and (i) using it in sorted( ) without lambda, (ii) using 
# sorted( ) with lambda. 
# Sample 
# Input: [-5, -7, 4, -2, -9] 
# Output: [-2, 4, -5, -7, -9]

# Absolute value means ignoring the sign.

def get_absVal(n):
    if (n < 0):
        return -n
    return n

nums = [-5, -7, 4, -2, -9]

# .sort modifies the existing list
# Works only on lists (list.sort() is a list method).
# nums.sort(key=get_absVal)

# Works on any iterable (lists, tuples, strings, sets, dictionaries, generators) and always returns a list.
sorted_without_lambda = sorted(nums, key=get_absVal)

sorted_lambda = sorted(nums, key = lambda x: -x if x < 0 else x)

print(sorted_without_lambda)

print(sorted_lambda)