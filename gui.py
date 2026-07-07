import operations
import FreeSimpleGUI as gui

gui.theme('DarkBlue')

label = gui.Text("Type in a TODO: ")
input_box = gui.InputText(tooltip = "enter todo", key="todo")
add_button = gui.Button("Add")
edit_button = gui.Button("Edit")
list_box = gui.Listbox(values=operations.get_todos(), key="todo_items", enable_events=True, size=(45, 10))
complete_button = gui.Button("Complete", key="complete")

window = gui.Window("My to-do App",
                    layout=[[label, input_box,add_button],
                            [list_box, edit_button],
                            [complete_button]],
                    font=('Helvetica', 16))
while True:
    event, values = window.read()
    match str(event).lower():
        case "add":
            todos = operations.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            operations.put_todos(todos)

            new_existing_todos = operations.get_todos()
            window['todo_items'].update(values=new_existing_todos)
        case "todo_items":
            window['todo'].update(value=values["todo_items"][0])
        case "edit":
            try:
                existing_todos = operations.get_todos()
                new_todo = values["todo"] + "\n"
                old_todo_to_edit = values["todo_items"][0]

                if old_todo_to_edit in existing_todos:
                    old_index = existing_todos.index(old_todo_to_edit)
                    existing_todos[old_index] = new_todo

                operations.put_todos(existing_todos)
                window['todo'].update('')

                new_existing_todos = operations.get_todos()
                window['todo_items'].update(values=new_existing_todos)
            except IndexError:
                gui.popup_error("Please select an item first")

        case "complete":
            try:
                existing_todos = operations.get_todos()
                completed_todo = values["todo"]
                if completed_todo in existing_todos:
                    existing_todos.remove(completed_todo)

                operations.put_todos(existing_todos)
                window['todo'].update('')

                new_existing_todos = operations.get_todos()
                window['todo_items'].update(values=new_existing_todos)
            except IndexError:
                gui.popup("Please select an item first")

        case WINDOW_CLOSED:
            break

window.close()