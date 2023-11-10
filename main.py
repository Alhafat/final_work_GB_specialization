import json
from datetime import datetime
from pathlib import Path
from typing import Any

from Animals import Animals, Pets, PackAnimals


# метод ожидания (пользователь выбирает вернуться ли в предыдущее меню)

def go_back(navigation: "Any"):
    print('Желаете вернуться в предыдущее меню?' + '\n')
    temp = input("Y/n:" + "\n").lower()
    match temp:
        case 'y':
            return eval(navigation)
        case 'n':
            return_main_or_finish()
        case _:
            print("Введено некорректное значение. Попробуйте еще раз.' + '\n'")
            go_back('go_back(navigation: "Any")')


# метод ожидания (пользователь выбирает продолжать ли работу с программой/выйти в главное меню)

def return_main_or_finish():
    print("\n" + "Желаете продолжить работу программы?" + "\n")
    temp = input("Y/n:" + "\n").lower()
    match temp:
        case 'y':
            main()
        case 'n':
            exit("Конец программы. До новых встреч!")
        case _:
            print("Введено некорректное значение. Попробуйте еще раз.' + '\n'")
            return_main_or_finish()


# метод сортирует по дате и производит вывод
def sort_by_date():
    type_name = choose_type_pets()
    match type_name:
        case 1:
            path = Path('pets.json')
            data = json.loads(path.read_text(encoding='utf-8'))
            print(sorted(data, key=lambda x: (x[6].split('.')[::-1], x[-1])))
        case 2:
            path = Path('pack animals.json')
            data = json.loads(path.read_text(encoding='utf-8'))
            print(sorted(data, key=lambda x: (x[6].split('.')[::-1], x[-1])))
    go_back('sort_by_date()')


# метод реализует функцию выбора класса питомца для последующей работы
def choose_type_pets():
    print("Известные типы питомцев:")
    Animals.show_all_types()
    try:
        animal_type = int(input('\n' + "Выберите тип питомца:" + '\n'))
        if animal_type > Animals.get_all_types():  # проверяем введено ли значение в диапазоне
            print("Класс в реестре не найден. "
                  "Для создания нового класса питомцев обратитесь пожалуйста к разработчику.")
            return_main_or_finish()
        match animal_type:
            case 1:  # домашние
                # Animals.show_all_animals(Pets.pets_animals, Pets.name_type)
                return animal_type
            case 2:  # парнокопытные
                # Animals.show_all_animals(PackAnimals.pack_animals, PackAnimals.name_type)
                return animal_type
            case _:
                print('Введено некорректное значение. Попробуйте еще раз.' + '\n')
                choose_type_pets()
    except (ValueError, IndexError):
        print("Введено неверное значение регистрационного номера, попробуйте еще раз!" + "\n")
        choose_type_pets()


# метод для добавления новых команд питомцу

def learn_commands(file_name, number_pet):
    try:
        change_request = input('\n' + 'Желаете внести изменения Y/n?:' + '\n').lower()
        match change_request:
            case 'y':
                temp = input('\n' + "Для добавления в список команд питомца "
                                    "внесите команды через пробел без учета регистра:" + '\n').upper().strip()
                if temp.strip():
                    Animals.add_command_pet(file_name, number_pet)
                    go_back('show_or_learn_commands()')
                else:
                    print('\n' + "Внесение изменений прервано, значения введены не были либо введены неверно.")
                    go_back('show_or_learn_commands()')
            case 'n':
                return_main_or_finish()
            case _:
                print('\n' + 'Такой команды не существует!' +
                      '\n\n' + 'Идет перезапуск программы, пожалуйста подождите...')
                learn_commands(file_name, number_pet)
    except ValueError:
        print('\n' + 'Ошибочное значение!!!' + '\n\n' + 'Идет перезапуск программы, пожалуйста подождите...' + '\n')
        main()


# метод поиска нужного файла при выборе класса - вспомогательный

def name_file_from_type():
    animal_type = choose_type_pets()
    match animal_type:
        case 1:  # домашние питомцы
            temp = Animals.show_all_animals(Pets.pets_animals, Pets.name_type)  # !!! не самый красивый вывод
            empty_class(temp)
            return 'pets'
        case 2:  # парнокопытные
            temp = Animals.show_all_animals(PackAnimals.pack_animals,
                                            PackAnimals.name_type)  # !!! не самый красивый вывод
            empty_class(temp)
            return 'pack animals'


# метод показывает известные команды + при выборе пользователем перебрасывает на добавление новых команд"

def show_or_learn_commands():
    try:
        file_name = name_file_from_type()
        # animal_type = choose_type_pets()
        # match animal_type:
        #     case 1:  # домашние питомцы
        #         temp = Animals.show_all_animals(Pets.pets_animals, Pets.name_type)  # !!! не самый красивый вывод
        #         file_name = 'pets'
        #         empty_class(temp)
        #     case 2:  # парнокопытные
        #         temp = Animals.show_all_animals(PackAnimals.pack_animals,
        #                                         PackAnimals.name_type)  # !!! не самый красивый вывод
        #         file_name = 'pack animals'
        #         empty_class(temp)

        number_pet = int(input('Для посмотра списка доступных команд питомца введите '
                               'его регистрационный номер:' + '\n'))
        match number_pet:
            case 1:  # pets animals
                if number_pet > Animals.all_number_of_pets(file_name):  # проверяем введено ли значение в диапазоне
                    print("Полученный регистрационный номер отсутствует. Пожалуйста проверьте введенное значение.")
                    go_back('show_or_learn_commands()')
                Animals.get_all_command_pets(file_name, number_pet)
                learn_commands(file_name, number_pet)
            case 2:  # pack animals
                if number_pet > Animals.all_number_of_pets(file_name):  # проверяем введено ли значение в диапазоне
                    print("Полученный регистрационный номер отсутствует. Пожалуйста проверьте введенное значение.")
                    go_back('show_or_learn_commands()')
                Animals.get_all_command_pets(file_name, number_pet)
                learn_commands(file_name, number_pet)
        go_back('show_or_learn_commands()')
        return_main_or_finish()
    except (ValueError, IndexError):
        print("Введено неверное значение регистрационного номера, попробуйте еще раз!" + "\n")
        show_or_learn_commands()


# создаем новую запись в реестре питомцев

def new_pet():
    try:
        animal_type = choose_type_pets()
        match animal_type:
            case 1:  # pets animals
                Animals.add_animal('pets')  # добавляет питомца в список класса
                Animals.add_name('pets')  # добавляет только имя питомца в основной список
                return_main_or_finish()
            case 2:  # pack animals
                Animals.add_animal('pack animals')  # добавляет питомца в список класса
                Animals.add_name('pack animals')  # добавляет только имя питомца в основной список
                return_main_or_finish()
    except ValueError:
        print("\n" + "Введено неверное значение типа, попробуйте еще раз!" + "\n")
        new_pet()


# создание нового класса питомцев(пока не реализовано):

def add_new_class_pet():
    print("Для создания нового класса питомцев обратитесь пожалуйста к разработчику.")
    # type = str(input("Введите тип животного: " + "\n")).lower()


# метод показывающий существующие классы питомцев:

def show_types_animals():
    print("Идет получение запрошенных данных..." + "\n")
    print("Известные типы питомцев:")
    Animals.show_all_types()
    go_back('show_types_animals()')


# метод проверяет наличие информации о питомцах(есть ли записи в классе питомцев),
# в случае отстутвия предлагает создание записи - вспомогательный:

def empty_class(temp):
    if temp == 1:
        try:
            print('\n' + 'Желаете внести питомца в реестр?' + '\n')
            change_request = input('Y/n?' + '\n')
            match change_request:
                case 'y':
                    new_pet()
                case 'n':
                    go_back('show_all_animals()')
                    return_main_or_finish()
                case _:
                    print('\n' + 'Такой команды не существует!' +
                          '\n\n' + 'Идет перезапуск программы, пожалуйста подождите...')
                    empty_class(temp)
        except ValueError:
            print('\n' + 'Ошибочное значение!!!' + '\n\n' + 'Идет перезапуск программы, пожалуйста подождите...' + '\n')
            main()
    # else:
    #     return None


# метод показывает общий список питомцев, либо по существующим классам:

def show_all_animals():
    try:
        print('\n' + 'Пожалуйста выберите вариант отображения:' + '\n')
        print('1. Отобразить список животных всех типов.')
        print('2. Отобразить список домашних животных.')
        print('3. Отобразить список парнокопытных животных.')
        print('4. Возврат в основное меню.' + '\n')

        choice = int(input('Введите номер команды:\n'))
        match choice:
            case 1:  # все животные
                print("\n" + "Список питомцев всех типов:")
                temp = Animals.show_all_animals('animals_name', Animals.name_type)  # !!! не самый красивый вывод
                empty_class(temp)
                go_back('show_all_animals()')
                return_main_or_finish()
            case 2:  # домашние питомцы
                print("\n" + "Идет получение запрошенных данных...")
                print("\n" + "Полный список домашних питомцев:")
                temp = Animals.show_all_animals('pets', Pets.name_type)  # !!! не самый красивый вывод
                empty_class(temp)
                go_back('show_all_animals()')
                return_main_or_finish()
            case 3:  # парнокопытные
                print("\n" + "Идет получение запрошенных данных...")
                print("\n" + "Полный список парнокопытных питомцев:")
                temp = Animals.show_all_animals('pack animals', PackAnimals.pack_animals,
                                                PackAnimals.name_type)  # !!! не самый красивый вывод
                empty_class(temp)
                go_back('show_all_animals()')
                return_main_or_finish()
            case 4:
                main()
            case _:
                print('Введена неверная команда, возврат в основное меню... \n')
                show_all_animals()
    except ValueError:
        print('Введена неверная команда, возврат в основное меню... \n')
        show_all_animals()


# метод для выбора действия(команды в консоли) - вспомогательный:

def insert_command():
    print('Что желаете выполнить?' + '\n')
    print('1. Отобразить список животных.')
    print('2. Отобразить известные типы питомцев.')
    print('3. Завести новое животное.')
    print('4. Отобразить список известных команд для животного. Обучить животное новой команде.')
    print('5. Отобразить животных по дате рождения.')
    print('6. Завести новый тип питомца.')
    print('7. Завершить работу программы.\n')
    choice = int(input('Введите номер команды:\n'))
    return choice


# основной метод- запуск приложения и основная навигация:

def main():
    try:
        choice = insert_command()
        match choice:
            case 1:
                show_all_animals()
            case 2:
                show_types_animals()
            case 3:
                new_pet()
            case 4:
                show_or_learn_commands()
            case 5:
                sort_by_date()
            case 6:
                add_new_class_pet()
            case 7:
                exit("Конец программы. До новых встреч!")
            case _:
                print('\n' + 'Такой команды не существует!' +
                      '\n\n' + 'Идет перезапуск программы, пожалуйста подождите...' + '\n')
                main()
    except ValueError:
        print('\n' + 'Ошибочное значение!!!' + '\n\n' + 'Идет перезапуск программы, пожалуйста подождите...' + '\n')
        main()


if __name__ == '__main__':
    print('\n' + 'Добро пожаловать в программу-реестр животных.' + '\n')
    main()
