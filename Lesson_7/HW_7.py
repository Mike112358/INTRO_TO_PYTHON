#Задача 1
class Matrix:

    def __init__(self, x):
        self.x = x
    def __str__(self):
        c = f"Матрица {len(self.x)} X {len(self.x[0])}\n\n"
        for i in range(len(self.x)):
            c += f"{self.x[i]}\n"
        t = c.replace("[", '')
        t = t.replace("]",'')
        t = t.replace(',','')
        return t

    def __add__(self, other):
        z = []
        for i in range(len(self.x)):
            l = []
            for k in range(len(self.x[0])):
                l.append(self.x[i][k] + other.x[i][k])
            z.append(l)
        return Matrix(z)



matrix_1 = Matrix([[1,1,1], [1, 1, 1]])
matrix_2 = Matrix([[2,2,2], [2, 2, 2]])
matrix_3 = Matrix([[10,10,10], [10, 10, 10]])
c = matrix_1
d = 1
print(matrix_1+matrix_2+matrix_2 + matrix_1)
print(matrix_1+matrix_1)
d= matrix_1
k = 1

#Задача 2

class Shoes:
    def __init__(self, type, H, V):
        c = "Вся одежда в сборе!"
        self.type = type
        self.V = V
        self.H = H

    def consumption(self):
        pass
    def __str__(self):
        if (self.V/6.5+0.5) <=0 or (self.H*2 + 0.3) <=0:
            return "Вы ввели некорректные данные!"
        else:
            return f"Общий расход ткани: {self.V/6.5+0.5 + self.H*2 + 0.3}"


class Coat(Shoes):
    def __str__(self):
        if self.type == 'coat':
            return f"Расход ткани на пальто: {self.V/6.5+0.5}"
        else:
            raise ValueError("Несоответствие типов")

    @property
    def for_10_coat(self):
        return 10*(self.V/6.5+0.5)


class Suit(Shoes):
    def __str__(self):
        if self.type =='suit':
            return f"Расход ткани на костюм: {self.H*2 + 0.3}"
        else:
            raise ValueError("Несоответствие типов")

    @property
    def for_10_suits(self):
        return 10*(self.H*2 + 0.3)




suit = Suit('suit', 1, 0)
coat = Coat('coat', 1,0)
c = 1
print(coat.for_10_coat)


#Задача 3
class Cell:
    def __init__(self, cnt):
        self.cnt = cnt

    def __str__(self):
        return f"Количество клеток = {self.cnt}"

    def __add__(self, other):
        cnt = self.cnt + other.cnt
        return Cell(cnt)

    def __sub__(self, other):
        cnt = self.cnt - other.cnt
        if cnt<0:
            raise ValueError("Invalid value!")
        return Cell(cnt)
    def __mul__(self, other):
        cnt = self.cnt * other.cnt
        return Cell(cnt)

    def __truediv__(self, other):
        cnt = self.cnt//other.cnt
        if cnt<0 or other.cnt == 0:
            raise ValueError("Invalid value!")
        return Cell(cnt)

    def make_order(self):
        c = str('\\n')
        f = f"{(self.cnt // 5) * ('*****' + c)}"
        k = f[:len(f) - 2]
        if self.cnt%5 == 0:
            return k
        else:
            g = k + c + f"{(self.cnt%5)*'*'}"
            return g


cell_1 = Cell(20)
cell_2 = Cell(2)
print(cell_1+cell_2+cell_1+cell_2)
print(cell_2 - cell_2)
print(cell_1*cell_2)
print(cell_1/cell_2)
print(cell_1.make_order())



