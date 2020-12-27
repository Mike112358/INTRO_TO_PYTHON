#Задача 1
'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль
'''
def two_numb(a,b):
    return a/b if b!=0 else 'Attention! You can not divide by zero'

a = int(input("Enter a:"))
b = int(input("Enter b:"))
print(two_numb(a,b))



##Задача 2
'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
'''

def named_func(name, surname,birthday,email,phone,city='LA'): ##проверил работу дефолтных переменных
    return (f"Your name is {name} {surname}. U live in {city}. U was born in {birthday}. Your email is {email}, phone is {phone}")

t = named_func(surname='Dog', name ='Snoop',phone = '112358', email = 'snoppy@mail.ru', birthday=1971)
print(t)


##Задача 3
'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов
'''
def my_func(a,b,c):
    if (a >=c and c>=b) or (c>=a and a>=b):
        d = c+a
    elif (b>=a and a>=c) or (a>=b and b>=c):
        d = a+b
    else:
        d = b + c
    return d


#Задача 4
'''
Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
'''
x = int(input("Enter x:"))
y = int(input("Enter y:"))

#Первый вариант
def my_func(x,y):
    return x**y

print(my_func(x,y))

#Второй вариант
def my_funcc (x,y):
    i = 0
    num = 1
    while (i<-y):
        num *= (1/x)
        i+=1
    return num

print(my_funcc(x,y))


#Задача 5
'''
Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу
'''
#Специальный символ = не число
def recursion_sum(sum_list):
    try:
        num = input("Enter sequence of numbers: ")
        num = num.split(" ")
        i = 0
        int_num = []
        while i<len(num):
            int_num.append(int(num[i]))
            i+=1
        sum_list.append(sum(int_num))
        print(sum(sum_list))
    except ValueError:
        return sum(sum_list) + sum(int_num)
    return recursion_sum(sum_list)
print(recursion_sum([]))

#Задача 6
'''
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. 
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. 
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
'''
int_func = lambda str: str.capitalize()
user_string = input("Enter Your string: ")
user_string = user_string.split(" ")
user_string = [int_func(i) for i in user_string]
print(" ".join(user_string))

