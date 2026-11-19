# 1. Reverse the order of words in a string. 
# Sample   
# Input: dogs chase cats but cats fear dogs 
# Output: dogs fear cats but cats chase dogs 

statement = "dogs chase cats but cats fear dogs"

# to reverse the order of string we first need to split the sentence into words
words = statement.split()
# ['dogs', 'chase', 'cats', 'but', 'cats', 'fear', 'dogs']

# [::-1] is used for reverse
# reverse the order of the words 
reverse = words[::-1]
# ["dogs", "fear", "cats", "but", "cats", "chase", "dogs"]

# Join the list back into a string with spaces between the words
reversed_sentence = " ".join(reverse)

print(reversed_sentence)