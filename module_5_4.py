class House:
    houses_history = []  # хранение названия созданных объектов

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name  # название
        self.number_of_floors = number_of_floors  # количество этажей

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, int):
            if self.number_of_floors == other:
                return True
        elif isinstance(other, House):
            if self.number_of_floors == other.number_of_floors:
                return True
        return False

    def __lt__(self, other):
        if isinstance(other, int):
            if self.number_of_floors < other:
                return True
        elif isinstance(other, House):
            if self.number_of_floors < other.number_of_floors:
                return True
        return False

    def __le__(self, other):
        if isinstance(other, int):
            if self.number_of_floors <= other:
                return True
        elif isinstance(other, House):
            if self.number_of_floors <= other.number_of_floors:
                return True
        return False

    def __gt__(self, other):
        if isinstance(other, int):
            if self.number_of_floors > other:
                return True
        elif isinstance(other, House):
            if self.number_of_floors > other.number_of_floors:
                return True
        return False

    def __ge__(self, other):
        if isinstance(other, int):
            if self.number_of_floors >= other:
                return True
        elif isinstance(other, House):
            if self.number_of_floors >= other.number_of_floors:
                return True
        return False

    def __ne__(self, other):
        if isinstance(other, int):
            if self.number_of_floors != other:
                return True
        elif isinstance(other, House):
            if self.number_of_floors != other.number_of_floors:
                return True
        return False

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    # ====== Добавление решений по заданию 5_4 ======

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)