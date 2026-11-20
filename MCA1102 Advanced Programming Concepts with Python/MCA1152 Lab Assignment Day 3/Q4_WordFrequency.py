# Write Python scripts to: 4. Use a dictionary to count the frequency of words in an input string. Only words should be 
# counted, not blank spaces, numbers, or punctuation. Upper case should be considered the 
# same as lower case. 
# Sample 
# Input: Fear leads to anger; Anger leads to hatred; Hatred leads to conflict; 
# Conflict leads to suffering. 
# Output: {'fear': 1, 'leads': 4, 'to': 4, 'anger': 2, 'hatred': 2, 'conflict': 2, 'suffering': 1}

import string

# input string
s1 = input("Enter a string: ")

# Upper case should be considered the same as lower case. 
small_s2 = s1.lower()

words = small_s2.split()

wordsWithoutPunctuationList = []

# Only words should be counted, not blank spaces, numbers, or punctuation.
# Remove punctuation
for i in words:
    wordsWithoutPunctuation = i.strip(string.punctuation)
    wordsWithoutPunctuationList.append(wordsWithoutPunctuation)

# Use a dictionary to count the frequency of words in an input string
frequency = {}

for i in wordsWithoutPunctuationList:
    if i in frequency:
        frequency[i] = frequency[i] + 1
    else: # if the word is not in the dictionary and first time appeared in dictionary +1 or assign it 1
        frequency[i] = 1

print(frequency)