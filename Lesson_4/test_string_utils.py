import pytest
from string_utils import StringUtils
string_util = StringUtils()

#Тест-кейс №1

@pytest.mark.parametrize('string, result', [
    #позитивные тест-кейсы:
   ("вася", "Вася"),
    ("алла Виктория", "Алла виктория"),
    ("зина2", "Зина2"),
    ("кеша-5", "Кеша-5"),
    #негативные тест-кейсы:
    ("", ""),
    ("МЧС", "Мчс"), 
    ("123баба", "123баба"), 
    ("  моя прелесть", "  моя прелесть"),  
    ("новости дня  ", "Новости дня  "), 
])

def test_capitilize(string, result):
    res = string_util.capitalize(string)
    assert res == result

#Тест-кейс №2

@pytest.mark.parametrize('string, result', [
    #positive test cases:
    ("  собака", "собака"),
    (" ЗИЛ", "ЗИЛ"),
    ("  '123'", "'123'"),
    (" Дина-Лена", "Дина-Лена"),
   
    #negative test cases:
    ("", ""),
    ("ма ма", "ма ма"),
    ("кот", "кот"),
    ("'123'  ", "'123'  "),
    ('1', '1'),
])
def test_trim(string, result):
    res = string_util.trim(string)
    assert res == result

#Тест-кейс №3

@pytest.mark.parametrize('string, delimeter, result', [
#позитивные тест-кейсы:
    ("яблоко,банан,апельсин",",", ["яблоко", "банан", "апельсин"]),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
    ("*@$@%@&", "@", ["*", "$", "%", "&"]),
    #негативные тест-кейсы:
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"]),
    ])

def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = string_util.to_list(string)
    else:
        res = string_util.to_list(string, delimeter)
    assert res == result

#Тест-кейс №4

@pytest.mark.parametrize('string, symbol, result', [
    
#позитивные тест-кейсы:

    ("банан", "б", True),
    (" гвоздь", "д", True),
    ("мир  ", "р", True),
    ("диван-кровать", "-", True),
    ("145", "1", True),
    ("", "", True),

#негативные тест-кейсы:

    ("Москва", "м", False),
    ("привет", "з", False),  
    ("кот", "№", False), 
    ("", "з", False),  
#Ошибка, описанная в defects. "hello", symbol = "" Expected Result: False Actual Result: True 
])

def test_contains(string, symbol, result):
    res = string_util.contains(string, symbol)
    assert res == result

#Тест-кейс №5

@pytest.mark.parametrize('string, symbol, result', [
    
    #позитивные тест-кейсы:

    ("корень", "к", "орень"),
    ("Лена", "н", "Леа"),
    ("Море", "М", "оре"),
    ("156", "1", "56"),
    ("Анна-Зина", "-", "АннаЗина"),
    ("Красная Москва", " ", "КраснаяМосква"),

    #негативные тест-кейсы:

    ("ножик", "з", "ножик"),
    ("", "", ""),
    ("", "с", ""),
    ("кофе", "", "кофе"),
    ("зелень ", " ", "зелень"),
])
def test_delete_symbol(string, symbol, result):
    res = string_util.delete_symbol(string, symbol)
    assert res == result

#Тест-кейс №6

@pytest.mark.parametrize('string, symbol, result', [

#позитивные тест-кейсы:
  
    ("светофор", "с", True),
    ("", "", True),
    ("Москва", "М", True),
    ("Film  ", "F", True),
    ("Мира-Зина", "М", True),
    ("123", "1", True),

#негативные тест-кейсы:

    ("Таня", "т", False),
    ("мира", "М", False),
    ("", "@", False),
    ("корж", "ж", False),
    ("тина", "н", False)
])
def test_starts_with(string, symbol, result):
    res = string_util.starts_with(string, symbol)
    assert res == result

#Тест-кейс №7

@pytest.mark.parametrize('string, symbol, result', [

#позитивные тест-кейсы:

    ("Костя", "я", True),
    ("ТОРТИК", "К", True),
    ("", "", True),
    ("собака ", "", True),
    ("67", "7", True),
    ("Роза-Лютик", "к", True),
    ("Мама1", "1", True),
    ("БоБ", "Б", True),

#негативные тест-кейсы:

    ("морж", "л", False),
    ("слон", "с", False),
    ("дверь", "Ь", False),
    ("", "*", False)
])
def test_end_with(string, symbol, result):
    res = string_util.end_with(string, symbol)
    assert res == result

#Тест-кейс №8

#позитивные тест-кейсы:

@pytest.mark.parametrize('string, result', [
   
#позитивные тест-кейсы:

    ("", True),
    (" ", True),
    ("  ", True),

#негативные тест-кейсы:

    ("кот", False),
    (" дом", False),
    ("345", False),
])
def test_is_empty(string, result):
    res = string_util.is_empty(string)
    assert res == result

#Тест-кейс №9

@pytest.mark.parametrize('lst, joiner, result', [

#позитивные тест-кейсы:

    (["с", "о", "с"], ",", "с,о,с"),
    ([1,2,3,4,5], None, "1, 2, 3, 4, 5"),
    (["Лада", "Калина"], "-", "Лада-Калина"),
    (["Лада", "Калина"], "Гранта", "ЛадаГрантаКалина"),
    (["м", "р", "т"], "", "мрт"),

#негативные тест-кейсы:

    ([], None, ""),
    ([], ",", ""),
    ([], "кот", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = string_util.list_to_string(lst)
    else:
        res = string_util.list_to_string(lst, joiner)
    assert res == result


