# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:55:26 2024

@author: master
"""

def get_todos(filepath):
    """    
    This function reads the file and gets all the lines present inisde that file in form of a list.

    Parameters
    ----------
    filepath : TYPE
        DESCRIPTION: To-do's file path.

    Returns
    -------
    todos_local : TYPE
        DESCRIPTION: List that contaions all the lines present inside to-do's file in a form of list.

    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, delete or exit: \n")
    user_action = user_action.strip()
    
    if user_action.startswith("add"):
        todo = user_action[4:]
        
        todos = get_todos('../text/todos.txt')
        
        todos.append(todo + '\n')
        
        write_todos('../text/todos.txt', todos)
        
    elif user_action.startswith("show"):
        todos = get_todos('../text/todos.txt')
        new_todos = [item.strip('\n') for item in todos] #list comprehension 
        
        for index, i in enumerate(new_todos):
            i = i.strip('\n')
            i = i.title()
            row = f"{index+1}: {i}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            
            todos = get_todos('../text/todos.txt')
            
            new_todo = input("Enter a todo: \n")
            todos[number]=new_todo + '\n'
            
            write_todos('../text/todos.txt', todos)
        except IndexError or ValueError:
            print("Please check your input prompt as there is something wrong with your prompt.")
            continue
        
    elif user_action.startswith("delete"):
        try:
            number = int(user_action[7:])
            
            todos = get_todos('../text/todos.txt')
            
            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            
            write_todos('../text/todos.txt', todos)
            message = f"Todo '{todo_to_remove}' was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
        
    elif user_action.startswith("exit"):
        break
    
    else:
        print("Enter the correct value. \n")
        
    
print("Bye!")
