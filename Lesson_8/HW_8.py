#Задачи 4-6
'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
'''
from abc import ABC, abstractmethod

#Абстрактный склад
class Storage(ABC):
    _cnt_employee:int
    _cnt_rooms:int

    def __init__(self, square, security, type_of_storage):
        self.square = square
        self.security = security
        self.type_of_storage = type_of_storage


#Дочерний класс: склад оргтехники
class Office_Storage(Storage):
    __cnt_employee = 100
    _cnt_rooms = 50
    __Products_cnt = {'Printer':55, 'Xerox':50, 'Scaner':70, 'Pens':250, 'Office Paper':100, 'Scissors':200}

    def __init__(self, square, security, type_of_storage, location):
        super().__init__(square, security, type_of_storage)
        self.location = location

    def private_inform(self):
        return f"Количество сотрудников склада {Office_Storage.__cnt_employee}. \n" \
               f"Число складских помещений {Office_Storage._cnt_rooms} \n" \
               f"На складе хранится следующее количество товара: {Office_Storage.__Products_cnt}"
    def prod_cnt(self):
        return self.__Products_cnt


#Абстрактный класс: оргтехника
class Office_equipment(ABC):
    cnt: int

    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color

    #@abstractmethod
    def action(self):
        print("Do smth")

    @property
    def valuable(self):
        pass


#Принтер
class Printer(Office_equipment):
    cnt = 10
    type='Printer'
    def __init__(self, name, weight, color, model):
        super().__init__(name, weight, color)
        self.model = model

    def action(self):
        print("Печать страницы!")

#Сканер
class Scaner(Office_equipment):
    cnt = 10
    type = 'Scaner'
    def __init__(self, name, weight, color, model):
        super().__init__(name, weight, color)
        self.model = model

    def action(self):
        print("Сканирование страницы!")


#Xerox
class Xerox(Office_equipment):
    cnt = 10
    type = 'Xerox'
    def __init__(self, name, weight, color, model):
        super().__init__(name, weight, color)
        self.model = model

    def action(self):
        print("Ксерокопирование страницы!")


#Класс - переходник
class Simbioz(Office_equipment, Office_Storage):
    def __init__(self, square,security,type_of_storage, location,name,weight,color):
        Office_Storage.__init__(self,square,security,type_of_storage, location)
        Office_equipment.__init__(self,name,weight,color)

    def to_storage(self,other):
        other.cnt -= 1
        print(f"На склад отправлен {other}")
        #т.к мы отправляем на склад, то кол-во товара соответствующего типа на складе увеличивается
        Office_Storage.prod_cnt(self)[other.type] += 1

    def to_company(self, other):
        print(f"В компанию отправлен {other}")
        #Мы передаем товар опредленного типа в компанию на складе у нас кол-во товара не изменилось
        other.cnt -= 1





k = 1

office = Office_Storage(10,True,'Office','Msk')
simbioz = Simbioz(20,True,'Office','Msk','Nm',10,'Blue')
c = 1
printer = Printer('Nm', 10,'Blue','x4')
scaner = Scaner('Scan', 12,'red', 'g5')
xerox = Xerox('X', 3,'Green', 'x5')
d =1
p = 1
simbioz.to_storage(printer)
simbioz.to_storage(xerox)
simbioz.to_company(printer)
print(printer.cnt)
print(office.private_inform())



#Задача 1
'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. 
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных
'''

class Data:

    def __init__(self, date):
        self.date = date

    def __str__(self):
        return self.date

    @classmethod
    def output(cls, date):
        day =int(str(date).split(' - ')[0])
        month = int(str(date).split(' - ')[1])
        year = int(str(date).split(' - ')[2])
        return day, month, year

    @staticmethod
    def validation(date):
        return f"день - {int(str(date).split(' - ')[0])}\n" \
               f"месяц - {int(str(date).split(' - ')[1])}\n" \
               f"год - {int(str(date).split(' - ')[2])}"

date = Data('11 - 01 - 2020')
print(Data.output(date))
print(Data.validation(date))



#Задача 2
'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''

##Собственное исключение
class NewException(Exception):
    def __init__(self, *args, **kwargs):
        self.text = args[0]


def division(a,b):
    if b == 0:
        raise NewException("Делить на 0 нельзя!!")
    return a/b

try:
    print(division(1,0))
except Exception as err:
    print(type(err), err)



#Задача 3
'''
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. 
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. 
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”. 
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. 
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число. 
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. 
При этом работа скрипта не должна завершаться
'''

class MyException(Exception):
    def __init__(self, *args, **kwargs):
        self.txt = args[0]

def func():
    lis = []
    x = input("Enter the number: ")
    while x !='Stop':
        for item in x:
            if item not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '0'):
                raise MyException("This shit is not number!")
        lis.append(x)
        print(lis)
        x = input("Enter the number: ")
    return lis

try:
    print(func())
except Exception as err:
    print(err, type(err))



#Задача 7
'''
7. Реализовать проект «Операции с комплексными числами». 
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
'''

class Complex:
    def __init__(self, complex_number):
        self.complex_number = complex_number

    def __str__(self):
        return self.complex_number

    def __add__(self, other):
        return f"{int(str(self.complex_number).split(' ')[0]) + int(str(other.complex_number).split(' ')[0])} + " \
               f"{int(str(self.complex_number).split(' ')[2][0]) + int(str(other.complex_number).split(' ')[2][0])}i"

    def __mul__(self, other):
        if str(self.complex_number).split(' ')[1] == str(other.complex_number).split(' ')[1]:
            return f"{int(str(self.complex_number).split(' ')[0])* int(str(other.complex_number).split(' ')[0]) - int(str(self.complex_number).split(' ')[2][0])*int(str(other.complex_number).split(' ')[2][0])} + " \
                   f"{int(str(self.complex_number).split(' ')[0])*int(str(other.complex_number).split(' ')[2][0]) + int(str(other.complex_number).split(' ')[0])*int(str(self.complex_number).split(' ')[2][0])}i"
        ###Тут еще вариант для разных знаков, просто влом такие длинные штуки писать, но я все понял 100%



comp_num1 = Complex('2 + 3i')
comp_num2 = Complex('1 + 7i')
#print(comp_num1)
print(comp_num1+comp_num2)
print(comp_num1*comp_num2)
