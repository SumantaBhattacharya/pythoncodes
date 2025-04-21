def Search(lst, key):
    key = int(key)  # Convert input to integer
    for i in range(len(lst)):
        if key == lst[i]:
            print("Key element is found at index " + str(i))
            break
    else:
        print("Key element is not found")

lst = [68, 69, 77, 99, 104, 420]
while(True):
    key = input("Enter the Key element you want to compare with the list:")
    Search(lst, key)


'''
It appears there might be an issue with the comparison. The input from the user is treated as a string,
 while the elements in the list are integers.
 Therefore, the comparison if key == lst[i]: might not work as expected.'''
'''So to search a list, we need list as well as we need key,
 right? That's why these two parametersAnd here I will take the for loop first,
   because we need to cheque the key element with the each element of the list,
     right? We need to compare this key with first 10 seven, four, one, nineteen,
       two, three hundred. We need to compare with each element of the list.
         That's why I take a follow,
           and I'll take rain from zero to length of list 1 because here length of list 1 is 7.
             So length of list 1 is nothing but7OK. So range will become zero7. So we'll get 012345 and 6.
               Ok, this index. So here I will take for loopLength of this one S. I just mentioned length of list one
               . There is nothing, but it will take range from zero to length of list 1. Alright. Next, I need to come'''