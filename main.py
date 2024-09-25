# Исходные данные:
#
# Есть класс Fighter, представляющий бойца.
# Есть класс Monster, представляющий монстра.
# Игрок управляет бойцом и может выбирать для него одно из вооружений для боя.
# Шаг 1: Создайте абстрактный класс для оружия
#
# Создайте абстрактный класс Weapon, который будет содержать абстрактный метод attack().
# Шаг 2: Реализуйте конкретные типы оружия
#
# Создайте несколько классов, унаследованных от Weapon, например, Sword и Bow. Каждый из этих классов реализует метод attack() своим уникальным способом.
# Шаг 3: Модифицируйте класс Fighter
#
# Добавьте в класс Fighter поле, которое будет хранить объект класса Weapon.
# Добавьте метод change_weapon(), который позволяет изменить оружие бойца.
# Шаг 4: Реализация боя
#
# Реализуйте простой механизм для демонстрации боя между бойцом и монстром, исходя из выбранного оружия.
# Требования к заданию:
#
# Код должен быть написан на Python.
# Программа должна демонстрировать применение принципа открытости/закрытости: новые типы оружия можно легко добавлять, не изменяя существующие классы бойцов и механизм боя.
# Программа должна выводить результат боя в консоль.

from abc import ABC, abstractmethod
class Weapon(ABC):
    @abstractmethod
    def attack(self, fighter, monster):
        pass

class Sword_weapon(Weapon):
    def attack(self, fighter, monster):
        print(f'{fighter1.name} - взял меч')
        print(f'{fighter1.name} - бьет мечом {monster}')



class Bow_weapon(Weapon):
    def attack(self, fighter, monster):
        print(f'{fighter1.name} - взял лук')
        print(f'{fighter1.name} - стреляет из лука в {monster}')


class Monster():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Монстр {self.name}'

class Fighter():
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, weapon):
        self.weapon = weapon

    def fight(self, monster):
        self.weapon.attack(self,monster)
        print('Монстр побежден!!!')


fighter1 = Fighter('Tim', Bow_weapon())
monster1 = Monster('Cmega')
monster2 = Monster('Tery')
fighter1.fight(monster1)

fighter1.change_weapon(Sword_weapon())
fighter1.fight(monster2)



