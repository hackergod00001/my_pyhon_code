# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 12:41:57 2024

@author: master
"""

while True:
    user_action = input("Type add, show, edit, delete or exit: \n")
    
    match user_action:
        case 'add':
            todo = input("Enter a todo:") + "\n"
            
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            todos.append(todo)
            
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            
        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            new_todos = [item.strip('\n') for item in todos] #list comprehension 
           #print(new_todos)
            for index, i in enumerate(new_todos):
               #i = i.strip('\n')
                i = i.title()
                row = f"{index+1}: {i}"
                print(row)
        case 'edit':
            number = int(input("Enter the number of your todo to edit: \n"))
            number = number - 1
            
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            # print("here is a existing todo", todos)
            
            new_todo = input("Enter a todo: \n")
            todos[number]=new_todo + '\n'
        
            # print("here is a existing todo", todos)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            
        case 'delete':
            number = int(input("Enter the number of your todo: \n"))
            
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo '{todo_to_remove}' was removed from the list"
            print(message)
            
        case 'exit':
            break
        case _:
            print("Enter the correct value. \n")
print("Bye!")
