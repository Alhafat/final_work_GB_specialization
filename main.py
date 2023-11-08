from Animals import Animals, Pets, PackAnimals


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


def show_commands():
    print('\n' + "Идет получение запрошенных данных..." + "\n")
    print("Известные типы питомцев:")
    Animals.show_all_types()
    try:
        animal_type = int(input('\n' + "Введите порядковый номер типа питомца:" + '\n'))
        if animal_type > Animals.get_all_types():  # проверяем введено ли значение в диапазоне
            print("Класс в реестре не найден. "
                  "Для создания нового класса питомцев обратитесь пожалуйста к разработчику.")
            waiting_for_the_command()
        match animal_type:
            case 1:
                Animals.show_all_animals(Pets.pets_animals)
            case 2:
                Animals.show_all_animals(PackAnimals.pack_animals)
        number = int(input('Для посмотра списка доступных команд питомца введите '
                           'его регистрационный номер:' + '\n'))
        match number:
            case 1:  # pets animals
                if number > Animals.all_number_of_pets('pets'):  # проверяем введено ли значение в диапазоне
                    print("Полученный регистрационный номер отсутствует. Пожалуйста проверьте введенное значение.")
                    waiting_for_the_command()
                Animals.get_all_command_pets('pets', number)
                waiting_for_the_command()
            case 2:  # pack animals
                if number > Animals.all_number_of_pets('pack animals'):  # проверяем введено ли значение в диапазоне
                    print("Полученный регистрационный номер отсутствует. Пожалуйста проверьте введенное значение.")
                    waiting_for_the_command()
                Animals.get_all_command_pets('pack animals', number)
                waiting_for_the_command()
    except (ValueError, IndexError):
        print("Введено неверное значение регистрационного номера, попробуйте еще раз!" + "\n")
        show_commands()


def new_pet():
    print("Доступные типы питомцев:\n")
    Animals.show_all_types()
    try:
        animal_type = int(input('\n' + "Введите порядковый номер типа питомца:" + '\n'))
        if animal_type > len(Animals.get_all_types()):  # проверяем введено ли значение в диапазоне
            print("Класс в реестре не найден. "
                  "Для создания нового класса питомцев обратитесь пожалуйста к разработчику.")
            waiting_for_the_command()
        match animal_type:
            case 1:  # pets animals
                Animals.add_animal('pets')
                Animals.add_name('pets')
                waiting_for_the_command()
            case 2:  # pack animals
                Animals.add_animal('pack animals')
                Animals.add_name('pack animals')
                waiting_for_the_command()
    except ValueError:
        print("\n" + "Введено неверное значение типа, попробуйте еще раз!" + "\n")
        new_pet()


def add_new_class_pet():
    print("Для создания нового класса питомцев обратитесь пожалуйста к разработчику.")
    # type = str(input("Введите тип животного: " + "\n")).lower()


def show_types_animals():
    print("Идет получение запрошенных данных..." + "\n")
    print("Известные типы питомцев:")
    Animals.show_all_types()
    waiting_for_the_command()


def show_all_animals():
    try:
        print('Пожалуйста выберите вариант отображения:' + '\n')
        print('1. Отобразить список животных всех типов.')
        print('2. Отобразить список домашних животных.')
        print('3. Отобразить список парнокопытных животных.')
        print('4. Вернуться в главное меню.')
        print('5. Завершить работу программы.' + '\n')
        choice = int(input('Введите номер команды:\n'))
        match choice:
            case 1:
                print("\n" + "Список питомцев всех типов:")
                Animals.show_all_animals(Animals.all_animals)  # !!! не самый красивый вывод
                waiting_for_the_command()
            case 2:
                print("\n" + "Идет получение запрошенных данных...")
                print("\n" + "Полный список домашних питомцев:")
                Animals.show_all_animals(Pets.pets_animals)  # !!! не самый красивый вывод
                waiting_for_the_command()
            case 3:
                print("\n" + "Идет получение запрошенных данных...")
                print("\n" + "Полный список парнокопытных питомцев:")
                Animals.show_all_animals(PackAnimals.pack_animals)  # !!! не самый красивый вывод
                waiting_for_the_command()
            case 4:
                main()
            case 5:
                exit("Конец программы. До новых встреч!")
    except ValueError:
        print('Введена неверная команда, возврат в основное меню... \n')
        show_all_animals()


def insert_command():
    print('1. Отобразить список животных.')
    print('2. Отобразить известные типы животных.')
    print('3. Завести новое животное.')
    print('4. Отобразить список известных команд для животного.')
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
            show_commands()
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            add_new_class_pet()
        elif choice == 8:
            exit("Конец программы. До новых встреч!")
        else:
            print(
                '\n' + 'Такой команды не существует!' + '\n\n' + 'Идет перезапуск программы, пожалуйста подождите...' + '\n')
            main()
    except ValueError:
        print('\n' + 'Ошибочное значение!!!' + '\n\n' + 'Идет перезапуск программы, пожалуйста подождите...' + '\n')
        main()


if __name__ == '__main__':
    main()
