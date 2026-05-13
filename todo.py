tasks = []

while True:
    print("\n1.Add 2.View 3.Delete 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        for i, t in enumerate(tasks):
            print(i+1, t)

    elif choice == "3":
        num = int(input("Enter task number: "))
        tasks.pop(num-1)

    elif choice == "4":
        break