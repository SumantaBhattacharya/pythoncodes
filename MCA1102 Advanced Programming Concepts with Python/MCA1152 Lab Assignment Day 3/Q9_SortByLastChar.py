# 9. Write a function that takes a string as input, and returns only its last character. Use this 
# function to sort list of strings by the last character of each string, from highest to lowest. 
# Sample      
# Input: ['150', '23', '781', '19', '3478', '12', '9005', '84', '9817', '96'] 
# Output: ['19', '3478', '9817', '96', '9005', '84', '23', '12', '781', '150']

def get_lastCharacter(s):
    return s[-1]

# Use this function to sort list of strings by the last character of each string, from highest to lowest.
# sort the list in decending order by last character
# list of strings
nums = ["67", "68", "69", "143", "420"]

nums.sort(key=get_lastCharacter, reverse=True)

print(nums)