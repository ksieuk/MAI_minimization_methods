from methods.second_part import (
    fletcher_powell,
    fletcher_revees,
    koshi,
    levenberg_marquardt,
    newton,
    newton_modified
)

methods_funcs = {
    '1': fletcher_powell,
    '2': fletcher_revees,
    '3': koshi,
    '4': levenberg_marquardt,
    '5': newton,
    '6': newton_modified
}

methods_ru = {
    '0': 'Закончить работу',
    '1': "Метод Флетчера-Пауэлла",
    '2': "Метод Флетчера-Ривса",
    '3': "Метод Коши",
    '4': "Метод Левенберга-Марквардта",
    '5': "Метод Ньютона",
    '6': "Модифицированный метод Ньютона"
}


def start():
    while True:
        try:
            for key, value in methods_ru.items():
                print(f"{key}: {value}")
            method_number = input('\nВыберите метод из списка. Укажите номер метода: ')

            if method_number not in methods_ru:
                raise ValueError('Метода с таким номером не существует')

            if method_number == '0':
                return print('Работа завершена')

            methods_funcs[method_number].start_input()
        except ValueError as e:
            print(f"=============\nОшибка валидации: {e}\n=============")
        except Exception as e:
            print(f"=============\nОшибка: {e}\n=============")


def main():
    start()


if __name__ == '__main__':
    main()
