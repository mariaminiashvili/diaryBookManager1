import sys

from diarybook import DiaryBook
from utils import read_from_json_into_application

class Menu:

    def __init__(self):
        self.diarybook = DiaryBook()


        self.choices = {
             "1": self.show_all_diaries,
             "2": self.add_diary,
             "3": self.search_diaries,
             "4": self.quit
         }

    def show_all_diaries(self):
        if len(self.diarybook.diaries) == 0:
            print("there are no diaries in the database.")
        else:
            for diary in self.diarybook.diaries:
                   print(f"{diary.id} - {diary.memo}")

    def add_diary(self):
        memo = input("enter a memo:")
        tags = input("enter tags:")
        self.diarybook.new_diary(memo,tags)
        print("your note has been added successfully")


    def search_diaries(self):
        keyword = input("enter a keyword")
        filtered_diaries = self.diarybook.search_diary(keyword)
        if len(filtered_diaries) == 0:
            print("we could not find any diary marching the given keyword")
        else:
            for diary in filtered_diaries:
                print(f"{diary.id} - {diary.memo}")

    def populate_database(self):
        diaries = utils.read_from_json_into_application("data.json")
        for diary in diaries:
            self.diarybook.diaries.append(diary)


    def quit(self):
        print("thanks for using our diarybook!")
        sys.exit(0)


    def display_menu(self):
        print("""
           diarybook Menu:
        
           1. Show  diaries
           2. Add Diary
           3. filter using keyword
           4. Quit program
        """)

    def run(self):
        # self.populate_database()
        while True:
             self.display_menu()
             choice = input("enter an option: ")
             action = self.choices.get(choice)
             if action:
                 action()
             else:
                 print("{0} is not a valid choice".format(choice))


if __name__ == "__main__" :
     Menu().run()
