# Question 2:

# Format input names, given as strings, as follows Sample

# Input	                    Output
# Aryadev	                Aryadev
# Rajsekhar Basu	        R. Basu
# Nabaneeta Dev Sen	        N. D. Sen
# Dawlat Wazir Bahram Khan	D. W. B. Khan

name = input("Enter a full name: ")

# split the name into words. 
# If there is only one word, we leave it alone. 
# If there are multiple words, we keep the last word as it is, 
# and convert all the other words into their first letter followed by a dot (.).

words = name.split()

# __len__() is the underlying dunder method called by len(words)
wordsLength = words.__len__()

# If the name has only one word (like "Aryadev"), print it as it is
if wordsLength == 1:
    print(words[0])
else:
    lastWord = words[-1]

    # to store first letter of the words the come before the last word
    initials = []

    #  Loop through all words except the last one
    for i in words[:-1]:
        # first letter of the word
        initials.append(i[0] + ".")

    formatted_name = " ".join(initials) + " " + lastWord

    print(formatted_name)

