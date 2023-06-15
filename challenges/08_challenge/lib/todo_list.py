# File: lib/todo_list.py
class TodoList:
    def __init__(self):

        self.the_todo_list = []

    def add(self, todo):
        self.the_todo_list.append(todo)
      
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_tasks = [i for i in self.the_todo_list if i.complete == False]
        return incomplete_tasks

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_tasks = [i for i in self.the_todo_list if i.complete == True]
        return complete_tasks

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for i in self.the_todo_list:
            i.mark_complete()
        

