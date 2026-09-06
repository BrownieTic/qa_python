import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    books = [('Гордость и предубеждение и зомби', 'Фантастика'), 
            ('Что делать, если ваш кот хочет вас убить', 'Комедии'),
            ('Вий', 'Ужасы')] 
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_duplicate_not_add_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('name', ['', 'Гордость и предубеждение и зомби' * 2])
    def test_add_new_book_false_len_not_add_book(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    def test_set_book_genre_one_book_set_genre(self, collector_one_book):
        collector_one_book.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector_one_book.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_set_book_genre_not_book_genre_none(self, collector):
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == None

    @pytest.mark.parametrize('name,genre', books)
    def test_get_book_genre_different_genres_get_genres(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_one_genre_get_collection_fantasy(self, collector, collector_one_book_with_genre):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']

    @pytest.mark.parametrize('genre', ['', 'Фентези', 'Детектив'])
    def test_get_books_with_specific_genre_get_collection_empty(self, collector_one_book_with_genre, genre):
        get_books = collector_one_book_with_genre.get_books_with_specific_genre(genre)
        assert get_books == []

    def test_get_books_genre_get_one_book_with_genre(self, collector_one_book_with_genre):
        get_books = collector_one_book_with_genre.get_books_genre()
        assert get_books == {'Гордость и предубеждение и зомби': 'Фантастика'}

    def test_get_books_genre_full_list_get_len_not_zero(self, collector):
        n = 0
        for book, genre in self.books:
            n += 1 
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)        
            assert len(collector.get_books_genre()) == n

    def test_get_books_for_children_allowable_genres_get_name_book(self, collector_one_book_with_genre):
        get_books = collector_one_book_with_genre.get_books_for_children()
        assert get_books == ['Гордость и предубеждение и зомби']

    @pytest.mark.parametrize('book, genre', 
                            [('Приключения Шерлока Холмса', 'Детективы'),
                            ('Вий', 'Ужасы')])
    def test_get_books_for_children_ban_genres_get_empty(self, collector, book, genre):
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_one_book_in_favorites(self, collector_one_book_in_favorites):
        get_books = collector_one_book_in_favorites.get_list_of_favorites_books()
        assert get_books == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_not_book_favorites_empty(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_one_book_in_favorites_empty_list(self, collector_one_book_in_favorites):
        collector_one_book_in_favorites.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert collector_one_book_in_favorites.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_book_not_favorites_lists_not_changed(self, collector, collector_one_book_in_favorites):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_list_of_favorites_books()) == 1 and len(collector.get_books_genre()) == 2

    def test_get_list_of_favorites_books_one_book_in_favorites(self, collector_one_book_in_favorites):
        get_books = collector_one_book_in_favorites.get_list_of_favorites_books()
        assert get_books == ['Гордость и предубеждение и зомби']
        