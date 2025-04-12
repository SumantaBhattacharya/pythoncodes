import pprint
def three(a,b,c):

 list1= [[[[0]for col1 in range(a)]for col2 in range (b)] for row in range (c)]
 list2= [[[[2]for col1 in range(a)]for col2 in range (b)] for row in range (c)]
 list=list1+list2
 return (list)

col1=2
col2=3
row=2
pprint.pprint(three(col1,col2,row))