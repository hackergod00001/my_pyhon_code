# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 17:24:52 2024

@author: master
"""
todos = []

while True:
    user_action = input("Type add, show, edit or exit: \n")
    user_action = user_action.strip() # strip removes white spaces from the input
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: \n")
            todos.append(todo)
        case 'show':
            for row in todos:
                print(row)
        case 'exit':
            break
print("Bye!")
