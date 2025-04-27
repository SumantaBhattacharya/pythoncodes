Queue = []


def enqueue():
    e = input(
        "Enter the element you want to add in the queue which works in the FIFO order:- ")
    Queue.append(e)
    print(e + " is added in the queue ")


def dequeue():
    if not Queue:
        print("Queue is empty")
    else:
        el = Queue.pop(0)
        print("removed elememt from the queue is:", el)


def display():
    print(Queue)


while True:
    choice = int(
        input(
            "Select the operation you want to perform on the queue: 1. ADDITION 2. REMOVAL 3. SHOW 4. QUIT: ")
    )

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")
