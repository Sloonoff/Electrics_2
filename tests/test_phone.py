from src.phone import Phone


def test_phone_init():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert phone.name == "iPhone 14"
    assert phone.price == 120_000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


# def test_phone_add():
#     phone1 = Phone("iPhone 14", 120_000, 5, 2)
#     phone2 = Phone("Samsung Galaxy S21", 80_000, 10, 1)
#     assert (phone1 + phone2).quantity == 15


def test_phone_str():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone) == "iPhone 14"


def test_phone_repr():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phone_number_of_sim():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert phone.number_of_sim == 2
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3


def test_phone_number_of_sim_error():
    try:
        phone = Phone("iPhone 14", 120_000, 5, -1)
    except ValueError as e:
        assert str(e) == "Количество физических SIM-карт должно быть целым числом больше нуля."




