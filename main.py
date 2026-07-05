from typing import List

todos = []
while True:
    what_to_do = input("What do you want to do? (Please enter only add/edit/show/exit)")
    what_to_do = what_to_do.strip()

    if what_to_do.startswith("add"):
        with open("todos.txt","r") as file:
            todos = file.readlines()

        for item in todos:
            if str(item).lower() == str(what_to_do[4:]).lower():
                print("This TODO already exists.")
            break

        todos.append(f"{what_to_do[4:]}\n")

        with open("todos.txt","w") as file:
            file.writelines(todos)

    elif what_to_do.startswith("show"):
        with open("todos.txt","r") as file:
            todos = file.readlines()
        if len(todos) == 0:
            print("No TODOs found.")
        else:
            for index, item in enumerate(todos, start=1):
                print(f"{index} - {item.strip("\n")}")

    elif what_to_do.startswith("edit"):
        with open("todos.txt","r") as file:
            todos = file.readlines()

        if len(todos) == 0:
            print("No TODOs found.")
        else:
            index = 1
            print("Here are the existing TODOs")
            for item in todos:
                print(str(index) + " - " + item.capitalize().strip())
                index += 1

            index_to_edit = int(input("Enter the index of the item that you want to edit: "))
            index_to_edit = index_to_edit - 1
            new_todo = input("Enter the new TODO: ")
            todos[index_to_edit] = f"{new_todo} \n"

        with open("todos.txt","w") as file:
            file.writelines(todos)
    elif what_to_do.startswith("complete"):
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        if len(todos) > 0:
            print("Here are the available TODOs:")
            for index, item in enumerate(todos, start=1):
                print(f"{index} - {item.capitalize().strip()}")

            completed_index = 0

            try:
                completed_index = int(input("Which one has completed? (please enter the index)"))
                if 0 < completed_index & completed_index <= len(todos):
                    completed_index = completed_index - 1
                    removed_value = todos[completed_index]

                    with open("todos.txt","w") as file:
                        todos.pop(completed_index)
                        file.writelines(todos)
                        print(f"TODO {removed_value.strip()} removed from the list.")
                else:
                    print("Please enter a valid number")
            except Exception as e:
                print("Please enter a valid number")
        else:
            print("No TODOs found.")
    else:
        print("Invalid input.")