import PySimpleGUI as sg

label = sg.Text("Enter your To-Do")
input_box = sg.InputText(tooltip="Enter ToDo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]], font=("Helvetica", 22))
window.read()
print("Hello!")
window.close()