user_prompt = "Enter a todo: \n"  # intermediate variables

while True:
    todo = input(user_prompt)
    todos = [todo]
    print(todos)
    
#%%
user_prompt = "Enter a todo: \n"    #intermediate variables

todos = []

while True:
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)
    print(todos)

    
# =============================================================================
# the keyword coming after dot are methods. So methods are like functions.
# You see this function has this parenthesis and an argument,
# and the methods also has parenthesis and arguments.
# But methods are attached to data types, to other objects.
# In this case, this append method is part of this todos variable.
# Actually, it is not part of the variable,
# it is part of the object associated with that variable.
# 
# In this case, the object is a list.
# You see, it's a list type,
# and every object has its own methods.
# So for example, if you want to access the append method
# of the todo, todo, this variable is associated
# with a string, not a list.
# 
# So if you try to apply append to that string,
# you're gonna get an error.
# 
# =============================================================================