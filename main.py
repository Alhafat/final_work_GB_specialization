from Animals import Animals, Pets, PackAnimals
import json


# with open('animals_name.json', 'w') as outfile:
#     animals_name = {'name': ["CAT_1", "CAT_2"]
#                     }
#     json.dump(animals_name, outfile)
# with open('animals_type.json', 'w') as outfile:
#     animals_type = {'name': ["PETS ANIMALS", "PACK ANIMALS"]}
#     json.dump(animals_type, outfile)
#
# with open('pets.json', 'w') as outfile:
#     pets = {"1": [
#         {"name_animal": ["CAT_1"],
#          "animal_type": ["PETS ANIMALS"],
#          "date_of_birth": ["2022-01-01"],
#          "animal_command": ["meow"]
#          }
#     ]
#     }
#     json.dump(pets, outfile)
#
# with open('pack animals.json', 'w') as outfile:
#     pack_animals = {'1': [
#         {'name_animal': ["HORSE_1"],
#          'animal_type': ['PACK ANIMALS'],
#          'date_of_birth': ['2022-01-01'],
#          'animal_command': ['meow']
#          }
#     ]
#     }
#     json.dump(pack_animals, outfile)


def waiting_for_the_command():
    print("\n" + "Желаете продолжить работу?" + "\n")
    temp = input("Y/n:" + "\n")
    temp = temp.lower()
    if temp == 'y':
        main()
    elif temp == 'n':
        exit("Конец программы. До новых встреч!")
    else:
        print("Введенное значение неверно, попробуйте еще раз!")
        waiting_for_the_command()


def new_pet():
    print("Доступные типы питомцев:\n")
    Animals.show_all_types()
    # print(type(len(Animals.get_all_types())))
    try:
        animal_type = int(input('\n' + "Введите порядковый номер типа питомца:" + '\n'))
        if animal_type > len(Animals.get_all_types()) - 1:  # проверяем введено ли значение в диапазоне
            print("Для создания нового класса питомцев обратитесь пожалуйста к разработчику.")
            waiting_for_the_command()
        match animal_type:
            case 1:  # pets animals
                Pets.add_animal()
                waiting_for_the_command()
            case 2:  # pack animals
                PackAnimals.add_animal()
                waiting_for_the_command()
    except ValueError:
        print("\n" + "Введено неверное значение, попробуйте еще раз!" + "\n")
        new_pet()


def add_new_class_pet():
    print("Для создания нового класса питомцев обратитесь пожалуйста к адмнистратору.")
    # type = str(input("Введите тип животного: " + "\n")).lower()


def show_types_animals():
    print("\n" + "Идет получение запрошенных данных...")
    print("\n" + "Типы питомцев:")
    Animals.show_all_types()
    waiting_for_the_command()


def show_all_animals():
    print('Пожалуйста выберите вариант отображения:' + '\n')
    print('1. Отобразить список животных всех типов.')
    print('2. Отобразить список домашних животных.')
    print('3. Отобразить список парнокопытных животных.')
    print('4. Вернуться в главное меню.')
    print('5. Завершить работу программы.' + '\n')
    choice = int(input('Введите номер команды:\n'))
    if choice == 1:
        print("\n" + "Список питомцев всех типов:")
        Animals.show_all_animals()  # !!! не самый красивый вывод
        waiting_for_the_command()
    elif choice == 2:
        print("\n" + "Идет получение запрошенных данных...")
        print("\n" + "Полный список домашних питомцев:")
        Pets.show_all_animals()  # !!! не самый красивый вывод
        waiting_for_the_command()
    elif choice == 3:
        print("\n" + "Идет получение запрошенных данных...")
        print("\n" + "Полный список парнокопытных питомцев:")
        PackAnimals.show_all_animals()  # !!! не самый красивый вывод
        waiting_for_the_command()
    elif choice == 4:
        main()
    elif choice == 5:
        exit("Конец программы. До новых встреч!")
    else:
        print('Введена неверная команда, возврат в основное меню... \n')
        show_all_animals()


def insert_command():
    print('1. Отобразить список животных.')
    print('2. Отобразить типы животных.')
    print('3. Завести новое животное.')
    print('4. Отобразить список известных команд для животных.')
    print('5. Обучить животное новой команде.')
    print('6. Отобразить животных по дате рождения.')
    print('7. Завести новый тип питомца.')
    print('8. Завершить работу программы.\n')

    choice = int(input('Введите номер команды:\n'))
    return choice


def main():
    pass
    print('\n' + 'Добро пожаловать в программу-реестр животных. Что желаете выполнить?' + '\n')
    try:
        choice = insert_command()
        if choice == 1:
            show_all_animals()
        elif choice == 2:
            show_types_animals()
        elif choice == 3:
            new_pet()
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            add_new_class_pet()
        elif choice == 8:
            exit("Конец программы. До новых встреч!")
        else:
            print('\nТакой команды не существует!\n\nИдет перезапуск программы, пожалуйста подождите...\n')
            main()
    except ValueError:
        print('\nОшибочное значение!!!\n\nИдет перезапуск программы, пожалуйста подождите...\n')
        main()


if __name__ == '__main__':
    main()
