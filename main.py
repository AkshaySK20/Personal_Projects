todos = []
i=2
while True:
    user_action = input("Do you want to add, show, edit, complete or exit?: ")
    user_action = user_action.strip()

    match user_action:

        case "add":
            to_do = input("Enter the todo: ") + "\n"

            with open("To-do file.txt", 'r') as file:
                todos = file.readlines()

            todos.append(to_do)

            with open("To-Do file.txt", 'w') as file:
                file.writelines(todos)

        case "show":
            with open("To-Do file.txt", 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index+1}.{item}"
                print(row)

        case "edit":
            print('Here is the existing To-Dos:')
            with open('To-Do file.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}.{item}"
                print(row)

            num = int(input("Enter the todo index number you want to edit: "))

            new_todo = input("Please enter the new todo: ")
            todos[num-1] = new_todo
            print(f"Here is the new list of todos")
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}.{item}"
                print(row)


        # we have an inbuilt method of list __setitem__ which can be used to replace the object in the list. Eg:
        # todos.__setitem__(1, "Study") would mean the index 1 in the list will be replaced by "study" You can
        # find all the methods of list by executing - dir(list), __xxxxx__ are internal methods that the python uses generally
        case "complete":
            with open('To-Do file.txt', 'r') as file:
                todos = file.readlines()

            Number = int(input("Please enter the number of the todo to mark it completed: "))
            todos.pop(Number - 1)

            with open("To-Do file.txt", 'w') as file:
                file.writelines(todos)

            print('Here is the existing To-Do list:')
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}.{item}"
                print(row)

        case "exit":
            break

        case _:
            print("Hey, you entered an unknown command!")

print("ok bye!")
