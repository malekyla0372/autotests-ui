import pytest


@pytest.fixture
def clear_books_database() -> None:
    print("clearing books database")

@pytest.fixture
def fill_books_database() -> None:
    print("filling books database")

@pytest.mark.usefixtures("fill_books_database")
def test_read_all_books_in_library():
    print("Reading all books in library")

@pytest.mark.usefixtures(
    "fill_books_database",
    "clear_books_database",
)
class TestLibrary:
    def test_read_book_from_library(self):
        ...
    def test_delete_book_from_library(self):
        ...