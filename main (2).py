# coding: utf-8
text = "Hello, Python!"
print (text[0]) # Выводит первый символ
print (text[0:5]) # Выводит подстроку text от 0 символа до 5 (включительно с нулевым, исключая пятый)
print (text[4:10])# Выведет строку от 4 символа до 10 (включая четвертый, исключая 10)
print (text[0:14]) # Выведет всю строку
print (text[7:]) # Выведет строку с 7 символа до конца
print (text[:5]) # Выведет строку с начала до 5 символа. Аналогично print text[0:5]
print (text[:]) # Выведет всю строку
print (text[-1]) # Выводит последний символ
print (text[-1:-14]) # Не сработает, выведет пустую строку
print (text[::2]) # Третий аргумент - шаг. Выведет каждый второй символ
print (text[::-1]) # Шаг отрицательный. Выведет фразу наоборот
print (text + "Nice to code you") # Выведет новую строку
print (text * 10) # Выведет 10 восклицательных знаков
