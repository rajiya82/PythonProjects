import FreeSimpleGUI as gui
import Ex1_functions as func

label1 = gui.Text("Enter feet")
input_box1 = gui.InputText(tooltip = "Enter feet", key="feets")

label2 = gui.Text("Enter inches")
input_box2 = gui.InputText(tooltip = "Enter inches", key="inches")

output_label = gui.Text(key="output")

button = gui.Button("Convert")

layout = [[label1, input_box1], [label2, input_box2], [button, output_label]]
window = gui.Window("Convert", layout=layout)

event, values = window.read()
print(f"Event: {event}")
print(f"Values: {values}")

feets = float(values["feets"])
inches = float(values["inches"])

values_in_meters = func.calculate_meeter(feets, inches)

window["output"].update(value=f"Meeter value is: {values_in_meters}")

window.read()
window.close()
