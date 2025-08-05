from typing import List
#TODO Class for Authors

class Book():
    title = ""
    author =List[str]
    genre = ""
    is_aval = True
    is_chosen = False


    def __init__(self, book_title: str, book_author:List[str], book_genre: str, book_aval: bool, book_chosen:bool)-> None:
        # for educational purposes i`m not checking for data corectness, just putting it insede of class
        #TODO: if/else statements checkups on data that`s comming in
        self.title = book_title
        self.author = book_author
        self.genre = book_genre
        self.is_aval = book_aval
        self.is_chosen = book_chosen
    # i`d like to realize  a stack of book`s here to make sure user can borrow book, but maybe later
    def borrow_book(self):
        if(self.is_aval):
            self.is_chosen = True
            self.is_aval = False
            print(f"You succesfully borrowed a book {self.title}")
        else:
            print(f"Book {self.title} is already borrowed to someone")
    def return_book(self):
        if(self.is_chosen):
            self.is_chosen = False
            self.is_aval = True
            print(f"You sucesfully returned a book {self.title}")
        else: 
            print("You can not return something you don`t have")
    def print_details(self):
        print(f"The {self.title} book is written by {self.author}")
        if(self.is_aval):
            print("This book is avaliable")
        else:
            print("We`re sorry to tell that, but book is already taken by someone, serch another one")



