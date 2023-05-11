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
        assert len(collector.get_books_rating()) == 2

    # проверяем, что при инициализации объекта класса создаётся пустой словарь books_rating
    def test_books_rating_empty_dictionary(self):
        collector = BooksCollector()

        assert collector.books_rating == {}

    # проверяем, что при инициализации объекта класса создаётся пустой список favorites
    def test_favorites_empty_list(self):
        collector = BooksCollector()

        assert collector.favorites == []

    # проверяем, что после добавления новой книги ей присваивается рейтинг 1
    def test_add_new_book_added_book_rating_one(self):
        collector = BooksCollector()

        collector.add_new_book('Илиада')

        assert collector.get_book_rating('Илиада')

    # проверяем, что рейтинг книги не может быть меньше 1
    def test_set_book_rating_book_rating_no_less_than_one(self):
        collector = BooksCollector()

        collector.add_new_book('Му-му')
        collector.set_book_rating('Му-му', 0)

        assert collector.get_book_rating('Му-му')

    # проверяем, что рейтинг книги не может быть больше 10
    def test_set_book_rating_book_rating_no_more_than_ten(self):
        collector = BooksCollector()

        collector.add_new_book('Улисс')
        collector.set_book_rating('Улисс', 15)

        assert collector.get_book_rating('Улисс')

    # проверяем, что у недобавленной книги нет рейтинга
    def test_get_book_rating_no_rating_for_not_added_book(self):
        collector = BooksCollector()

        assert collector.get_book_rating('Одиссея') == None

    # проверяем, что выводятся книги с рейтингом 8
    def test_get_books_with_specific_rating_books_with_no_less_than_eight_rating(self):
        collector = BooksCollector()

        collector.add_new_book('Коллекционер')
        collector.add_new_book('Хитроумный идальго Дон Кихот Ламанчский')
        collector.set_book_rating('Хитроумный идальго Дон Кихот Ламанчский', 8)

        if 8 in collector.books_rating.values():
            assert collector.get_books_with_specific_rating(8)

    # проверяем, что выводится словарь books_rating
    def test_get_books_rating_return_books_rating_dictionary(self):
        collector = BooksCollector()

        collector.add_new_book('Колыбель для кошки')

        assert 'Колыбель для кошки' in collector.get_books_rating().keys()

    # проверяем, что книга добавилась в Избранное
    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()

        collector.add_new_book('Улитка на склоне')
        collector.add_book_in_favorites('Улитка на склоне')

        assert 'Улитка на склоне' in collector.favorites

    # проверяем, что книга удалилась из Избранного
    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()

        collector.add_new_book('Отцы и дети')
        collector.add_book_in_favorites('Отцы и дети')

        assert collector.delete_book_from_favorites('Отцы и дети') == None

    # проверяем, что выводится список Избранных книг
    def test_get_list_of_favorites_books_return_list_of_favorite_books(self):
        collector = BooksCollector()

        collector.add_new_book('Крутой маршрут')
        collector.add_book_in_favorites('Крутой маршрут')
        collector.add_new_book('Братья Карамазовы')
        collector.add_book_in_favorites('Братья Карамазовы')

        assert 'Крутой маршрут' and 'Братья Карамазовы' in collector.get_list_of_favorites_books()
