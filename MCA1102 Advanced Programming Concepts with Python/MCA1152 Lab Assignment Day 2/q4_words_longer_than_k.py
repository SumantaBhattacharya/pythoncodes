# 4. Find words in a string which are greater than some given length k. 
# Sample  
# Input: "If debugging is the process of removing bugs, then programming 
# must be the process of putting them in.", k=7 
# Output: debugging, removing, programming

import string

s1 = "If debugging is the process of removing bugs, then programming must be the process of putting them in."

words = s1.split()

lettersGreaterThan7 = []

for i in words:

    # remove every word punctuation such as "in." "bugs,"
    wordsWithoutPunctuation = i.strip(string.punctuation)

    letters = wordsWithoutPunctuation.__len__()

    if(letters > 7):
        lettersGreaterThan7.append(wordsWithoutPunctuation)

WordsGreaterThan7letters = " ".join(lettersGreaterThan7)
print(WordsGreaterThan7letters)