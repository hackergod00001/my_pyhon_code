# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 13:26:19 2024

@author: master
"""

while True:
    user_action = input("Type add, show, edit, delete or exit: \n")
    user_action = user_action.strip()
    
    if user_action.startswith("add"): #'add' in user_action: #or 'new' in user_action: #or 'more' in user_action:
        # todo = input("Enter a todo:") + "\n"
        todo = user_action[4:]
        
        with open('../text/todos.txt', 'r') as file:
            todos = file.readlines()
        
        todos.append(todo + '\n') #bug1 fix
        
        with open('../text/todos.txt', 'w') as file:
            file.writelines(todos)
        
    elif user_action.startswith("show"): #'show' in user_action:
        with open('../text/todos.txt', 'r') as file:
            todos = file.readlines()
        new_todos = [item.strip('\n') for item in todos] #list comprehension 
       #print(new_todos)
        for index, i in enumerate(new_todos):
            i = i.strip('\n')
            i = i.title()
            row = f"{index+1}: {i}"
            print(row)
    elif user_action.startswith("edit"): #'edit' in user_action:
        try:
            number = int(user_action[5:])
            #number = int(input("Enter the number of your todo to edit: \n"))
            number = number - 1
            
            with open('../text/todos.txt', 'r') as file:
                todos = file.readlines()
            
            # print("here is a existing todo", todos)
            
            new_todo = input("Enter a todo: \n")
            todos[number]=new_todo + '\n'
        
            # print("here is a existing todo", todos)
            with open('../text/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Please check your input prompt as there is something wrong with your prompt.")
            # user_action = input("Type add, show, edit, delete or exit: \n")
            # user_action = user_action.strip()
            continue
        
    elif user_action.startswith("delete"): #'delete' in user_action:
        try:
            number = int(user_action[7:])
            #number = int(input("Enter the number of your todo: \n"))
            
            with open('../text/todos.txt', 'r') as file:
                todos = file.readlines()
            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            
            with open('../text/todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo '{todo_to_remove}' was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
        
    elif user_action.startswith("exit"): # 'exit' in user_action:
        break
    
    else:
        print("Enter the correct value. \n")
        
    
print("Bye!")
