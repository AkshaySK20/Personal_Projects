todos = []

while True:
    user_action = input("Do you want to add, show or exit: ")

    match user_action:
        case "add":
            to_do = input("Enter the todo: ")
            todos.append(to_do)
        case "show":
            # enumerate will grab the index from the list
            for index, item in enumerate(todos):
                print(f"{index + 1}-{item}")
        # The first character of the word will be capital letter -> .title()
        # item = item.title()
        # print(item)
        case "edit":
            num = int(input("Enter the todo index number you want to edit: "))
            exist_todo = todos[num - 1]
            new_todo = input("Please enter the new todo: ")
            todos[num - 1] = new_todo
            print(f"Here is the new list of todos {todos}")
        # we have an inbuilt method of list __setitem__ which can be used to replace the object in the list. Eg:
        # todos.__setitem__(1, "Study") would mean the index 1 in the list will be replaced by "study" You can
        # find all the methods of list by executing - dir(list), __xxxxx__ are internal methods that the python uses generally
        case "complete":
            Number = int(input("Please enter the number of the todo to mark it completed: "))
            todos.pop(Number - 1)

        case "exit":
            break

        case _:
            print("Hey, you entered an unknown command!")

print("ok bye!")
