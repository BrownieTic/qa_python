import pytest
from main import BooksCollector

@pytest.fixture(scope="function")
def collector():
    book_collector = BooksCollector()
    return book_collector

@pytest.fixture(scope="function")
def collector_one_book(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    return collector

@pytest.fixture(scope="function")
def collector_one_book_with_genre(collector_one_book):
    collector_one_book.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
    return collector_one_book

@pytest.fixture(scope="function")
def collector_one_book_in_favorites(collector_one_book):
    collector_one_book.add_book_in_favorites('Гордость и предубеждение и зомби')
    return collector_one_book