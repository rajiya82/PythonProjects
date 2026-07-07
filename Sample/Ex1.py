import FreeSimpleGUI as gui

label1 = gui.Text("Enter feet")
input_box1 = gui.InputText(tooltip = "Enter feet")

label2 = gui.Text("Enter inches")
input_box2 = gui.InputText(tooltip = "Enter inches")

button = gui.Button("Convert")

layout = [[label1, input_box1], [label2, input_box2], [button]]
window = gui.Window("Convert", layout=layout)

window.read()
window.close()
