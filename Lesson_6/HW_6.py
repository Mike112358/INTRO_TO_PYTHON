import time

#Задача 1
'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''

#Первый способ
class TrafficLight:
    __color = 'Red'
    def running(self):
        c = 1
        while c<5:
            print(TrafficLight.__color)
            time.sleep(7)
            TrafficLight.__color = 'Yellow'
            print(TrafficLight.__color)
            time.sleep(2)
            TrafficLight.__color = 'Green'
            time.sleep(1)
            print(TrafficLight.__color)
            TrafficLight.__color = 'Red'
            time.sleep(7)
            c+=1
    def __call__(self, *args, **kwargs):
        self.running()

tr = TrafficLight()
tr()

##Второй способ. Пользователь указывает какой цвет
class TrafficLight1:
    __color = 'Red'
    def __init__(self, color):
        self.color = color
    def running1(self):
        if self.color == TrafficLight1.__color:
            print(self.color)
            time.sleep(1)
            print("Yellow")
            time.sleep(1)
            print("Green")
            time.sleep(1)
        else:
            print("You are an asshole")

tr_1 = TrafficLight1("Red")
tr_1.running1()


#Задача 2
'''
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. 
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
'''

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def asph_mass(self):
        one_km_mass = 10
        sm_asph = 5
        return self._width*self._length*one_km_mass*sm_asph

road =Road(3, 3)
print(road.asph_mass())



#Задача 3
'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). 
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return f"{self._income}"

income_dict = {"Mike": {"wage": 500, "bonus": 200}, "Kate": {"wage": 600, "bonus":100}, "Johnny": {"wage": 700, "bonus": 300}}
worker = Worker("Mike", "Ruffalo", "Developer", 100)
pos = Position(list(income_dict.keys())[2], "Smith", "Developer", list(dict(list(income_dict.values())[2]).values())[0] + list(dict(list(income_dict.values())[2]).values())[1])

print(pos.get_full_name())
print(pos.get_total_income())



#Задача 4
'''
4. Реализуйте базовый класс Car. 
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости
'''

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print("Я поехала, господа!!! Я же беспилотник, нафиг мне водитель")

    def stop(self):
        print("Я сбила гопника! Пришлось остановиться!")

    def turn(self,direction):
        print(f"После того как я сбила гопника я повернула {direction} ")

    def show_speed(self):
        print(f"Моя текущая скорость {self.speed}")

class TownCar(Car):
    def show_speed(self):
        if self.speed>60:
            print("Ты слишком быстрый! Помедленнее")
        else:
            return super().show_speed()

class WorkCar(Car):
    def show_speed(self):
        if self.speed>40:
            print("Ты слишком быстрый! Помедленнее, пжлст")
        else:
            return super().show_speed()

class PoliceCaar(Car):
    def mig(self):
        print("Хочу новую мигалку!")

class SportCar(Car):
    def sport(self):
        print("Я тачка с битцухой!")

car = Car(100, "Red", "Mazda", 1)
workcar = WorkCar(40, "Green", "Nissan", 1)
sportcar = SportCar(500,"Yellow", "Jeep", 0)
car.turn("налево")
workcar.show_speed()
sportcar.sport()



# Задача 5
'''
5. Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” 
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
В каждом из классов реализовать переопределение метода draw. 
Для каждого из классов методы должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Я ручка ручка ручка!")

class Pencil(Stationery):
    def draw(self):
        print("Я вообще карандаш!")

class Handle(Stationery):
    def draw(self):
        print("Я маркер!")

stat = Stationery('канцелярка')
stat.draw()
pen = Pen('Ручка')
pen.draw()
pencil = Pencil('карандаш')
pencil.draw()
handle = Handle('маркер')
handle.draw()


