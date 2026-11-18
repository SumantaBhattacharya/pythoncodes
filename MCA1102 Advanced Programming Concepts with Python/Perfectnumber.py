# 6. Write  a  Python  script  that  accepts  a  positive  integer  from  a  user,  and  checks  whether 
# that  number  is  a  Perfect  number  or  not.  [A  perfect  number  is  a  positive  integer  that  is 
# equal to the sum of its proper divisors e.g. 6, 28, 496, 8128, ...]  
# 6 has proper divisors: 1, 2, 3
# 1 + 2 + 3 = 6

num = int(input("Enter a positive integer: "))
if (num > 0):

    i = 1
    sum_of_proper_divisors = 0

    # find out the divisors
    while(i < num):
        if(num % i == 0):
            sum_of_proper_divisors = sum_of_proper_divisors + i
        i = i + 1

    if(sum_of_proper_divisors == num):
        print("Perfect number")
    else:
        print("Not a Perfect number")