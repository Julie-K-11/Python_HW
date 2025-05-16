import random

lst_1 = [random.randint(1, 10) for _ in range(5)] 
print(lst_1)

lst_2 = [random.randint(1, 10) for _ in range(5)]
print(lst_2)

lst_3 = lst_1 + lst_2
print(f"Об'єднання списків: {lst_3}")

lst_4 = list(set(lst_1 + lst_2))
print(f"Об'єднання без повторень: {lst_4}")

lst_5 = list(set(lst_1) & set(lst_2))
print(f"Спільні елементи: {lst_5}")

lst_6 = list(set(lst_1) ^ set(lst_2))
print(f"Унікальні елементи: {lst_6}")

lst_7 = [min(lst_1), max(lst_1), min(lst_2), max(lst_2)]
print(f"Мінімум і максимум: {lst_7}")