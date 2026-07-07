import operations
import FreeSimpleGUI as gui

label = gui.Text("Type in a TODO: ")
input_box = gui.InputText(tooltip = "enter todo")
add_button = gui.Button("Add")
delete_button = gui.Button("Delete")

window = gui.Window("My to-do App", layout=[[label, input_box],[add_button, delete_button]])
window.read()
window.close()