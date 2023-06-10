import csv   #Дз_4

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
    all_items = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        self.all_items.append(self)

    def __add__(self, other):
        return Item(self.name + " и " + other.name, self.price + other.price, self.quantity + other.quantity)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception('Длина наименования товара превышает 10 символов.')
        self._name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __repr__(self):

        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    @classmethod
    def set_pay_rate(cls, pay_rate):
        cls.pay_rate = pay_rate

    @classmethod
    def get_all_items(cls):
        return cls.all_items

    @classmethod
    def instantiate_from_csv(cls, path):
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                item = cls(row['name'], float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(string):
        return float(string)







































# class Item:
#     """
#     Класс для представления товара в магазине.
#     """
#     pay_rate = 1.0
#     all = []
#
#     def __init__(self, name: str, price: float, quantity: int) -> None:
#         """
#         Создание экземпляра класса item.
#
#         :param name: Название товара.
#         :param price: Цена за единицу товара.
#         :param quantity: Количество товара в магазине.
#         """
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def calculate_total_price(self) -> float:
#         """
#         Рассчитывает общую стоимость конкретного товара в магазине.
#
#         :return: Общая стоимость товара.
#         """
#         return self.price * self.quantity
#
#     def apply_discount(self) -> None:
#         """
#         Применяет установленную скидку для конкретного товара.
#         """
#         self.price *= self.pay_rate














































# class Item:     Дз_3
#     """
#     Класс для представления товара в магазине.
#     """
#     pay_rate = 1.0
#     all = []
#
#     def __init__(self, name: str, price: float, quantity: int) -> None:
#         """
#         Создание экземпляра класса item.
#
#         :param name: Название товара.
#         :param price: Цена за единицу товара.
#         :param quantity: Количество товара в магазине.
#         """
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def calculate_total_price(self) -> float:
#         """
#         Рассчитывает общую стоимость конкретного товара в магазине.
#
#         :return: Общая стоимость товара.
#         """
#         total_price = self.price * self.quantity
#         return total_price
#
#     def apply_discount(self) -> None:
#         """
#         Применяет установленную скидку для конкретного товара.
#         """
#         self.price = self.price * (1 - self.pay_rate)
#
#     def __repr__(self):
#         return f"Item('{self.name}', {self.price}, {self.quantity})"
#
#     def __str__(self):
#         return self.name
#
#
#
#
# import csv     Дз_2
#
# class Item:
#     """
#     Класс для представления товара в магазине.
#     """
#     pay_rate = 1
#     all_items = []
#
#     def __init__(self, name: str, price: float, quantity: int) -> None:
#         """
#         Создание экземпляра класса item.
#
#         :param name: Название товара.
#         :param price: Цена за единицу товара.
#         :param quantity: Количество товара в магазине.
#         """
#         self._name = name
#         self.price = price
#         self.quantity = quantity
#         self.all_items.append(self)
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         if len(value) > 10:
#             raise Exception('Длина наименования товара превышает 10 символов.')
#         self._name = value
#
#     def calculate_total_price(self) -> float:
#         """
#         Рассчитывает общую стоимость конкретного товара в магазине.
#
#         :return: Общая стоимость товара.
#         """
#         return self.price * self.quantity
#
#     def apply_discount(self) -> None:
#         """
#         Применяет установленную скидку для конкретного товара.
#         """
#         self.price *= self.pay_rate
#
#     @classmethod
#     def set_pay_rate(cls, pay_rate):
#         cls.pay_rate = pay_rate
#
#     @classmethod
#     def get_all_items(cls):
#         return cls.all_items
#
#     @classmethod
#     def instantiate_from_csv(cls):
#         with open('src/items.csv', newline='') as csvfile:
#             reader = csv.DictReader(csvfile)
#             for row in reader:
#                 item = cls(row['name'], float(row['price']), int(row['quantity']))
#
#     @staticmethod
#     def string_to_number(string):
#         return float(string)
#
#
#
# class Item:    Дз_1
#     """
#     Класс для представления товара в магазине.
#     """
#     pay_rate = 1
#     all_items = []
#
#     def __init__(self, name: str, price: float, quantity: int) -> None:
#         """
#         Создание экземпляра класса item.
#
#         :param name: Название товара.
#         :param price: Цена за единицу товара.
#         :param quantity: Количество товара в магазине.
#         """
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.all_items.append(self)
#
#     def calculate_total_price(self) -> float:
#         """
#         Рассчитывает общую стоимость конкретного товара в магазине.
#
#         :return: Общая стоимость товара.
#         """
#         return self.price * self.quantity
#
#     def apply_discount(self) -> None:
#         """
#         Применяет установленную скидку для конкретного товара.
#         """
#         self.price *= self.pay_rate
#
#     @classmethod
#     def set_pay_rate(cls, pay_rate):
#         cls.pay_rate = pay_rate
#
#     @classmethod
#     def get_all_items(cls):
#         return cls.all_items
