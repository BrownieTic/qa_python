import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_not_add_book_add_duplicate(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('name', ['', 'Гордость и предубеждение и зомби' * 2])
    def test_add_new_book_not_add_book_false_len(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    def test_set_book_genre_set_genre(self, collector_one_book):
        collector_one_book.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector_one_book.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_set_book_genre_not_set_genre_name_not_exists(self, collector):
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == None

    def test_get_book_genre_get_genre(self, collector_one_book_with_genre):
        assert collector_one_book_with_genre.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_get_books_with_specific_genre_get_collection_fantasy(self, collector, collector_one_book_with_genre):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

    @pytest.mark.parametrize('genre', ['', 'Фентези', 'Детектив'])
    def test_get_books_with_specific_genre_get_collection_empty(self, collector_one_book_with_genre, genre):
        assert collector_one_book_with_genre.get_books_with_specific_genre(genre) == []

    collection_book = [('Гордость и предубеждение и зомби', 'Фантастика'), ('Что делать, если ваш кот хочет вас убить', 'Фантастика')] 
    @pytest.mark.parametrize('book, genre', collection_book)
    def test_get_books_genre_get_collection(self, collector, book, genre):
        n = 0
        for book, genre in collection_book:
            n += 1 
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)        
            assert len(collector.get_books_genre()) == n