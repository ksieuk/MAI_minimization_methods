from methods.first_part import (
    min,
    newton as newton_min,
    unimod_steps
)

from methods.second_part import (
    fletcher_powell,
    fletcher_revees,
    koshi,
    levenberg_marquardt,
    newton,
    newton_modified
)

methods_funcs = {
    '1': min,
    '2': newton_min,
    '3': unimod_steps,
    '4': fletcher_powell,
    '5': fletcher_revees,
    '6': koshi,
    '7': levenberg_marquardt,
    '8': newton,
    '9': newton_modified,
}

methods_ru = {
    '1': 'Минимизация: Равномерный поиск, Метод половинного деления, Метод золотого сечения',
    '2': 'Метод Ньютона-Рафсона, Метод Больцано, Метод секущих',
    '3': 'Интервал унимодальности: С постоянным шагом, пропорциональным шагом, С шагом Свенна',
    '4': 'Метод Флетчера-Пауэлла',
    '5': 'Метод Флетчера-Ривса',
    '6': 'Метод Коши',
    '7': 'Метод Левенберга-Марквардта',
    '8': 'Метод Ньютона',
    '9': 'Модифицированный метод Ньютона',
    '0': 'Закончить работу',
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
        print('\n==================================\n')


def main():
    start()


if __name__ == '__main__':
    main()
