import math

# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным. Дополнительно: можете проверить, что это действительно число, 
# и что это действительно входит в нужный диапазон

# 6 -> да
# 7 -> да
# 1 -> нет

n_num = input("День недели: ")
if n_num.isdigit():
    n_num = int(n_num)
    if 5<n_num<=7:
        print("да")
    elif 1<n_num<=5:
        print("нет")
    else: print("ГДЕ ТЫ ВИДЕЛ ТАКИЕ НЕДЕЛИ?")
else: print("ЭТО НЕ ДЕНЬ НЕДЕЛИ!!!")
day = int(input)
day_name = {1: 'mon',
            2: 'tue',
            3: 'wen',
            4: 'thu',
            5: 'fri',
            6: 'sun',
            7: 'sat',}
print(day_name.get(day, 'ТАКОГО ДНЯ НЕ СУЩЕСТВУЕТ!!!'))

# 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# Нужно написать таблицу истинности.

for x in (True,False): # можно использовать (1,0)
    for y in (True,False):
        for z in (True,False):
            print('x: ',x,', y: ',y,', z: ',z,'=', not(x or y or z) == (not x and not y and not z))

# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

x_num, y_num = int(input("X: ")), int(input("Y: "))
if (x_num == 0 or y_num == 0):
    if (x_num == 0 and y_num != 0):
        print('Точка на оси "Х"')
    elif (y_num == 0 and x_num != 0):
        print('Точка на оси "Y"')
    else: print('Кординаты X и Y должны быть ≠ 0')
else:
    if (x_num > 0):
        if (y_num > 0):
            print('1 четверть') 
        else: print('4 четверть') 
    else:
        if (y_num > 0):
            print('2 четверть')
        else: print('3 четверть') 

# 4-Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# - quarter = 1 => x∈(0, ∞) u y∈(0,∞)

x_num = int(input("Enter quarter: "))
if(x_num==1): print('x∈(0, ∞) u y∈(0,∞)') 
if(x_num==2): print('x∈(0, -∞) u y∈(0,∞)')
if(x_num==3): print('x∈(0, ∞) u y∈(0,-∞)')
if(x_num==4): print('x∈(0, -∞) u y∈(0,-∞)')
else: print('Not quarter')


# 5- Напишите программу, которая принимает на вход координаты  двух точек и находит расстояние между ними в 2D пространстве.

# A (3,6); B (2,1) -> 5.09
# A (7,-5); B (1,-1) -> 7.21

ax_num, ay_num = float(input("Точка A\nX: ")), float(input("Y: "))
bx_num, by_num = float(input("Точка B\nX: ")), float(input("Y: "))
ab_range = math.sqrt(((ax_num-bx_num)**2) + (ay_num-by_num)**2)
print(round(ab_range, 2))