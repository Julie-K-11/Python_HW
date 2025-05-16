import random

print("-------------Завдання 1-------------")

text = "Etincidunt sit labore quaerat quaerat sit etincidunt? eius etincidunt magnam adipisci 2 porro modi!!! amet modi dolor neque: quisquam quiquia dolorem neque ipsum, ut modi voluptatem. Numquam tempora velit, non ipsum. Consectetur etincidunt 123 dolore magnam sed dolorem dolore modi! eius quiquia quaerat sit velit. Neque numquam porro eius. Quaerat quisquam quisquam ipsum quiquia. Est sit tempora eius quiquia. Labore sit est adipisci labore. Adipisci 0 porro labore dolorem tempora voluptatem velit dolor."

sentences = []
endings = ['.', '!', '?']
start = 0
for i, ch in enumerate(text):
    if ch in endings:
        sentence = text[start:i+1].strip()
        if sentence:
            sentences.append(sentence[0].upper() + sentence[1:])
        start = i + 1

if start < len(text):
    tail = text[start:].strip()
    if tail:
        sentences.append(tail[0].upper() + tail[1:])

new_text = ' '.join(sentences)
print(f"Текст з великих літер:\n{new_text}")

count_digits = sum(1 for ch in text if ch.isdigit())
print(f"Кількість цифр: {count_digits}")

punctuation = '.,!?;:-'
count_punct = sum(1 for ch in text if ch in punctuation)
print(f"Кількість знаків пунктуації: {count_punct}")

count_exclam = text.count('!')
print(f"Кількість знаків оклику: {count_exclam}")

print("\n-------------Завдання 2-------------")

user_num_lst = [int(x) for x in input("Введіть цілі числа через пробіл: ").split()]
find_num = int(input("Число для пошуку: "))

count = user_num_lst.count(find_num)

print(f"Число зустрічається разів: {count}")

print("\n-------------Завдання 3-------------")

if user_num_lst:
    total = sum(user_num_lst)
    average = total / len(user_num_lst)
    print(f"Сума: {total}")
    print(f"Середнє арифметичне: {average}")
else:
    print("Нічого не введено.")
