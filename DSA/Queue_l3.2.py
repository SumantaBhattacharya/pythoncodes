Queue = []

def enqueue():
    e=(input("Enter the element you want to add in the queue which works in the FIFO order:- "))
    Queue.append(e)
    print(e+ " is added in the queue ")

def dequeue():
    if(not Queue):
        print("Queue is empty")
    else:
        el = Queue.pop(0)
        print("removed elememt from the queue is:", el)

def display():
    print(Queue)

def is_empty():
    if (not Queue):
        print("Queue is empty")
    else:
        print("Queue is not empty")

def size():
    print("Size of the queue is:", len(Queue))

def peek():
    if not Queue:
        print("Queue is empty")
    else:
        print("Front element of the queue is:", Queue[0])

def clear():
    Queue.clear()
    print("Queue is cleared")

while True:
    choice=int(input("Select the operation you want to perform on the queue: 1. ADDITION 2. REMOVAL 3. SHOW 4. IS EMPTY 5. SIZE 6.PEEK 7. CLEAR  8. QUIT: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice ==4:
        is_empty()
    elif choice == 5:
        size()
    elif choice == 6:
        peek()
    elif choice == 7:
        clear()
    elif choice == 8:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")