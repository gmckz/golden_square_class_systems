from lib.diary_entry import *
from lib.todo_list import *
from lib.diary import *
from lib.todo import *

# As a user
# So that I can record my experiences
# I want to keep a regular diary
def test_diary_adds_entries():
    my_diary = Diary()
    my_entry = DiaryEntry('title', 'contents')
    my_diary.add(my_entry)
    assert my_entry in my_diary.entry_list

# As a user
# So that I can reflect on my experiences
# I want to read my past diary entries
def test_diary_read():
    my_diary = Diary()
    my_entry = DiaryEntry('title', 'contents')
    my_entry2 = DiaryEntry('title2', 'contents2')
    my_entry3 = DiaryEntry('title3', 'contents3')

    my_diary.add(my_entry)
    my_diary.add(my_entry2)
    my_diary.add(my_entry3)

    assert my_diary.read() == {'title': 'contents', 'title2': 'contents2', 'title3': 'contents3'}


# As a user
# So that I can reflect on my experiences in my busy day
# I want to select diary entries to read based on how much time I have and my reading speed
def test_diary_read_time():
    my_diary = Diary()
    my_entry = DiaryEntry('title', 'contents '*10)
    my_entry2 = DiaryEntry('title2', 'contents2 '*20)
    my_entry3 = DiaryEntry('title3', 'contents3 '*30)

    my_diary.add(my_entry)
    my_diary.add(my_entry2)
    my_diary.add(my_entry3)

    assert my_diary.what_can_i_read(9, 1) == []
    assert my_diary.what_can_i_read(19, 1) == [my_entry]
    assert my_diary.what_can_i_read(21, 1) == [my_entry, my_entry2]
    assert my_diary.what_can_i_read(31, 1) == [my_entry, my_entry2, my_entry3]

# As a user
# So that I can keep track of my tasks
# I want to keep a todo list along with my diary
def test_todo_in_diary():
    my_diary = Diary()
    my_todolist = TodoList()
    my_todo = Todo('eat')
    print (my_todo)
    my_todolist.add(my_todo)
    my_diary.add_todo(my_todolist)

    assert my_todolist in my_diary.todos

# As a user
# So that I can keep track of my contacts
# I want to see a list of all of the mobile phone numbers in all my diary entries
def test_diary_read_time():
    my_diary = Diary()
    my_entry = DiaryEntry('title', 'contents '*10+' 07945838294 ')
    my_entry2 = DiaryEntry('title2', 'contents2 '*20+' 07245838294 ')
    my_entry3 = DiaryEntry('title3', 'contents3 '*30+' 07945868294 ')

    my_diary.add(my_entry)
    my_diary.add(my_entry2)
    my_diary.add(my_entry3)

    assert my_diary.give_mobiles() == ['07945838294', '07245838294', '07945868294']