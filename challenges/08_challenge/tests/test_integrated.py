from lib.todo_list import *
from lib.todo import *

'''initialising test, add returns list of Todo objects'''
def test_todo_list_adds_todo_object():
    my_todo = Todo('a task')
    my_list = TodoList()
    my_list.add(my_todo)
    assert my_todo in my_list.the_todo_list

'''test incomplete returns list of Todo instances representing the incomplete todos'''
def test_incomplete_returns_todos():
    my_todo = Todo('a task')
    my_other_todo = Todo('other task')
    my_list = TodoList()
    my_list.add(my_todo)
    my_list.add(my_other_todo)
    assert my_todo in my_list.incomplete()

'''test complete returns list of Todo instances representing the complete todos'''
def test_complete_returns_todos():
    my_todo = Todo('a task')
    my_other_todo = Todo('other task')
    my_list = TodoList()
    my_list.add(my_todo)
    my_list.add(my_other_todo)
    my_todo.mark_complete()
    assert [my_todo] == my_list.complete()

def test_give_up_marks_all_todos_complete():
    my_todo = Todo('a task')
    my_other_todo = Todo('other task')
    my_list = TodoList()
    my_list.add(my_todo)
    my_list.add(my_other_todo)
    my_list.give_up()
    assert my_todo in my_list.complete() and my_other_todo in my_list.complete()

"""test todo
init sets the task property and complete to false"""
def test_init_todo():
    
    pass

"""test mark_complete sets complete to true"""
def test_mark_complete():
    pass