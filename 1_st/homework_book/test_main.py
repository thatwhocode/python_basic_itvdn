from .main import Book

def test_of_creation():
    bible = Book("Bible", ["Moises"], "historical/fairytale", True, False)
    assert bible.title == "Bible"
    assert bible.author ==["Moises"]
    assert bible.genre == "historical/fairytale"
    assert bible.is_aval == True
    assert bible.is_chosen ==False

def test_of_borrowin():
    bible = Book("Bible", ["Moises"], "historical/fairytale", True, False)
    bible.borrow_book()
    assert bible.is_aval ==False
    assert bible.is_chosen ==True


def test_of_returning():
    bible = Book("Bible", ["Moises"], "historical/fairytale", True, False)
    bible.borrow_book()
    bible.return_book()
    assert bible.is_aval == True
    assert bible.is_chosen == False
    