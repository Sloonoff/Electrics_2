class Item:
    """
    Класс для представления товара в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создает экземпляр класса Item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """
        Возвращает название товара.

        :return: Название товара.
        """
        return self.name


class Keyboard(Item):
    """
    Класс для представления клавиатуры в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создает экземпляр класса Keyboard.

        :param name: Название клавиатуры.
        :param price: Цена за единицу клавиатуры.
        :param quantity: Количество клавиатур в магазине.
        """
        super().__init__(name, price, quantity)
        self.language = 'EN'

    def __str__(self) -> str:
        """
        Возвращает название клавиатуры.

        :return: Название клавиатуры.
        """
        return self.name

    def change_lang(self) -> 'Keyboard':
        """
        Меняет раскладку клавиатуры на следующую.

        :return: Текущий экземпляр класса Keyboard.
        """
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'
        return self


class LanguageMixin:
    def __init__(self, language='EN'):
        self.language = language

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"
        return self

    def set_language(self, language):
        if language not in ('EN', 'RU'):
            raise ValueError(f"Неподдерживаемый язык: {language}")
        self.language = language








