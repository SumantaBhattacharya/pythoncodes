# 19. Give an implementation of a function called nums() that has three parameters, the first, a  
# float, is required, the second parameter multInt, an integer, is optional with a default value of 
# 10, the final parameter switch, is also optional with a default value of False. The function 
# should multiply the two integers, and if switch is True, should change the sign of the product 
# before returning it.

def nums(first, multInt = 10, switch = False):
    product = first * multInt
    if switch == True:
        product = -product
    return product

print(nums(52.6))
print(nums(52.6, 34))
print(nums(3.0, 4, True))