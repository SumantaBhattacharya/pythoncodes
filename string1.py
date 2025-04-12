'''A string is basically a sequence of one or more characters enclosed in a single quotation or double quotation and triple quotation
In double quotes string we can include single quote but we cannot include double quote we can include single quote in double code string in the middle
in triple quote string we can include multiple lines string which is not possible in a single or double quotes string even we can include single or double quote in it'''

str1 = 'my name is "sumanta bhattacharya"'#single line
str2=   "\n I WOULD 'LIKE' TO THANK YOU"#single  line 
str='''\nI will be there for you
I care about my 'family' more than anything else
are "you" up for a coffe '''

print(str1,str2,str)#We cannot use the same quotation twice
print(" introduction ",str1,"proposal",str)#stream concatenate
print(str1+str2)#stream concatenate
print(str1[12])#stream indexing
print(str1[20])#stream indexing
print(str2[20:29])#stream slicin|when we perform slicing the end input is not included syntax [start:end index]
print (str1.capitalize())   #capitalize() function used to upper the first letter of the values of the chosen variable
print (str1.upper())
print (str2.lower())  

print (len(str1))
print (type(str1))
print (dir(str1))

D=str2*3
print(D)


print (str2.replace("LIKE","LOVE"))#.replace(olde string , new string )
print (str1.replace("s","S"))#Return a copy with all occurrences of substring old replaced by new.
  #count
   # Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences.
#If the optional argument count is given, only the first count occurrences are replaced.


d=(str2.find("LIKE")) #S.find(sub[, start[, end]]) -> int
#Return the lowest index in S where substring sub is found,
#such that sub is contained within S[start:end]. Optional arguments start and end are interpreted as in slice notation.
#Return -1 on failure.
print(d)

for char in str1:
    print(char)

  
print("sumanta" in str1 )  

