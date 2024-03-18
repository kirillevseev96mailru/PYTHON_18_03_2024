class Animal:
    def __init__(self, name, commands, dateofbirthday):
        self.name = name
        self.commands = commands
        self.dateofbirthday = dateofbirthday

    def learn_command(self, new_command):
        self.commands = self.commands + ', ' + new_command

    def what_commands(self):
        return f'Команды: "{self.commands}"; принадлежат - {self.name}'

    def __repr__(self):
        return f'Имя - {self.name}\nКоманды - "{self.commands}"\n'


class Pets(Animal):
    def __init__(self, colour, *args):
        self.colour = colour
        super().__init__(*args)


class PackAnimals(Animal):
    def __init__(self, fast_or_not, *args):
        self.fast_or_not = fast_or_not
        super().__init__(*args)


class Dog(Pets):
    def __init__(self, breed, *args):
        self.breed = breed
        super().__init__(*args)

    def __repr__(self):
        return f'Имя - {self.name}\nКоманды - "{self.commands}"\nПорода - {self.breed}\nЦвет - {self.colour}\n'


class Cat(Pets):
    def __init__(self, breed, *args):
        self.breed = breed
        super().__init__(*args)

    def __repr__(self):
        return f'Имя - {self.name}\nКоманды - "{self.commands}"\nПорода - {self.breed}\nЦвет - {self.colour}\n'


class Hamster(Pets):
    def __init__(self, size, *args):
        self.size = size
        super().__init__(*args)

    def __repr__(self):
        return f'Имя - {self.name}\nКоманды - "{self.commands}"\nРазмерчик - {self.size}\nЦвет - {self.colour}\n'


class Horse(PackAnimals):
    def __init__(self, breed, *args):
        self.breed = breed
        super().__init__(*args)

    def __repr__(self):
        return f'Имя - {self.name}\nКоманды - "{self.commands}"\nПорода - {self.breed}\nБыстрое или нет - {self.fast_or_not}\n'


class Camel(PackAnimals):
    def __init__(self, size, *args):
        self.size = size
        super().__init__(*args)

    def __repr__(self):
        return f'Имя - {self.name}\nКоманды - "{self.commands}"\nРазмерчик - {self.size}\nБыстрое или нет  - {self.fast_or_not}\n'


class Donkey(PackAnimals):
    def __init__(self, load_capacity, *args):
        self.load_capacity = load_capacity
        super().__init__(*args)

    def __repr__(self):
        return f'Имя - {self.name}\nКоманды - "{self.commands}"\nГрузоподъемность - {self.load_capacity}\nБыстрое или нет  - {self.fast_or_not}\n'

