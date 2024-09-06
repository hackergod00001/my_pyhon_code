# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 12:16:08 2024

@author: master
"""

while True:
    user_action = input("Type add, show, edit, delete or exit: \n")
    
    match user_action:
        case 'add':
            todo = input("Enter a todo:") + "\n"
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            
            todos.append(todo)
            
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
            
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            print(todos)
            for index, i in enumerate(todos):
                i = i.strip('\n')
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