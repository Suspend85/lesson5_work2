documents = [{
    "type": "passport",
    "number": "2207 876234",
    "name": "Василий Гупкин"
}, {
    "type": "invoice",
    "number": "11-2",
    "name": "Геннадий Покемонов"
}, {
    "type": "insurance",
    "number": "10006",
    "name": "Аристарх Павлов"
}]
directories = {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': []}


def check_input_num_in_docs(input_num):
    """Function for find number of document in the base"""
    for doc in documents:
        if input_num in doc.values():
            return True  # номер есть в каталоге
    return False  # номера нет в каталоге


def is_str_not_blank(input_str):
    """Function to check the str for blank"""
    return bool(input_str
                and input_str.strip())  # true - если строка не пустая


def person_by_doc(input_num):
    """Function of returning the people name by document number"""
    for doc in documents:  # -------------------вынести в функцию check_input_num_in_docs
        if input_num in doc.values():  # --------/
            return doc['name']
    return


def dir_by_doc(input_num):
    """Function of returning the shelf by document number"""
    for dir, doc in directories.items():
        if input_num in doc:
            return dir
    return


def add_docs(input_num, input_type, input_name, input_dir):
    """Function for add the data to base"""
    res_add = {}
    res_add['type'] = input_type.strip()
    res_add['number'] = input_num.strip()
    res_add['name'] = input_name.strip()
    # если номер документа пусто - вернем значение
    if not is_str_not_blank(input_num):
        return input_num
    # если номер полки пустой - вернем значение
    if not is_str_not_blank(input_dir):
        return input_dir
    if input_dir.isdigit() and 0 < int(input_dir) <= len(directories):
        documents.append(res_add)
        directories.setdefault(input_dir.strip(), []).append(input_num.strip())
        return directories  # успешная проверка, добавим документ, вернем directories
    return  # иначе вернем None/False/0


def del_docs(input_num):
    """Function for delete the data from base by document number"""
    for doc in documents:  # ------------------вынести в функцию check_input_num_in_docs
        if input_num.strip() in doc.values():  # ------/
            documents.remove(doc)
            for dir, doc in directories.items():
                if input_num.strip() in doc:
                    doc.remove(input_num.strip())
            return input_num
    return


def move_docs(input_num='', input_dir=''):
    """Function for move the data to other shelf"""
    res = [
        'Такого документа нет в базе', 'Такого документа нет на полках',
        'Номер полки не введен', 'переместить документ не получилось'
    ]
    if not input_dir.strip():
        print(res[2])
        return
    if input_dir not in directories:
        select = input('Построим полку с этим номером  [+ / -]? ')
        if not (select == '+') or not (add_shelf(input_dir)):
            print(res[3])
            return  # ---------------- если не добавляем полку, то возвращаем None/False/0
    res[2] = ''
    if input_num:
        for num_, dir_ in directories.items():
            if input_num in dir_:
                dir_.remove(input_num)
                directories.get(input_dir.strip(),
                                []).append(input_num.strip())
                print(f'Документ №{input_num} перенесен на полку №{input_dir}')
                return True
    for result in res:
        if result:
            print(result)
    return False


def add_shelf(input_dir):
    """Function for add shelf to the shelf list"""
    if is_str_not_blank(input_dir) or input_dir.isdigit():
        if str(input_dir) in directories:
            return
    directories[str(input_dir)] = []
    return True


def i_take_print_res(res):
    """Function for printing results of other functions"""
    if res:
        print(f'\t{res}')
    else:
        print('\tРезультата нет')


def main():
    """-*-\tp – people - команда для поиска имени человека по документу.\n\ts – shelf – команда для поиска полки по номеру документа.\n\tl - list - команда для вывода списка всех документов.\n\td - dir - команда для вывода содержания полок.\n\t+ - add - команда для добавления данных в базу.\n\t- - del - команда для удаления документа из базы.\n\tm - move - команда для перемещения документа на указанную полку\n\tas - add shelf - команда для добавления полки\n\t? - help - команда для вызова справки.\n\tq - quit - команда для выхода из приложения.-*-"""
    print(main.__doc__)
    while True:
        user_input = input('\nВведите команду: ')

        if user_input == 'p' or user_input == 'people':
            person_ = person_by_doc(input('\tВведите номер документа: '))
            i_take_print_res(person_)

        elif user_input == 's' or user_input == 'shelf':
            dir_ = dir_by_doc(input('\tВведите номер документа: '))
            i_take_print_res(dir_)

        elif user_input == 'l' or user_input == 'list':
            for elem in documents:
                print('\t', *elem.values())

        elif user_input == 'd' or user_input == 'dir':
            # print(f'\t{directories}')
            for count, dir in directories.items():
                print(f'\t{count}. {dir}')
            print(documents)
            print(directories)
        elif user_input == '+' or user_input == 'add':
            input_num = input('\tВведите номер документа: ')
            input_type = input('\tВведите тип документа: ')
            input_name = input('\tВведите имя владельца: ')
            input_dir = input(
                f'\tВведите номер полки (целое число) от 1 до {len(directories)}: '
            )
            res_add = add_docs(input_num, input_type, input_name, input_dir)
            if res_add == input_num:
                print(f'\tНомер документа не может быть пустой')
            elif res_add == input_dir:
                print(f'\tНомер полки не может быть пустой')
            elif not res_add:
                print(f'\tОшибка. Полки с номером: {input_dir} не существует, \
                     введите номер полки с 1 по {len(directories)}')
            else:
                print(f'\tДокумент успешно добавлен в базу.\n\t{directories}')
        elif user_input == '-' or user_input == 'del':
            del_ = del_docs(input('\tВведите номер документа: '))
            if not del_:
                print(f'\tТакого документа нет в каталогах, на полках')
            else:
                print(f'\tДокумент №{del_} удален из каталога и с полки')
        elif user_input == 'm' or user_input == 'move':
            move_docs(input('\tВведите номер документа: '),
                      input('\tВведите целевую полку: '))
        elif user_input == 'as' or user_input == 'add shelf':
            as_ = add_shelf(input('\tВведите номер полки: '))
            if not as_:
                print(f'\tполка уже существует.')
            else:
                print(f'\tПолка добавлена')
        elif user_input == '?' or user_input == 'help':
            print(main.__doc__)
        elif user_input == 'q':
            print('\tДо свидания!')
            break


main()