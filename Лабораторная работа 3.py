class Book:
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError('Значение количества страниц должно быть числом')
        if value <= 0:
            raise ValueError('Количество страниц должно быть положительным целым числом.')

        self._pages = value

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name,author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float):

        if not isinstance(value, (float, int)):
            raise TypeError('Значение продолжительности должно быть числом')
        if  value <= 0:
            raise ValueError('Продолжительность должна быть положительным числом.')

        self._duration = float(value)

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}"

'''Пример использования '''
paper_book = PaperBook('Отцы и дети', 'И.С. Тургенев', 284)
audio_book = AudioBook('Мастер и Маргарита','М.А. Булгаков',17.5)
print(paper_book)
print(audio_book)

'''Проверка свойств'''
try:
    paper_book.pages = -284
except ValueError as error:
    print(f'Ошибка: {error}')

try:
    audio_book.duration = 'семнадцать с половиной часов'
except TypeError as error:
    print(f'Ошибка: {error}')