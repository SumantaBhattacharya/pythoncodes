# Write Python scripts to: 1. Accept  a  list  of  tuples,  
# where  each  tuple  contains  two  elements,  and  convert  it  into  a 
# dictionary, using the first element of each tuple as the key and the second as the value.

# 1. Accept  a  list  of  tuples
# where  each  tuple  contains  two  elements
listOfTuples = [("name", "SUMANTA BHATTACHARYA"),("roll no", 2682005), ("course", "Master of Computer Applications")]

# convert  it  into  a dictionary, 
# using the first element of each tuple as the key and the second as the value.
dicts = dict(listOfTuples)

print(dicts)