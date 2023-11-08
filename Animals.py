import json
from pathlib import Path


class Animals:
    with open("animals_name.json") as file:
        all_animals = json.load(file)

    with open("animals_type.json") as file:
        class_type = json.load(file)

    def __init__(self, all_animals, class_type):
        self.all_animals = json.dumps(all_animals)  # список животных всех типов
        self.class_type = json.dumps(class_type)  # список доступных групп животных

    def add_class_type(self, new_class):
        pass
        # self.animal_type.append(new_class)  # добавление нового класса

    @staticmethod
    def show_all_animals(name_all_animals):
        for animal in name_all_animals:
            print('\n' + 'Идет получение запрошенных данных...' + '\n')
            print('\n' + 'Получен список питомцев:' + '\n')
            print(f'{animal}' + '\n')

    @staticmethod
    def all_number_of_pets(file_name):
        with open(f"{file_name}.json") as file:
            data = json.load(file)
            return len(data)

    @staticmethod
    def get_all_command_pets(file_name, number):
        with open(f"{file_name}.json") as file:
            animals = json.load(file)
            print(animals[number-1][-1])

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
    def add_animal(file_name):
        with open(f"{file_name}.json", 'r') as file:
            pack_animals = json.load(file)
            last_key = len(pack_animals) + 1  # увеличиваем последний ключ для следующей сроки json

            path = Path(f'{file_name}.json')
            data = json.loads(path.read_text(encoding='utf-8'))
            data.append([f'#{last_key}',
                         "name_animal", input("Введите имя питомца: " + "\n").upper(),
                         "animal_type", "PACK ANIMALS",
                         "date_of_birth", input("Введите дату рождения питомца в формате YYYY-MM-DD:" + "\n"),
                         "animal_command", input("Введите доступные команды для питомца:" + "\n").upper()
                         ])
            path.write_text(json.dumps(data, indent=4), encoding='utf-8')

    # def show_commands(self):
    #     with open(f"{file_name}.json", 'r') as file:
    #         pack_animals = json.load(file)
    #         last_key = len(pack_animals) + 1  # увеличиваем последний ключ для следующей сроки json


class Pets(Animals):
    with open("pets.json") as file:
        pets_animals = json.load(file)

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

    # @staticmethod
    # def add_animal():
    #     with open("pets.json", 'r+') as file:
    #         pets = json.load(file)
    #         last_key = len(pets) + 1  # увеличиваем последний ключ для следующей сроки json
    #
    #         path = Path('pets.json')
    #         data = json.loads(path.read_text(encoding='utf-8'))
    #         data.append([f'#{last_key}',
    #                      "name_animal", input("Введите имя питомца: " + "\n").upper(),
    #                      "animal_type", "PETS ANIMALS",
    #                      "date_of_birth", input("Введите дату рождения питомца в формате YYYY-MM-DD:" + "\n"),
    #                      "animal_command", input("Введите доступные команды для питомца:" + "\n").upper()
    #                      ])
    #         path.write_text(json.dumps(data, indent=4), encoding='utf-8')


class PackAnimals(Animals):
    with open("pack animals.json") as file:
        pack_animals = json.load(file)

    # animal_command = []

    def __init__(self, name_animal, animal_type, date_of_birth, class_type):
        super().__init__(class_type)
        self.name = name_animal
        self.animal_type = animal_type
        self.date_of_birth = date_of_birth
        self.class_type = class_type
        self.pack_animals = []  # список всех животных
        self.animal_command = []  # пустой список для заполнения текста команд

    # @staticmethod
    # def add_animal():
    #     with open("pack animals.json", 'r+') as file:
    #         pack_animals = json.load(file)
    #         last_key = len(pack_animals) + 1  # увеличиваем последний ключ для следующей сроки json
    #
    #         path = Path('pack animals.json')
    #         data = json.loads(path.read_text(encoding='utf-8'))
    #         data.append([f'#{last_key}',
    #                      "name_animal", input("Введите имя питомца: " + "\n").upper(),
    #                      "animal_type", "PACK ANIMALS",
    #                      "date_of_birth", input("Введите дату рождения питомца в формате YYYY-MM-DD:" + "\n"),
    #                      "animal_command", input("Введите доступные команды для питомца:" + "\n").upper()
    #                      ])
    #         path.write_text(json.dumps(data, indent=4), encoding='utf-8')
    #
    #         # with open('pack animals.json', 'r'):
    #         date = json.load(file)
    #         value = date[-1][2]
    #         Animals.add_name(value)
