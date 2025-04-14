
def addition(num1,num2):
     return(num1-num2)
   
def substraction(num1,num2):
    return(num1-num2)
def multiplication(num1,num2):
    return(num1*num2)
def division(num1,num2):
    return(num1//num2)
      
print("+--------------------------------------------------------------------+")
print(
        "|1|\t\t\t"
        + "  For  "
        + "|"
        + "\t"
        + "Addition"
        + "                     "
        + "|"
    )
print(
        "|2|\t\t\t"
        + "  For  "
        + "|"
        + "\t"
        + "Substraction"
        + "                 "
        + "|"
    )
print(
        "|3|\t\t\t"
        + "  For  "
        + "|"
        + "\t"
        + "Multiplication"
        + "               "
        + "|"
    )
print(
        "|4|\t\t\t"
        + "  For  "
        + "|"
        + "\t"
        + "Division"
        + "                     "
        + "|"
    )
print("+--------------------------------------------------------------------+")
choice = int(input("Enter your coice:"))
num1 = float(input("Enter any number of your chioce:"))
num2 = float(input("Enter any secondnumber of your chioce:"))

if choice == 1:
    result=addition(num1, num2)
elif choice == 2:
    result=substraction(num1, num2)
elif choice == 3:
    result=multiplication(num1, num2)
elif choice == 4:
    result=division(num1, num2)
else:
    print("|5|", "Inavalid")

print(result)
