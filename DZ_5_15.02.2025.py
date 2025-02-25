# Задание 1
# Пользователь вводит с клавиатуры число в диапа-
# зоне от 1 до 100. Если число кратно 3 (делится на 3 без
# остатка) нужно вывести слово Fizz. Если число кратно 5
# нужно вывести слово Buzz. Если число кратно 3 и 5 нужно
# вывести Fizz Buzz. Если число не кратно не 3 и 5 нужно
# вывести само число.
# Если пользователь ввел значение не в диапазоне от 1
# до 100 требуется вывести сообщение об ошибке.

# a = int(input("Введите число от 1 до 100: "))

# if 1 <= a <= 100:
#     match (a % 3, a % 5):
#         case (0, 0):
#             print("Fizz Buzz")
#         case (0, _):
#             print("Fizz")
#         case (_, 0):
#             print("Buzz")
#         case (_, _):
#             print(a)
# else:
#     print("Некорректный ввод!")


#--------------------------------------------------------------------------------
# Задание 2
# Написать программу, которая по выбору пользова-
# теля возводит введенное им число в степень от нулевой
# до седьмой включительно.

# a = int(input("Введите число: "))
# step = int(input("Введите степень числа от 0 до 7: "))

# match step:
#     case 0:
#         print(f"{a}**{step} = {a**step}")
#     case 1:
#         print(f"{a}**{step} = {a**step}")
#     case 2:
#         print(f"{a}**{step} = {a**step}")
#     case 3:
#         print(f"{a}**{step} = {a**step}")
#     case 4:
#         print(f"{a}**{step} = {a**step}")
#     case 5:
#         print(f"{a}**{step} = {a**step}")
#     case 6:
#         print(f"{a}**{step} = {a**step}")
#     case 7:
#         print(f"{a}**{step} = {a**step}")
#     case _:
#         print("Некорректный ввод!")


#--------------------------------------------------------------------------------
# Задание 3
# Написать программу подсчета стоимости разговора
# для разных мобильных операторов. Пользователь вводит
# стоимость разговора и выбирает с какого на какой опе-
# ратор он звонит. Вывести стоимость на экран.

# print("Cтоимость услуг 1ой минуты разговора: ")
# print(" - 1 - Билайн, 5 руб./мин.\n - 2 - МТС, 10 руб./мин.\n - 3 - Теле2, 8 руб./мин.\n"
#        " - 4 - Сбер, 11 руб./мин.\n - 5 - Мегафон, 15 руб./мин.")

# a = int(input("Введите выбранный вариант: "))
# min = int(input("Введите количество минут: "))

# match a:
#     case 1:
#         print(f"Стоимость услуг составит: {5*min} руб.")
#     case 2:
#         print(f"Стоимость услуг составит: {10*min} руб.")
#     case 3:
#         print(f"Стоимость услуг составит: {8*min} руб.")
#     case 4:
#         print(f"Стоимость услуг составит: {11*min} руб.")
#     case 5:
#         print(f"Стоимость услуг составит: {15*min} руб.")
#     case _:
#         print("Некорректный ввод!")


#--------------------------------------------------------------------------------
# Задание 4
# Зарплата менеджера составляет 200$ + процент от про-
# даж, продажи до 500$ — 3%, от 500 до 1000 — 5%, свыше
# 1000 — 8%. Пользователь вводит с клавиатуры уровень
# продаж для трех менеджеров. Определить их зарплату,
# определить лучшего менеджера, начислить ему премию
# 200$, вывести итоги на экран.

zap1 = int(input("Введите уровень продаж 1го менеджера: "))
zap2 = int(input("Введите уровень продаж 2го менеджера: "))
zap3 = int(input("Введите уровень продаж 3го менеджера: "))

match zap1:
    case _ if zap1 < 500:
        zap1 = 200+zap1*0.03
        print(f"Зарплата 1го менеджера: {zap1}")
    case _ if 500 <= zap1 <= 1000:
        zap1 = 200+zap1*0.05
        print(f"Зарплата 1го менеджера: {zap1}")
    case _ if zap1 > 1000:
        zap1 = 200+zap1*0.08
        print(f"Зарплата 1го менеджера: {zap1}")

match zap2:
    case _ if zap2 < 500:
        zap2 = 200+zap2*0.03
        print(f"Зарплата 2го менеджера: {zap2}")
    case _ if 500 <= zap2 <= 1000:
        zap2 = 200+zap2*0.05
        print(f"Зарплата 2го менеджера: {zap2}")
    case _ if zap2 > 1000:
        zap2 = 200+zap2*0.08
        print(f"Зарплата 2го менеджера: {zap2}")

match zap3:
    case _ if zap3 < 500:
        zap3 = 200+zap3*0.03
        print(f"Зарплата 3го менеджера: {zap3}")
    case _ if 500 <= zap3 <= 1000:
        zap3 = 200+zap3*0.05
        print(f"Зарплата 3го менеджера: {zap3}")
    case _ if zap3 > 1000:
        zap3 = 200+zap3*0.08
        print(f"Зарплата 3го менеджера: {zap3}")

best = max(max(zap1, zap2), zap3)

match best:
    case _ if best == zap1:
        zap1=zap1+200
        print("1му менеджеру начислена пермия в размере 200 $")
    case _ if best == zap2:
        zap2=zap2+200
        print("2му менеджеру начислена пермия в размере 200 $")
    case _ if best == zap3:
        zap3=zap3+200
        print("3му менеджеру начислена пермия в размере 200 $")

print(f"Итого зарплаты менеджеров:\n - 1го - {zap1} $\n - 2го - {zap2} $\n - 3го - {zap3} $")