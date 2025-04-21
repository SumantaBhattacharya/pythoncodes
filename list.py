''' a list is used to store multiple items in a single variable 
The list has following characteristics or features
 The list is an ordered collection or sequence of items 
 it is defined within parenthesis i.e circular bracket
 items are seperated by commas
 the size of a empty list is zero(0)
 
 The elements of the list can access by index
   The list are the mutable data type
     A list can store the number of various elements
     list=array
     list=[] empty list
     There are two types of data types mutable and immutable
     mutable objects can change its states or contents
     immutable objects cannot 
     mutable datatypes are
     1 list 
     2 dictionary 
       immutable datatypes are
       1 tuple 
       2 sets
      3 string
       4 complex
       5 float
       6 int'''
language=["cprogram","c++","javascript","html(hypertext markup language)","php"]
programminglanguage=["dart","kotlin","swift"]

print(language)
print(language[0])
print(language[1])
print(language[-2])
print (language[3:5])#when we perform slicing the end input is not included
print (language[:])# its just prints all elements of the list, the start index is 0 which is dafault
print (language[:2])


language[2:4]="sql","haskell"#upgrade
print ( language)


print(type(language))
print(id(language))#In python every object has an indentity. the id of an object is always unique and constant for this object during its lifetime  
print(len(language))
print(dir(language))#we can list out all the attributes and methods of a given object using the dir () function 





language.extend("python")#list.append() takes exactly one argument
print ( language)
language.append("css")#list.extend() takes exactly one argument 
print ( language)
language.insert(2,"java")#insert expected 2 arguments we can incer one item as desired location by using incert method
print ( language)
language.pop()#romoves the last item
print(language)
language.remove("java")#list.remove() takes exactly one argument  remove() method romoves the specified item
print(language)

language.extend(programminglanguage)#conctenate
print(language)
languages=language.copy()
print(languages)

print("c++" in language)#membership operator
print("javascript" not in language)
print( programminglanguage is language)
print( programminglanguage is not language)

language.sort()# this sort() fucntion help to order the elements in alphabetical form ot if the elements are number then it orders the elements sequencially
print(language)
language.reverse() # the reverse() fucntion as its name suggests it reverse the elements of the list
print(language)

languages=set(language)#conversion of list to set
print(languages)
languages=tuple(language)#conversion of list to tuple
print(languages)
languages=str(language)#conversion of list to tuple
print(languages)

r= range (3,31,3)
print(list(r))

resulted= language + ["vscode",2]
print(resulted)

resultation=language.__add__(["pascal","fortran"])
print(resultation)

for char in language:
    print("\n",language)
print(language)





print(language.index("c++"))#based on the latest or updated list it gives the output

for i in language:
    #print(i,end=" ")# the loop will stop after its reaches to the c program.
    if i=="cprogram":#cprogram was still printed. It is because the brake statement came after the print function.
        break#remove either print statement to see the result
    print(i)#Here is the difference is the first print statement iterates to c program and the second print statement stops when it touch.or reaches to dart.
#When I is equal to is equal to C program then it breaks.Before the C program, all the elements are get printed.





language.clear()
print("\n",language)





