from src.item import Item


class Phone(Item):
    """
    Класс для представления смартфона в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название смартфона.
        :param price: Цена за единицу смартфона.
        :param quantity: Количество смартфонов в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __add__(self, other):
        return Item(self.name + " и " + other.name, self.price + other.price, self.quantity + other.quantity)

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_sim):
        if new_sim < 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

        self.__number_of_sim = new_sim

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"



































    # from src.item import Item
#
#
# class Phone(Item):
#     """
#     Класс для представления смартфона в магазине.
#     """
#
#     def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
#         """
#         Создание экземпляра класса Phone.
#
#         :param name: Название смартфона.
#         :param price: Цена за единицу смартфона.
#         :param quantity: Количество смартфонов в магазине.
#         :param number_of_sim: Количество поддерживаемых сим-карт.
#         """
#         super().__init__(name, price, quantity)
#         self.number_of_sim = number_of_sim
#
#
#
#     def __str__(self):
#         """
#         Возвращает название смартфона.
#
#         :return: Название смартфона.
#         """
#         return self.name
#
#     def __repr__(self):
#         """
#         Возвращает строковое представление объекта.
#
#         :return: Строковое представление объекта.
#         """
#         return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
#
#     @property
#     def number_of_sim(self) -> int:
#         """
#         Геттер для количества поддерживаемых сим-карт.
#
#         :return: Количество поддерживаемых сим-карт.
#         """
#         return self._number_of_sim
#
#     @number_of_sim.setter
#     def number_of_sim(self, value: int) -> None:
#         """
#         Сеттер для количества поддерживаемых сим-карт.
#
#         :param value: Количество поддерживаемых сим-карт.
#         """
#         if not isinstance(value, int) or value <= 0:
#             raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
#         self._number_of_sim = value
