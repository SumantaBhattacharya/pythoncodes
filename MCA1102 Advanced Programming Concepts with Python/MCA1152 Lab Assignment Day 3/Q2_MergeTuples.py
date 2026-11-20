# Write Python scripts to: 2. Merge multiple tuples into a single tuple without duplicates, maintaining the original order 
# of elements. 

t1 = ("SUMANTA BHATTACHARYA"), (2682005), ("Master of Computer Applications")
t2 = (34), (2682005), (12626010055)

# Merge multiple tuples into a single tuple
t3 = t1 + t2

# immutable objects cannot change its state or contents
# immutable datatypes are i. tuple (tuple is a ordered sequence of items same as list. it is defined within parenthesisit that is circular brackets () where items are separated by commas, a tuple is used to store multiple items in a single variable. it doesnt support changing its value (tuple object does not support item assignment))
# the differences between list and tuple is that their parenthesis are different list use square bracket and tuple use circular bracket and tuple is immutable and list is mutable
# an index represents the positoned number of tuples elements .the index starts from 0-1

# A list to remove the duplicates as tuples are immutabe
l1 = [] #list does not change its order

for i in t3:
    if i not in l1:
        l1.append(i)

# now convert back to tuple
t4 = tuple(l1)

print(t4)