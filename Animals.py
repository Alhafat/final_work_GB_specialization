import json
from pathlib import Path
from datetime import datetime


class Animals:
    with open("animals_name.json") as file:
        all_animals = json.load(file)
        file.close()

    with open("animals_type.json") as file:
        class_type = json.load(file)
        file.close()

    name_type = 'Все питомцы:'

    def __init__(self, all_animals, class_type):
        self.all_animals = json.dumps(all_animals)  # список животных всех типов
        self.class_type = json.dumps(class_type)  # список доступных групп животных

    def add_class_type(self, new_class):
        pass
        # self.animal_type.append(new_class)  # добавление нового класса

    @staticmethod
    def show_all_animals(name_all_animals, name_type):
        if not name_all_animals:
            print('\n' + 'Идет получение данных... Запрошенные питомцы в реестре отсутствуют.')
            return 1
        else:
            print('\n' + 'Идет получение запрошенных данных...' + '\n')
            print('\n' + 'Получен список питомцев:' + '\n')
            print(f'{name_type}:' + '\n')
            for animal in name_all_animals:
                print(f'{animal}' + '\n')

    @staticmethod
    def all_number_of_pets(file_name):
        with open(f"{file_name}.json") as file:
            data = json.load(file)
            return len(data)

    @staticmethod
    def get_all_command_pets(file_name, number_pet):
        with open(f"{file_name}.json") as file:
            animals = json.load(file)
            print(animals[number_pet - 1][-1])

    @staticmethod
    def add_command_pet(file_name, number_pet, new_command):
        path = Path(f'{file_name}.json')
        data = json.loads(path.read_text(encoding='utf-8'))
        data[number_pet - 1][-1] += ' ' + new_command
        path.write_text(json.dumps(data, indent=4), encoding='utf-8')
        print('Данные успешно обновлены.' + '\n')

    @staticmethod
    def show_all_types():
        with open("animals_type.json", 'r') as file:
            class_type = json.load(file)
            i = 1
            for animal_type in class_type:
                print(f"{i}. {animal_type}")
                i += 1

    @staticmethod
    def get_all_types():
        with open("animals_type.json") as file:
            class_type = json.load(file)
        return len(class_type)

    @staticmethod
    def add_name(file_name):
        with open(f'{file_name}.json', 'r') as file:
            date = json.load(file)
            value = (date[-1][0], date[-1][2])
        path = Path('animals_name.json')
        data = json.loads(path.read_text(encoding='utf-8'))
        data.append(value)
        path.write_text(json.dumps(data, indent=4), encoding='utf-8')
        print("\n" + "Питомец успешно добавлен к учету." + "\n")

    @staticmethod
    def get_date_input():
        while True:
            try:
                date_input = input("Введите дату в формате ГГГГ.ММ.ДД.:" + '\n')
                date = datetime.strptime(date_input, "%Y.%m.%d").date()
                return json.dumps(date, indent=4, sort_keys=True, default=str)
            except ValueError:
                print("Некорректный формат даты. Пожалуйста, попробуйте снова.")


    @staticmethod
    def add_animal(file_name):
        with open(f"{file_name}.json", 'r') as file:
            pack_animals = json.load(file)
            last_key = len(pack_animals) + 1  # увеличиваем последний ключ для следующей сроки json
            file.close()

            path = Path(f'{file_name}.json')
            data = json.loads(path.read_text(encoding='utf-8'))
            data.append([f'#{last_key}',
                         "name_animal", input("Введите имя питомца без учета регистра: " + "\n").upper(),
                         "animal_type", "PACK ANIMALS",
                         "date_of_birth", Animals.get_date_input(),
                         "animal_command", input("Введите доступные команды для "
                                                 "питомца через пробел без учета регистра:" + "\n").upper()
                         ])
            path.write_text(json.dumps(data, indent=4), encoding='utf-8')


class Pets(Animals):
    with open("pets.json") as file:
        pets_animals = json.load(file)
        file.close()

    name_type = 'Домашние питомцы'

    def __init__(self, name_animal, animal_type, date_of_birth):
        super().__init__(name_animal, animal_type)
        self.name = name_animal
        self.animal_type = animal_type
        self.date_of_birth = date_of_birth
        self.pets_animals = []  # список всех животных
        self.animal_command = []  # пустой список для заполнения текста команд

    def remember(self, text):
        self.animal_command.append(text)  # добавляем новую команду в список

    def retell(self):
        print(' '.join(self.animal_command))  # вывод всех известных комманд

    def add_animals(self, new_animal):
        self.pets_animals.append(new_animal)  # добавить новое животное в список


class PackAnimals(Animals):
    with open("pack animals.json") as file:
        pack_animals = json.load(file)
        file.close()

    name_type = 'Парнокопытные питомцы'

    def __init__(self, name_animal, animal_type, date_of_birth, class_type):
        super().__init__(class_type)
        self.name = name_animal
        self.animal_type = animal_type
        self.date_of_birth = date_of_birth
        self.class_type = class_type
        self.pack_animals = []  # список всех животных
        self.animal_command = []  # пустой список для заполнения текста команд
