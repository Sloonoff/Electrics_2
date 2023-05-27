from src.item import Item


def test_name_length():
    item = Item(name='Телефон', price=10000, rating=5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    try:
        item.name = 'СуперСмартфон'
    except Exception as e:
        assert str(e) == 'Длина наименования товара превышает 10 символов.'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all_items) == 6


def test_string_to_number():
    assert Item.string_to_number('5') == 5.0
    assert Item.string_to_number('5.0') == 5.0
    assert Item.string_to_number('5.5') == 5.5
















# """Здесь надо написать тесты с использованием pytest для модуля item."""
# from src.item import Item
#
#
# def test_name_length():
#     item = Item('Телефон', 10000, 5)
#     item.name = 'Смартфон'
#     assert item.name == 'Смартфон'
#
#     try:
#         item.name = 'СуперСмартфон'
#     except Exception as e:
#         assert str(e) == 'Длина наименования товара превышает 10 символов.'
#
#
# def test_instantiate_from_csv():
#     Item.instantiate_from_csv()
#     assert len(Item.all_items) == 6
#
#
# def test_string_to_number():
#     assert Item.string_to_number('5') == 5.0
#     assert Item.string_to_number('5.0') == 5.0
#     assert Item.string_to_number('5.5') == 5.5
