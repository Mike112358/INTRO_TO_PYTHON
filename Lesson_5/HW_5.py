#Задача 1
'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''
#Первый вариант
file = open('some.txt', 'w')
while True:
    t = input("Enter some string: ")
    if t != '':
        file.write(t+'\n')
    else:
        break
file.close()

#Второй вариант
with open('some_1.txt','w') as file:
    while True:
        t = input("Enter your sting:")
        if t!='':
            file.write(t+'\n')
        else:
            break


#Задача 2
'''
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке
'''
with open('some_2.txt','r') as file:
    cnt_string = 0
    cnt_words = []
    n = 1
    for line in file:
        cnt_words.append(f"В строке № {n} {len(line.split(' '))} слов(а)")
        cnt_string+=1
        n+=1


#Задача 3
'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников
'''

with open('some_3.txt', 'r') as file:
    avg = 0
    i = 0
    salary_list = []
    for line in file:
        t = line.split(' ')
        if int(t[1]) <20000:
            print(t[0])
        salary_list.append(int(t[1]))
    avg_sal = sum(salary_list)/len(salary_list)


#Задача 4
'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''
## Немного считерил, но это все для того чтобы можно было сделать общий вариант(one, two, three, four, five, six ...)
from translate import Translator
translator= Translator(from_lang="english",to_lang="russian")
with open('some_4','r', encoding="utf-8") as file:
    with open('some_4_w.txt','w',encoding="utf-8") as file_w:
        i = 1
        for line in file:
            k = line.split(" — ")
            trans = translator.translate(k[0])
            file_w.write(f"{trans}  — {i}"+'\n')



#Задача 5
'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

with open('some_5.txt','w') as file:
    file.write(input("Enter sequence of numbers: "))
with open("some_5.txt", 'r') as file_r:
    t = file_r.read()
    lis =t.split(' ')
    S = sum([int(item) for item in lis])


#Задача 6
'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
'''

########################### СПИСАЛ С РАЗБОРА. НО РАЗОБРАЛСЯ ХОТЯ БЫ САМ.
my_dict = {}
with open('some_6.txt', encoding='utf-8') as file:
    for line in file:
        name, stats = line.split(":")
        #print(stats,"".join([i for i in stats if i ==" " or i.isdigit()]))
        name_sum = sum(map(int, "".join([i for i in stats if i ==" " or i.isdigit()]).split()))
        my_dict[name] = name_sum
#print(my_dict)

#Второй СПИСАННЫй и разобранный способ
with open('some_6.txt', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        new_str = "".join((i if i in "0123456789" else" ") for i in line)
        new_2 = [int(i) for i in new_str.split()]
        print(f"{line.split()[0]}{sum(new_2)}")


#Задача 7
'''
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
'''
with open('some_7.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    profit = []
    firm = []
    i = 0
    for line in lines:
        #print(line)
        num = [i for i in line.split() if i.isdigit()]
        profit.append(int(num[0]) - int(num[1]))
        firm.append(line.split()[0])
        average_profit = sum([int(k.split()[2:][0])-int(k.split()[2:][1]) for k in lines if (int(k.split()[2:][0])-int(k.split()[2:][1])>=0)])/len([i for i in lines if (int(i.split()[2:][0])-int(i.split()[2:][1])>=0)])
dict_profit = [{i:k for i,k in zip(firm,profit)},{"average_profit":average_profit}]
print(dict_profit)


#Создадим джееееейсон:
import json
with open('firm_profit.json','w') as write_f:
    json.dump(dict_profit, write_f)