import random

print("-------------Завдання 1-------------")

lst = [random.randint(-10, 25) for _ in range(10)]
print(f"Список рандомних чисел: {lst} ")

sum_negative = sum(i for i in lst if i < 0)
print(f"Сума від’ємних: {sum_negative}")

sum_even = sum(i for i in lst if i % 2 == 0)
print(f"Сума парних: {sum_even}")

sum_odd = sum(i for i in lst if i % 2 != 0)
print(f"Сума непарних: {sum_odd}")

index_3 = 1
for i in range(0, len(lst), 3):
    index_3 *= lst[i]
print(f"Добуток індексів кратних 3: {index_3}")

min_index = lst.index(min(lst))
max_index = lst.index(max(lst))

start, end = sorted([min_index, max_index])
between_min_max = 1
for num in lst[start + 1:end]:
    between_min_max *= num
print("Добуток між мін і макс:", between_min_max)

first_index = next(i for i, num in enumerate(lst) if num > 0)

reversed_index = list(reversed(range(len(lst))))
last_index = next(i for i in reversed_index if lst[i] > 0)

sum_between_positive = sum(lst[first_index + 1:last_index])
print(f"Сума між першим і останнім додатніми: {sum_between_positive}")  

print("\n-------------Завдання 2-------------")

lst_even = [x for x in lst if x % 2 == 0]
print(f"Парні: {lst_even}")

lst_odd = [x for x in lst if x % 2 != 0]
print(f"Непарні: {lst_odd}")

lst_negative = [x for x in lst if x < 0]
print(f"Від’ємні: {lst_negative}")

lst_positive = [x for x in lst if x > 0]
print(f"Додатні: {lst_positive}")