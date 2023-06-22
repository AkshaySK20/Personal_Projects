todos = []
i=2
while True:
    user_action = input("Do you want to add, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "new":
            t_in = input("Enter the new To-Do: ")
            t_adapted = "1." + t_in
            t_file = open("To-Do file", 'w')
            t_file.write(t_adapted)

        case "add":
            to_do = input("Enter the todo: ")
            t_file = open("To-Do file", 'a')
            while True:
                t_file.write(f"\n{i}.{to_do}")
                i+=1
                break

            #todos.append(to_do)
        case "show":
            t_file = open("To-Do file", 'r')
            print(t_file.read())
            # enumerate will grab the index from the list
            #for index, item in enumerate(todos):
                #print(f"{index + 1}-{item}")
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
