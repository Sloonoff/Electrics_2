from src.item import Item


class LanguageMixin:
    """
    Миксин для изменения языка клавиатуры.
    """

    def change_lang(self) -> 'Keyboard':
        """
        Метод для изменения языка клавиатуры.
        :return: Экземпляр класса Keyboard с измененным языком.
        """
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'
        return self
