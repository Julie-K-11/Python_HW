import os.path

print("-------------Завдання 1-------------\n")

class Directory:
    def __init__(self, filename):
        self.filename = filename
        self.records = []
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 5:
                        self.records.append({
                            'Назва фірми': data[0],
                            'Власник': data[1],
                            'Телефон': data[2],
                            'Адреса': data[3],
                            'Рід діяльності': data[4]
                        })

    def save(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            for entry in self.records:
                line = ','.join(entry.values()) + '\n'
                file.write(line)

    def add(self, company_name, owner, phone, address, business_type):
        self.records.append({
            'Назва фірми': company_name,
            'Власник': owner,
            'Телефон': phone,
            'Адреса': address,
            'Рід діяльності': business_type
        })
        self.save()

    def search_by_company_name(self, company_name):
        return [entry for entry in self.records if entry['Назва фірми'] == company_name]

    def search_by_owner(self, owner):
        return [entry for entry in self.records if entry['Власник'] == owner]

    def search_by_phone(self, phone):
        return [entry for entry in self.records if entry['Телефон'] == phone]

    def search_by_business_type(self, business_type):
        return [entry for entry in self.records if entry['Рід діяльності'] == business_type]

    def get_all(self):
        return self.records

def main():
    directory = Directory(os.path.join('data', 'directory.txt'))

    directory.add('White', 'Аліна Вайт', '111111111', 'А 12', 'Продаж')
    directory.add('Blue', 'Анна Блю', '222222222', 'Р 11', 'Маркетинг')

    print("Пошук за назвою: ")
    print(directory.search_by_company_name('White'))

    print("Пошук власником: ")
    print(directory.search_by_owner('Анна Блю'))

    print("Пошук за телефоном: ")
    print(directory.search_by_phone('111111111'))

    print("Пошук за діяльністю: ")
    print(directory.search_by_business_type('Продаж'))

    print("Всі записи:")
    print(directory.get_all())

if __name__ == '__main__':
    main()
