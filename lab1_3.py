print("Insert the number corresponding to the action you want to perform:\n")

a = 0
myList = []

while(a != 4):

    print("1. insert a new task")
    print("2. remove a task")
    print("3. show all the tasks")
    print("4. close the program")

    a = int(input())

    if(a == 1):
        print("Enter the task to insert:")
        task = input()
        myList.append(task)

    if(a == 2):
        print("Enter the task to remove:")
        task = input()
        myList.remove(task)

    if(a == 3):
        print("My todo list:\n")
        print(myList)


