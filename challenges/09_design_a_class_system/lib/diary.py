"""takes diary entry
takes todo_list"""
from lib.diary_entry import *
from lib.todo_list import *

class Diary():
    def __init__(self):
        self.entry_list = []
        self.todos = []

    def add(self, entry):
        self.entry_list.append(entry)

    def read(self):
        the_entries = {}
        for i in self.entry_list:
            the_entries[i.title] = i.contents
        return the_entries
    

#     As a user
#     So that I can reflect on my experiences in my busy day
#     I want to select diary entries to read based on how much time I have and my reading speed
# scrape diary entries per wpm minutes
    def what_can_i_read(self, wpm, minutes):
        total_words_read = wpm*minutes
        possible_reading = []
        for i in self.entry_list:
            if i.count_words() <= total_words_read:
                possible_reading.append(i)

        return possible_reading


    def add_todo(self, todolist):
        self.todos.append(todolist)
#     As a user
#     So that I can keep track of my tasks
#     I want to keep a todo list along with my diary
# todolist 
    def give_mobiles(self):
        mobile_numbers = []
        entries = self.read()
        content = ''
        for i in entries.values():
            content += (i)
        wordlist = content.split()
        for i in wordlist:
            if i[0:2] == '07':
                print (i)
                mobile_numbers.append(i)
        return mobile_numbers
        



        # print (entries.values().split)
        

        # returns mobile numbers from contents
#     As a user
#     So that I can keep track of my contacts
#     I want to see a list of all of the mobile phone numbers in all my diary entries
# return mobile number variable