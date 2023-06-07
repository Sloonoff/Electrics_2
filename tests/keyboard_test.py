from src.keyboard import Keyboard

def test_keyboard_creation():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

def test_keyboard_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"

def test_keyboard_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert str(kb.language) == "RU"

def test_keyboard_change_lang_twice():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang().change_lang()
    assert str(kb.language) == "EN"

def test_keyboard_change_lang_invalid():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    try:
        kb.language = 'CH'
    except AttributeError as e:
        assert str(e) == "can't set attribute"
