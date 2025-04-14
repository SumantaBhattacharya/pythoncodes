def addition(num1, num2):
    result = num1 + num2
    print("{0} + {1} = {2}".format(num1, num2, result))


def substraction(num1, num2):
    result = num1 - num2
    print("{0} - {1} = {2}".format(num1, num2, result))


def multiplication(num1, num2):
    result = num1 * num2
    print("{0} * {1} = {2}".format(num1, num2, result))


def division(num1, num2):
    if num2 == 0.0:
        print("cannot do divide by zero")
    else:
        result = num1 // num2  # 15/0
        print("{0} / {1} = {2}".format(num1, num2, result))


while True:
    print("+--------------------------------------------------------------------+")
    print("|1|\t\t\t"+"  For  "+"|"+"\t"+"Addition"+"                     "+"|")
    print("|2|\t\t\t"+"  For  "+"|"+"\t"+"Substraction"+"                 "+"|")
    print("|3|\t\t\t"+"  For  "+"|"+"\t"+"Multiplication"+"               "+"|")
    print("|4|\t\t\t"+"  For  "+"|"+"\t"+"Division"+"                     "+"|")
    print("press 'q' or 'Q' to stop the calculating process")
    print("+--------------------------------------------------------------------+")

    choice = (input("Enter your coice:"))
    if choice=='q' or choice == 'Q':
          break
    
    


    
    num1 = float(input("Enter any number of your chioce:"))
    num2 = float(input("Enter any secondnumber of your chioce:"))

    if choice == 1:
            result = addition(num1, num2)
    elif choice == 2:
            result = substraction(num1, num2)
    elif choice == 3:
            result = multiplication(num1, num2)
    elif choice == 4:
            result = division(num1, num2)
    else:
            print("|5|", "Invalid")

