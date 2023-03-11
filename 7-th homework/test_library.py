from unittest.mock import patch
import library
import pytest


choices_get_declension_kopiyka = [
    ('1', 'копійка'),
    ('2', 'копійки'),
    ('5', 'копійок'),
    ('11', 'копійок')
]


choices_get_declension_hryvnia = [
    ('1', 'гривня'),
    ('3', 'гривні'),
    ('7', 'гривень'),
    ('12', 'гривень')
]


choices_separate_number = [
    (123.45, '123 гривні 45 копійок'),
    (5.00, '5 гривень 0 копійок'),
    (1.01, '1 гривня 01 копійка'),
    (123456.78, '123456 гривень 78 копійок')
]


choices_is_hot_today = [
    (0, False),
    (24, False),
    (25, True),
    (30, True)
]


choices_get_valid_number = [
    ("3.14",  3.14),
    ('5', 5),
    ('8.000000', 8.0)

]


@pytest.mark.parametrize('number, expected', choices_get_declension_kopiyka)
def test_get_declension_kopiyka(number, expected):
    assert library.get_declension_kopiyka(number) == expected


@pytest.mark.parametrize('number, expected', choices_get_declension_hryvnia)
def test_get_declension_hryvnia(number, expected):
    assert library.get_declension_hryvnia(number) == expected


@pytest.mark.parametrize('number, expected', choices_separate_number)
def test_separate_number(number, expected):
    assert library.separate_number(number) == expected


@pytest.mark.parametrize('number, expected', choices_is_hot_today)
def test_is_hot_today(number, expected):
    assert library.is_hot_today(number) == expected


@pytest.mark.parametrize('user_input, expected', choices_get_valid_number)
def test_get_valid_number(user_input, expected):
    with patch('builtins.input', return_value=user_input):
        assert library.get_valid_number() == expected


def test_get_declension_kopiyka_type():
    arg = '123'
    result = library.get_declension_kopiyka(arg)
    assert isinstance(result, str)


def test_get_declension_hryvnia_type():
    arg = '123'
    result = library.get_declension_hryvnia(arg)
    assert isinstance(result, str)


def test_separate_number_return_type():
    num = 10.0
    result = library.separate_number(num)
    assert isinstance(result, str)




