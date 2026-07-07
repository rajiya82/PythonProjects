
def get_todos(filepath = "todos.txt"):
    """read the todos file and return a list"""
    with open(filepath,"r") as file:
        local_todos = file.readlines()
        return local_todos

def put_todos(local_todos, filepath = "todos.txt"):
    """write the todos file"""
    with open(filepath,"w") as file:
        file.writelines(local_todos)
        return local_todos

def update_todos(completed_idx, local_todos, filepath = "todos.txt"):
    """update the todos file"""
    with open(filepath, "w") as file:
        local_todos.pop(completed_idx)
        file.writelines(local_todos)
        return True