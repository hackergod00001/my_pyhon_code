# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:06:07 2024

@author: master
"""
import sys
sys.path.append('..')
from moduless.todo import to_do_functions
import time

now = time.strftime("%d %b, %Y %H:%M:%S")
print("It is: ", now)

while True:
    user_action = input("Type add, show, edit, delete or exit: \n")
    user_action = user_action.strip()
    
    if user_action.startswith("add"):
        todo = user_action[4:]
        
        todos = to_do_functions.get_todos('../text/todos.txt')
        
        todos.append(todo + '\n')
        
        to_do_functions.write_todos('../text/todos.txt', todos)
        
    elif user_action.startswith("show"):
        todos = to_do_functions.get_todos('../text/todos.txt')
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
            
            todos = to_do_functions.get_todos('../text/todos.txt')
            
            new_todo = input("Enter a todo: \n")
            todos[number]=new_todo + '\n'
            
            to_do_functions.write_todos('../text/todos.txt', todos)
        except IndexError or ValueError:
            print("Please check your input prompt as there is something wrong with your prompt.")
            continue
        
    elif user_action.startswith("delete"):
        try:
            number = int(user_action[7:])
            
            todos = to_do_functions.get_todos('../text/todos.txt')
            
            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            
            to_do_functions.write_todos('../text/todos.txt', todos)
            message = f"Todo '{todo_to_remove}' was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
        
    elif user_action.startswith("exit"):
        break
    
    else:
        print("Enter the correct value. \n")
        
    
print("Bye!")