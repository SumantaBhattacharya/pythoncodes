# 14. Sort a list of names alphabetically by last name. 
# Sample Input: ['Han Kang', 'Geoffrey Hinton', 'John Hopfield', 'Nihon Hidankyo']  
# Output: ['Nihon Hidankyo', 'Geoffrey Hinton', 'John Hopfield', 'Han Kang']

def get_lastName(name):
    words = name.split()
    return words[-1]

names = ['Han Kang', 'Geoffrey Hinton', 'John Hopfield', 'Nihon Hidankyo']

sorted_names = sorted(names, key=get_lastName)

print(sorted_names)