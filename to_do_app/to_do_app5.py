# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 17:24:52 2024

@author: master
"""
todos = []

while True:
    user_action = input("Type add, show, edit, delete or exit: \n")
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: \n")
            todos.append(todo)
        case 'show':
            for index, i in enumerate(todos):
                i = i.title()
                row = f"{index+1}: {i}"
                print(row)
        case 'edit':
            number = int(input("Enter the number of your todo to edit: \n"))
            number = number - 1
            new_todo = input("Enter a todo: \n")
            todos[number]=new_todo
        case 'delete':
            number = int(input("Enter the number of your todo: \n"))
            todos.pop(number-1)
        case 'exit':
            break
        case _:
            print("Enter the correct value. \n")
print("Bye!")
