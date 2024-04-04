#через переменную (параметры вводит пользователь)
a=int(input("Введите номер месяца от 1 до 12:"))
if (a>0) and (a<3):
    print("Зима")
if (a>2) and (a<6):
    print("Весна")
if (a>5) and (a<9):
    print("Лето") 
if (a>8) and (a<12):
    print("Осень")
if (a==12):
    print("Зима")

#через функцию (месяц задан - февраль)
def month_to_season(a):
    if (a>0) and (a<3):
        print("Зима")
    if (a>2) and (a<6):
        print("Весна")
    if (a>5) and (a<9):
        print("Лето") 
    if (a>8) and (a<12):
        print("Осень")
    if (a==12):
        print("Зима")

month_to_season(3)