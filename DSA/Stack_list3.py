Stack = []
n=(int(input("Enter a Fixed size of the stack:")))

def push():
    if (len(Stack) == n):
        print("Stack is full")
    else:
        element = input("enter the element:")
        Stack.append(element)
        print(Stack)

def pop():
    if Stack is None:
        print(Stack,"The stack is empty")
    else:
        e=Stack.pop()
        print(Stack,"The deleted element is ",e)

while True:
        print("Select The Operation You want to Perform In the Stack")
        print("1.ADDITION")
        print("2.REMOVEL")
        print("YOU NEITHER WANT TO DO ANY OF THOSE, OKAY.TO GET OUT OF THE PROGRAM PRESS 3.YOU CAN GET BACK TO US AGAIN SOON BYE!")
        choose=(int(input("Enter the number of operation shown on the screen:")))
        if choose == 1:
            el=push()
            print("Congrats! You have added a element Into the Stack",el,end="")
        elif(choose == 2):
            ele=pop()
            print("Congrats! You have deleted a element from the Stack",ele)
        elif(choose == 3):
            break
        else:
            print("ERROR! MAYBE WRONG INPUT","PLEASE TRY AGAIN SOMETIME SOON")
