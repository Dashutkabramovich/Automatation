n=int(input("Введите любое число:"))
print("Список чисел от 1", "до", n)
for i in range(1, n+1):
    if (i % 3 != 0) and (i % 5 != 0):
        print(i, end=' ')
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz") 
    elif (i % 3 == 0):
        print("Fizz") 
    elif (i % 5 == 0):
        print("Buzz") 
