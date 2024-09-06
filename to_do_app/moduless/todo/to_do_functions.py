# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:07:18 2024

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

#print(help(get_todos))

def write_todos(filepath, todos_arg):
    """
    This function writes the file and gets all the lines present inisde that file form the list.


    Parameters
    ----------
    filepath : TYPE
        DESCRIPTION.
    todos_arg : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)