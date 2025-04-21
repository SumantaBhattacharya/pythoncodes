def Search(lst, key):

    lists = []
    flag = False

    key = eval(key)  # Convert input to integer
    for i in range(len(lst)):
        if key == lst[i]:
            flag = True
            lists.append(i)
    if flag == True:
        print("Key element is found at index " + str(i))
        
        for i in lists:
            print(i)
    else:
         print("Key element is not found ")
            

lst = [68, 69, 77, 99, 104, 420,6.9,69]
while(True):
    key = input("Enter the Key element you want to compare with the list:")
    Search(lst, key)

''' I just assign a value to a variable that is to initially dispose.
 Ok, initially I took the value of category plus false. When it becomes equal,
   then I change the value of that variable to and I append that index value to this 2.
     So now that index value will be stored in this 2 and flag will be 2 if element is formed. So next,
       if flag is 2 that means the key element is formed. So to bring that index,
         I use the follow if flag is false, that means this condition is not satisfied.
           That's why flag value is still false. It doesn't become true. So that means print key is not form.
             And here I change the value. So now, if I save this and this. So now I enter 1.
               So K element is founded in this 1 and 501 2 34'''
