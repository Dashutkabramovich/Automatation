lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
#функция фильтеро проверяет числа менее 30, и делящееся на 3 нацело
def filtero(a):
    if(a % 3 == 0 and a<30):
        return True
    else:
        return False
#фильтр ниже фильтрует значения
out_filter = filter(filtero, lst)
print (list(out_filter))