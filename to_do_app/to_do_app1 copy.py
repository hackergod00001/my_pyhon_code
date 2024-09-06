# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 17:24:52 2024

@author: master
"""
while True:
    user_action = input("Type add, show, edit, delete or exit: \n")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo:" ) + "\n"
            
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
            new_todos = []
            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)
            # print(todos)
            for index, i in enumerate(new_item): #todos):
                i = i.title()
                row = f"{index+1}: {i}"
                print(row)
        case 'edit':
            number = int(input("Enter the number of your todo to edit: \n"))
            number = number - 1
            new_todo = input("Enter a todo: ")+ "\n"
            todos[number] = new_todo
        case 'delete':
            number = int(input("Enter the number of your todo: \n"))
            todos.pop(number-1)
        case 'exit':
            break
        case _:
            print("Enter the correct value. \n")
print("Bye!")

#%%
while True:
    user_action = input("Type add, show, edit, delete or exit: \n")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo:" ) + "\n"
            
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
            new_todos = [item.strip('\n') for item in todos]
            # print(todos)
            for index, i in enumerate(new_todos): #new_item): #todos):
                i = i.title()
                row = f"{index+1}: {i}"
                print(row)
        case 'edit':
            number = int(input("Enter the number of your todo to edit: \n"))
            number = number - 1
            new_todo = input("Enter a todo: ")+ "\n"
            todos[number] = new_todo
        case 'delete':
            number = int(input("Enter the number of your todo: \n"))
            todos.pop(number-1)
        case 'exit':
            break
        case _:
            print("Enter the correct value. \n")
print("Bye!")

#%%
while True:
    user_action = input("Type add, show, edit, delete or exit: \n")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo:" ) + "\n"
            
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
            #new_todos = [item.strip('\n') for item in todos]
            # print(todos)
            for index, i in enumerate(todos): #new_todos): #new_item): #todos):
                i = i.strip('\n')
                i = i.title()
                row = f"{index+1}: {i}"
                print(row)
        case 'edit':
            number = int(input("Enter the number of your todo to edit: \n"))
            number = number - 1
            new_todo = input("Enter a todo: ")+ "\n"
            todos[number] = new_todo
        case 'delete':
            number = int(input("Enter the number of your todo: \n"))
            todos.pop(number-1)
        case 'exit':
            break
        case _:
            print("Enter the correct value. \n")
print("Bye!")

#%%
while True:
    user_action = input("Type add, show, edit, delete or exit: \n")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo:" ) + "\n"
            
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            todos.append(todo)
            
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            #new_todos = [item.strip('\n') for item in todos]
            # print(todos)
            for index, i in enumerate(todos): #new_todos): #new_item): #todos):
                i = i.strip('\n')
                i = i.title()
                row = f"{index+1}: {i}"
                print(row)
        case 'edit':
            number = int(input("Enter the number of your todo to edit: \n"))
            number = number - 1
            new_todo = input("Enter a todo: ")+ "\n"
            todos[number] = new_todo
        case 'delete':
            number = int(input("Enter the number of your todo: \n"))
            todos.pop(number-1)
        case 'exit':
            break
        case _:
            print("Enter the correct value. \n")
print("Bye!")

#%%