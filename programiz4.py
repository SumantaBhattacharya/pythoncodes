#task = There is given a list froma list of number , move zero to the end of the list
list=[1,0,2,0,4,6]

for item in list :
   if item==0:
      list.remove(item)
      list.append(item)
      print(list)

print("removing the zeroes and adding the zeroes to the end",list)

