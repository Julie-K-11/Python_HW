print("-------------Завдання 1-------------\n")

basketbolisty = {
    "Майкл Джордан": 170,
    "Мануте Бол": 231,
    "Карім Абдул-Джаббар": 218,
    "Меджик Джонсон": 206
}

print("\n------------Ориганіл")
print(basketbolisty)

basketbolisty["Тім Данкан"] = 211

del basketbolisty["Мануте Бол"]

print("\n------------Після видалення та додавання")
print(basketbolisty)

find_by_name = "Карім Абдул-Джаббар"
if find_by_name in basketbolisty:
    print(f"\nЗнайдено. Зріст {find_by_name}: {basketbolisty[find_by_name]} см")
else:
    print("\nБаскетболіст не знайдений")


basketbolisty["Майкл Джордан"] = 198

print("\n------------Після заміни")
print(basketbolisty)


print("\n-------------Завдання 2-------------\n")

dictionary = {
    "cherry": "cerise",
    "banana": "banana",
    "apple": "pomme",
    "poire": "pear",
    "peach": "pêche"
}

print("\n------------Ориганіл")
print(dictionary)

dictionary["Watermelon"] = "Pastèque"

del dictionary["peach"]

print("\n------------Після видалення та додавання")
print(dictionary)

word = "apple"
if word in dictionary:
    print(f"\nЗнайдено. Французький переклад '{word}': {dictionary[word]}")
else:
    print("\nСлово не знайдено")

dictionary["banana"] = "banane"

print("\n------------Після заміни")
print(dictionary)

print("\n-------------Завдання 3-------------\n")

firma = [
    {"fio":"Tom Donald", "phone": "+111111111", "email": "tom@gmail.com", "position": "Manager", "office": "101", "skype": "manager.tom"},
    {"fio":"Ann Taylor", "phone": "+444444444", "email": "ann@gmail.com", "position": "Programmer", "office": "103", "skype": "programmer.ann"}
]

print("\n------------Оригінал")
print(firma)

firma = [employee for employee in firma if employee["fio"] != "Tom Donald"]

firma.append({
    "fio": "Alina Smith",
    "phone": "+333333333",
    "email": "alina@gmail.com",
    "position": "Designer",
    "office": "103",
    "skype": "designer.alina"
})

print("\n------------Після видалення та додавання")
print(firma)

# Пошук співробітника за ім’ям
employees = "Ann Taylor"
found = False
for employee in firma:
    if employee["fio"] == employees:
        print("\n------------Знайдено співробітника:")
        print(employee)
        found = True
        break
if not found:
    print("\nСпівробітник не знайдений")

# Заміна Skype Анни
for employee in firma:
    if employee["fio"] == "Ann Taylor":
        employee["position"] = "Manager"
        employee["office"] = "101"
        employee["skype"] = "manager.ann"

print("\n------------Після заміни Skype")
print(firma)

print("\n-------------Завдання 4-------------\n")

books = [
    {"title": "The Chronicles of Narnia","author": "C.S. Lewis", "genre": "fantasy", "year": 1950, "pages": 768, "publisher": "HarperCollins"},
    {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "genre": "fantasy", "year": 1997, "pages": 320, "publisher": "Bloomsbury"},
    {"title": "The Shining", "author": "Stephen King", "genre": "horror", "year": 1977, "pages": 447, "publisher": "Doubleday"}
]

print("\n------------Оригінал")
for book in books:
    print(book)

books = [book for book in books if book["title"] != "The Shining"]

books.append({
    "title": "The Green Mile",
    "author": "Stephen King",
    "genre": "drama",
    "year": 1996,
    "pages": 592,
    "publisher": "Scribner"
})

print("\n------------Після видалення та додавання")
for book in books:
    print(book)

search_title = "Harry Potter and the Philosopher's Stone"
found = False
for book in books:
    if book["title"] == search_title:
        print("\n------------Знайдено книгу")
        print(book)
        found = True
        break
if not found:
    print("\nКнигу не знайдено")

for book in books:
    if book["title"] == "Harry Potter and the Philosopher's Stone":
        book["publisher"] = "Scholastic"

print("\n------------Після заміни видавництва")
for book in books:
    print(book)