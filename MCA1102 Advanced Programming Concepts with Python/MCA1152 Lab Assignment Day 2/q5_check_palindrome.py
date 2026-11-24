# 5. Check if a string is palindrome or not.  
# Sample 
# Input                             Output 
# noon                              Palindrome 
# Radar                             Palindrome
# A12  21a                          Palindrome
# Was it a car or a cat I saw       Palindrome
# A man, a plan, a canal: Panama!   Palindrome
# Students of MCA                   Not Palindrome

# Forward: amanaplanacanalpanama
# Backward: amanaplanacanalpanama

import string

sentence = input("A man, a plan, a canal: Panama!")

words = sentence.split()

wordsWithoutPunctuationList = []

for i in words:
    # remove punctuation from every word such as "man," "a plan," "a canal:" "Panama!"
    wordsWithoutPunctuation = i.strip(string.punctuation).lower()
    wordsWithoutPunctuationList.append(wordsWithoutPunctuation)

reversedSentence = wordsWithoutPunctuationList[::-1]

if(sentence == reversedSentence):
    print("Palindrome")