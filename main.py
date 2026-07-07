from typing import List
from datetime import datetime

from operations import get_todos, put_todos, update_todos

def main():
    while True:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        what_to_do = input("What do you want to do? (Please enter only add/edit/show/exit)")
        what_to_do = what_to_do.strip()

        if what_to_do.startswith("add"):
            todos = get_todos()

            for item in todos:
                if str(item).lower() == str(what_to_do[4:]).lower():
                    print("This TODO already exists.")
                break

            todos.append(f"{what_to_do[4:]}\n")
            put_todos(todos)

        elif what_to_do.startswith("show"):
            todos = get_todos()

            if len(todos) == 0:
                print("No TODOs found.")
            else:
                for index, item in enumerate(todos, start=1):
                    print(f"{index} - {item.strip("\n")}")

        elif what_to_do.startswith("edit"):
            todos = get_todos()

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

            put_todos(todos)

        elif what_to_do.startswith("complete"):
            todos = get_todos()

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
                        updated = update_todos(completed_index, todos)
                        if updated:
                            print(f"TODO {removed_value.strip()} removed from the list.")
                    else:
                        print("Please enter a valid number")
                except Exception as e:
                    print("Please enter a valid number")
            else:
                print("No TODOs found.")
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()