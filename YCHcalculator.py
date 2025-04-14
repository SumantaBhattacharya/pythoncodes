#display
print("+--------------------------------------------------------------------+")
print("|1|\t\t\t"+"  For  "+"|"+"\t"+"Addition"+"                     "+"|")
print("|2|\t\t\t"+"  For  "+"|"+"\t"+"Substraction"+"                 "+"|")
print("|3|\t\t\t"+"  For  "+"|"+"\t"+"Multiplication"+"               "+"|")
print("|4|\t\t\t"+"  For  "+"|"+"\t"+"Division"+"                     "+"|")
print("+--------------------------------------------------------------------+")

choice=(int(input("Enter your coice:")))
num1=(float(input("Enter any number of your chioce:")))
num2=(float(input("Enter any secondnumber of your chioce:")))

if (choice==1):
    print("|1|",num1+num2)
elif(choice==2):
    print("|2|",num1-num2)
elif(choice==3):
    print("|3|",num1*num2)
elif(choice==4):
    print("|4|",num1//num2)
else:
    print("|5|","Inavalid")



    
    



        