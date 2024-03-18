from Animals.Animals import *


class CounterAnimal:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return CounterAnimal(int(self.num) + other)

    def __repr__(self):
        return f'Количество животных изменилось - {self.num}'


animals = []
dog1 = Dog('1', '1', '1', '1', '1')
dog2 = Dog('2', '2', '2', '2', '2')
cat1 = Cat('1', '1', '1', '1', '1')
cat2 = Cat('2', '2', '2', '2', '2')
horses1 = Horse('1', '1', '1', '1', '1')
horses2 = Horse('2', '2', '2', '2', '2')
camel1 = Camel('1', '1', '1', '1', '1')
camel2 = Camel('2', '2', '2', '2', '2')
animals.extend((dog1, dog2, cat1, cat2, horses1, horses2, camel1, camel2))
counter_animal_1 = CounterAnimal(8)


def append_new_animal():
    new_animal = input('Что за животное?\n'
                       'Dog,Cat,Hamster,Horse,Camel,Donkey - ')
    if new_animal == 'Dog':
        specifications = input('Введите характеристики собаки следующим образом:\n'
                               'Порода,Цвет,Имя,Команды,ДР\n')
        arr_spec = specifications.split(',')
        obj = Dog(arr_spec[0], arr_spec[1], arr_spec[2], arr_spec[3], arr_spec[4])
        animals.append(obj)
        return obj, new_animal
    elif new_animal == 'Cat':
        specifications = input('Введите характеристики кошки следующим образом:\n'
                               'Порода,Цвет,Имя,Команды,ДР\n')
        arr_spec = specifications.split(',')
        obj = Cat(arr_spec[0], arr_spec[1], arr_spec[2], arr_spec[3], arr_spec[4])
        animals.append(obj)
        return obj, new_animal
    elif new_animal == 'Hamster':
        specifications = input('Введите характеристики хомяка следующим образом:\n'
                               'Размерчик,Цвет,Имя,Команды,ДР\n')
        arr_spec = specifications.split(',')
        obj = Cat(arr_spec[0], arr_spec[1], arr_spec[2], arr_spec[3], arr_spec[4])
        animals.append(obj)
        return obj, new_animal
    elif new_animal == 'Horse':
        specifications = input('Введите характеристики лошади следующим образом:\n'
                               'Порода,Быстрое или нет,Имя,Команды,ДР\n')
        arr_spec = specifications.split(',')
        obj = Cat(arr_spec[0], arr_spec[1], arr_spec[2], arr_spec[3], arr_spec[4])
        animals.append(obj)
        return obj, new_animal
    elif new_animal == 'Camel':
        specifications = input('Введите характеристики верблюда следующим образом:\n'
                               'Размерчик,Цвет,Имя,Команды,ДР\n')
        arr_spec = specifications.split(',')
        obj = Cat(arr_spec[0], arr_spec[1], arr_spec[2], arr_spec[3], arr_spec[4])
        animals.append(obj)
        return obj, new_animal
    elif new_animal == 'Donkey':
        specifications = input('Введите характеристики верблюда следующим образом:\n'
                               'Грузоподъемность,Цвет,Имя,Команды,ДР\n')
        arr_spec = specifications.split(',')
        obj = Cat(arr_spec[0], arr_spec[1], arr_spec[2], arr_spec[3], arr_spec[4])
        animals.append(obj)
        return obj, new_animal
    else:
        print('Вы ввели непонятное животное...')


def serch_animals_commands():
    name = input(f'******************************************************\n'
          f'Список всех наших животных:\n'
          f'{animals}\n'
          f'******************************************************\n'
          f'Введите имя животного, команды которого вы хотите узнать:')
    print(f'Животные и их команды, имеющие имя - {name}\n')
    for i in range(len(animals)):
        if animals[i].name == name:
            obj = animals[i]
            print(obj.what_commands())
    print(f'******************************************************\n')


def learning_animal_commands():
    name = input(f'********************************************************\n'
                 f'Список всех наших животных:\n'
                 f'{animals}\n'
                 f'********************************************************\n'
                 f'Введите имя животного, команды которого вы хотите изменить:')
    print(f'Животные и их команды, имеющие имя - {name}\n')
    counter = 0
    for i in range(len(animals)):
        if animals[i].name == name:
            counter = counter + 1
            obj = animals[i]
            print(obj.what_commands())
    number_animal = int(input(f'********************************************************\n'
          f'Введит цифру равную порядковому номер животного, от 0 до {counter-1}: '))
    command = str(input('Введит команду которой вы хотите обучить животное: '))
    counter = -1
    for i in range(len(animals)):
        if animals[i].name == name:
            counter = counter + 1
            if number_animal == counter:
                animals[i].learn_command(f'{command}')
                print(f'Вы обучили животное -  {animals[i].name} команде - {command}')
                animals[i].what_commands()
                print(f'********************************************************\n')


def registry_pets():
    while True:
        answer = input(str(f'********************************************************\n'
                           f'На данный момент животных в реестре -  {len(animals)}\n'
                           f'Вы можете:\n'
                           f'1 - добавить новое животное\n'
                           f'2 - узнать команда конкретного животного\n'
                           f'3 - увидеть список животных\n'
                           f'4 - обучить конкретного животного новым командам\n'
                           f'0 - Выйти\n'
                           f'Выбери нужный вам пункт\n'
                           f'********************************************************\n'))

        if answer == '0':
            print('Вы вышли из приложения. До свидания!')
            break
        elif answer == '1':
            obj, new_animal = append_new_animal()
            print(f'Поздравляю! Вы добавили новое животное - {new_animal}\n'
                  f'{counter_animal_1.__add__(1)}\n'
                  f'{obj}\n'
                  f'********************************************************\n')
        elif answer == '2':
            serch_animals_commands()
        elif answer == '3':
            print(f'********************************************************\n'
                  f'Список всех наших животных:\n')
            for i in range(len(animals)):
                print(f'{animals[i]}\n')
            print(f'********************************************************\n')
        elif answer == '4':
            learning_animal_commands()
        else:
            print('Вы ввели неизвестную команду...')


if __name__ == '__main__':
    registry_pets()

