'''
Dictionary is an unorderedand Changeable collection of data values that holds  key values pairs in Python
 dictionaries are defined within curly brackets with each  item being a pair in the form of a key : value
Dictionary is beneficial if you need to store elements in the form of key value pair of some or different data type 
Dictionary are mutable data type so we can modify its items
Dictionary is a data type like integer ,complex value ,list, string, tuple,float ,boolean values Etc where some specific values exist for some particularly key
The dictionary is defined into 2 elements - keys and values
Key must be a single element
Value can be any type such as integer ,list, float, tuple Etc
Dictionary is a key value pairs. It is similer to associative arrays in other programming languages. 
Creating the dictionary
dictionary can be created by using multiple key value Pairs enclosed with the curly brackets and each key Is separated from its value by the colon (:)
syntax 
dictionary_name=
{
"key":value1,
key:value2
}
Properties of dictionary
values
Dictionary values have no restriction
Make an be any artibitiary Python object either standard object or user defined object.
keys
More than one entry per key is not allowed
When duplicate keys encountered during assignment the last assignment wins
 Keys must be immutable -
string number or tuples can be considered as dictionary keys but something like square bracket ["keys"] is not allowed
'dict' object is not callable
the keys must be unique for identification
Dictionaries are optimized to get values when the key is known
'''
introduction={"first_name":"Sumanta","last_name":"Bhattacharya","age":18,"12thmarks":69.8,"10th":52.6}
print(introduction)
x=introduction["first_name"]
print("my father given name is",x)

print(introduction["12thmarks"])

print(introduction.get("last_name"))#same method accessing value
print(introduction.get("hobbies"),["writting","walking"])

a=introduction["first_name"]="sudip"#update
print(a)

print(type(introduction))
print(id(introduction))
print(len(introduction))
print(dir(introduction))


introduction["language"]="python","java"#Adding new items to a dictionary
print(introduction)

introduction.pop("first_name")#The pop function requires an argument in dictionary but pop function requires no argument in list This is the difference between pop function of list and dictionary.pop delete the specific item in dictionary but when we use pop function in list It deletes the last item inside the brackets:to delete the specific item in list we use remove ()function
print(introduction)

for key in introduction:
    print(key)
    print(introduction[key])

    



