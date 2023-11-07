import json
import re
from pathlib import Path


class Animals:
    with open("animals_name.json") as file:
        all_animals = [json.load(file)]

    with open("animals_type.json") as file:
        class_type = json.load(file)

    def __init__(self, all_animals, class_type):
        self.all_animals = json.dumps(all_animals)  # список животных всех типов
        self.class_type = json.dumps(class_type)  # список доступных групп животных

    def add_class_type(self, new_class):
        pass
        # self.animal_type.append(new_class)  # добавление нового класса

    @staticmethod
    def show_all_animals():
        with open("animals_name.json", 'r') as file:
            all_animals = json.load(file)
            print(f'{all_animals}')

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
        animal_type = []
        with open("animals_type.json") as file:
            class_type = json.load(file)
            for name in class_type:
                animal_type.append(name)
        return animal_type


class Pets(Animals):
    with open("pets.json") as file:
        pets_animals = json.load(file)

    # animal_command = []

    def __init__(self, name_animal, animal_type, date_of_birth, animal_command):
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

    @staticmethod
    def show_all_animals():
        with open("pets.json", 'r') as file:
            pets = json.load(file)
            for pet in pets:
                print(pet)

    @staticmethod
    def add_animal():
        with open("pets.json", 'r+') as file:
            pets = json.load(file)
            key = list(pets[-1].keys())
            last_key = int(key[0]) + 1  # увеличиваем последний ключ для следующей сроки json

            path = Path('pets.json')
            data = json.loads(path.read_text(encoding='utf-8'))
            data.append({f'{last_key}': {
                "name_animal": input("Введите имя питомца: " + "\n").upper(),
                "animal_type": "PETS ANIMALS",
                "date_of_birth": input("Введите дату рождения питомца в формате YYYY-MM-DD:" + "\n"),
                "animal_command": input("Введите доступные команды для питомца:" + "\n").upper()
            }
            })
            path.write_text(json.dumps(data, indent=4), encoding='utf-8')
        print("\n" + "Питомец успешно добавлен к учету." + "\n")


class PackAnimals(Animals):
    with open("pack animals.json") as file:
        pets_animals = json.load(file)

    # animal_command = []

    def __init__(self, name_animal, animal_type, date_of_birth, animal_command, class_type):
        super().__init__(class_type)
        self.name = name_animal
        self.animal_type = animal_type
        self.date_of_birth = date_of_birth
        self.class_type = class_type
        self.pack_animals = []  # список всех животных
        self.animal_command = []  # пустой список для заполнения текста команд

    @staticmethod
    def show_all_animals():
        with open("pack animals.json", 'r') as file:
            pack_animals = json.load(file)
            print(json.dumps(pack_animals))

    @staticmethod
    def add_animal():
        with open("pack animals.json", 'r+') as file:
            pack_animals = json.load(file)
            key = list(pack_animals[-1].keys())
            last_key = int(key[0]) + 1  # увеличиваем последний ключ для следующей сроки json

            path = Path('pack animals.json')
            data = json.loads(path.read_text(encoding='utf-8'))
            data.append({f'{last_key}': {
                "name_animal": input("Введите имя питомца: " + "\n").upper(),
                "animal_type": "PACK ANIMALS",
                "date_of_birth": input("Введите дату рождения питомца в формате YYYY-MM-DD:" + "\n"),
                "animal_command": input("Введите доступные команды для питомца:" + "\n").upper()
            }
            })
            path.write_text(json.dumps(data, indent=4), encoding='utf-8')
        print("\n" + "Питомец успешно добавлен к учету." + "\n")
