''' Домашнее задание
Доработаем задачи 5-6 (animals.py). Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.'''

from animals import Animal, Dog, Bird, Fish


class Creator():

    def create_animal(type_animal, name, weight, age, animal_type):
        return type_animal(name, weight, age, animal_type)
    
    # def create_bird(name: str, weight: int, age: int, bird_type: str, sound: str):
    #     return Bird(name, weight, age, bird_type, sound)

    # def create_dog(name: str, weight: int, age: int, dog_type: str):
    #     return Dog(name, weight, age, dog_type)

    # def create_fish(name: str, weight: int, age: int, fish_type: str):
    #     return Fish(name, weight, age, fish_type)


if __name__ == '__main__':
    # jack = AnimalsCreator.create_dog('Джек', 12, 5, 'Питбуль')
    # print(jack)
    # freddy = AnimalsCreator.create_fish('Фредди', 1, 1, 'Камбала')
    # print(freddy)
    first = Creator.create_animal(Fish,'Dory', 30, 4, 'Regal_blue')
    print(first)
