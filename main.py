from Animals import Animals, Pets, PackAnimals


def waiting_for_the_command():
    print("\n" + "Желаете продолжить работу программы?" + "\n")
    temp = input("Y/n:" + "\n").lower()
    if temp == 'y':
        main()
    elif temp == 'n':
        exit("Конец программы. До новых встреч!")
    else:
        print("Введенное значение неверно, попробуйте еще раз!")
        waiting_for_the_command()


def choose_type_pets():
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
                return animal_type
            case 2:
                Animals.show_all_animals(PackAnimals.pack_animals)
                return animal_type
    except (ValueError, IndexError):
        print("Введено неверное значение регистрационного номера, попробуйте еще раз!" + "\n")
        choose_type_pets()


def learn_commands(file_name, number_pet):
    try:
        change_request = input('\n' + 'Желаете внести изменения Y/n?:' + '\n').lower()
        if change_request == 'y' or change_request == 'n':
            match change_request:
                case 'y':
                    temp = input('\n' + "Для добавления в список команд питомца "
                                        "внесите команды через пробел без учета регистра:" + '\n').upper().strip()
                    if temp.strip():
                        Animals.add_command_pet(file_name, number_pet, temp)
                        waiting_for_the_command()
                    else:
                        print('\n' + "Внесение изменений прервано, значения введены не были либо введены неверно.")
                        waiting_for_the_command()
                case 'n':
                    waiting_for_the_command()
        else:
            print('\n' + 'Такой команды не существует!' +
                  '\n\n' + 'Идет перезапуск программы, пожалуйста подождите...')
            learn_commands(file_name, number_pet)
    except ValueError:
        print('\n' + 'Ошибочное значение!!!' + '\n\n' + 'Идет перезапуск программы, пожалуйста подождите...' + '\n')
        main()


def show_or_learn_commands():
    print('\n' + "Идет получение запрошенных данных..." + "\n")
    choose_type_pets()
    try:
        number_pet = int(input('Для посмотра списка доступных команд питомца введите '
                               'его регистрационный номер:' + '\n'))
        match number_pet:
            case 1:  # pets animals
                file_name = 'pets'
                if number_pet > Animals.all_number_of_pets('pets'):  # проверяем введено ли значение в диапазоне
                    print("Полученный регистрационный номер отсутствует. Пожалуйста проверьте введенное значение.")
                    waiting_for_the_command()
                Animals.get_all_command_pets(file_name, number_pet)
                learn_commands(file_name, number_pet)
            case 2:  # pack animals
                file_name = 'pack animals'
                if number_pet > Animals.all_number_of_pets(file_name):  # проверяем введено ли значение в диапазоне
                    print("Полученный регистрационный номер отсутствует. Пожалуйста проверьте введенное значение.")
                    waiting_for_the_command()
                Animals.get_all_command_pets(file_name, number_pet)
                learn_commands(file_name, number_pet)
    except (ValueError, IndexError):
        print("Введено неверное значение регистрационного номера, попробуйте еще раз!" + "\n")
        show_or_learn_commands()


def new_pet():
    animal_type = choose_type_pets()
    try:
        match animal_type:
            case 1:  # pets animals
                Animals.add_animal('pets')  # добавляет питомца в список класса
                Animals.add_name('pets')    # добавляет только имя питомца в основной список
                waiting_for_the_command()
            case 2:  # pack animals
                Animals.add_animal('pack animals')  # добавляет питомца в список класса
                Animals.add_name('pack animals')    # добавляет только имя питомца в основной список
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


def empty_class(temp):
    if temp == 1:
        try:
            print('\n' + 'Желаете внести питомца в реестр?' + '\n')
            change_request = input('Y/n?' + '\n')
            if change_request == 'y' or change_request == 'n':
                match change_request:
                    case 'y':
                        new_pet()
                    case 'n':
                        waiting_for_the_command()
            else:
                print('\n' + 'Такой команды не существует!' +
                      '\n\n' + 'Идет перезапуск программы, пожалуйста подождите...')
                empty_class(temp)
        except ValueError:
            print('\n' + 'Ошибочное значение!!!' + '\n\n' + 'Идет перезапуск программы, пожалуйста подождите...' + '\n')
            main()
    else:
        return None


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
            case 1:                                                                         #все животные
                print("\n" + "Список питомцев всех типов:")
                temp = Animals.show_all_animals(Animals.all_animals)  # !!! не самый красивый вывод
                empty_class(temp)
                waiting_for_the_command()
            case 2:                                                                         #домашние питомцы
                print("\n" + "Идет получение запрошенных данных...")
                print("\n" + "Полный список домашних питомцев:")
                temp = Animals.show_all_animals(Pets.pets_animals)  # !!! не самый красивый вывод
                empty_class(temp)
                waiting_for_the_command()
            case 3:                                                                         #парнокопытные
                print("\n" + "Идет получение запрошенных данных...")
                print("\n" + "Полный список парнокопытных питомцев:")
                temp = Animals.show_all_animals(PackAnimals.pack_animals)  # !!! не самый красивый вывод
                empty_class(temp)
                waiting_for_the_command()
            case 4:
                main()
            case 5:
                exit("Конец программы. До новых встреч!")
            case _:
                print('Введена неверная команда, возврат в основное меню... \n')
                main()
    except ValueError:
        print('Введена неверная команда, возврат в основное меню... \n')
        main()


def insert_command():
    print('1. Отобразить список животных.')
    print('2. Отобразить известные типы животных.')
    print('3. Завести новое животное.')
    print('4. Отобразить список известных команд для животного. Обучить животное новой команде.')
    print('5. Отобразить животных по дате рождения.')
    print('6. Завести новый тип питомца.')
    print('7. Завершить работу программы.\n')
    choice = int(input('Введите номер команды:\n'))
    return choice


def main():
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
            show_or_learn_commands()
        elif choice == 5:
            pass
        elif choice == 6:
            add_new_class_pet()
        elif choice == 7:
            exit("Конец программы. До новых встреч!")
        else:
            print('\n' + 'Такой команды не существует!' +
                  '\n\n' + 'Идет перезапуск программы, пожалуйста подождите...' + '\n')
            main()
    except ValueError:
        print('\n' + 'Ошибочное значение!!!' + '\n\n' + 'Идет перезапуск программы, пожалуйста подождите...' + '\n')
        main()


if __name__ == '__main__':
    main()
