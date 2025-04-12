#A set is a unordered collection of items, cannot contain duplicate items and these items are not in any perticular order, we can only use immutable objects in sets. set items dont have any indexes,sets are mutable
animals={"cat","dog","bull","sheep","cow"}
print(animals)
pet=set()
print(pet)

print(type(animals))
print(len(animals))
print(dir(animals))
print(id(animals))


wild_animals=["tiger","lion","hippopotamus","monkey","snake"]#convert
print(set(wild_animals))#we can convert other iterables like tuples, dictionaries and string into a set in a similer way. we can also add all the elements of iterables like tuples , list and string to a set

animals.add("geraph")
print(animals)

domestic_animals={"goat","pig","rabbit","duck","hamster","snake"}
animals.update(domestic_animals)
print(animals)
animals.update(domestic_animals,{"donkey"})
print(animals)
animals.discard("bull")
print(animals)
#if the items we are trying to remove is not in the set, discard returns none where as the remove method throws an error
# the remove function works in both list and set 
animals.remove("sheep")
print(animals)#set.remove() takes exactly one argument (0 given)


print("cow" not in animals)
print("cow" in animals)
# the keyword 'in' is used list, string and sets 
 

for char in animals:
    print( animals)

a = animals.union(wild_animals)
print(a)
an = animals | domestic_animals#unsupported operand type(s) for |: 'set' and 'list'
print(an)

animal = animals.intersection(wild_animals)
print(animal)

ani = animal & domestic_animals
print(ani)


animals.clear()
print(animals)