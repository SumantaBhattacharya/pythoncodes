def frequency(array,element):
    count = 0
    for i in array:
       
        if i == element:
            count=count+1# # Increment count for each match
             # Return the total count after counting all occurrences
    return count #just return also works
array=[7,9,4,7,7,7]
element=7
result=frequency(array,element)
print(f"the element {element} appears {result} times in array")

