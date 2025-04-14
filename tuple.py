''' immutable objects cannot change its state or contents
               immutable datatypes are
       1 tuple
        tuple is a ordered sequence of items same as list 
        It is defined within parenthesisit that is circular brackets () where items are separated by commas
         a tuple is used to store multiple items in a single variable 
          the only difference between list and tuple is that their parenthesis are different list use square bracket and tuple use circular bracket
           it doesnt support changing its value (tuple object does not support item assignment)
           an index represents the positoned number of tuples elements .the index starts from 0-1
             value.sort()# this sort() fucntion help to order the elements in alphabetical form ot if the elements are number then it orders the elements sequencially
    ^^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'sort'
value.reverse() # the reverse() fucntion as its name suggests it reverse the elements of the list
    ^^^^^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'reverse'
AttributeError: 'tuple' object has no attribute 'clear'
tuple consumes less memory than list 
tuple does not have build in mathods  '''

value=(4,"program",52.6,'S',True,False)
print(value)
print(type(value))
print(len(value))
print(id(value))
print(dir(value))

print(value[1])
print(value[1:3])#when we perform slicing the end input is not included

print(value[-2])

print (value[:])# its just prints all elements of the list, the start index is 0 which is dafault
print (value[:2])

print("javascript"in value)#membership operator
print("javascript" not in value)

resultation=value.__add__(("0","Y"))
print(resultation)


for number in value:
    print(value)

 



