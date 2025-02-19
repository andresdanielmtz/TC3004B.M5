"""
Ejemplo de OOP - M5 Patrones de Diseño
"""

from time import sleep as sl


class Animal:
    def __init__(self, name: str, age: int, gender: str, color: str, weight: float):
        self.name = name
        self.age = age
        self.gender = gender
        self.color = color
        self.weight = weight

    def eat(self, food: str):
        print(f"{self.name} is eating {food}")

    def run(self, destination):
        print(f"{self.name} is running {destination}")

    def breathe(self):
        print(f"{self.name} is breathing")

    def sleep(self, seconds):
        print(f"This animal will sleep for {seconds} seconds.")
        sl(seconds)


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cat(Animal):
    def __init__(
        self, name: str, age: int, gender: str, color: str, weight: float, isNasty: bool
    ):
        super().__init__(name, age, gender, color, weight)
        self.isNasty = isNasty

    def meow(self):
        print("Meow")


class Dog(Animal):
    def __init__(
        self,
        name: str,
        age: int,
        gender: str,
        color: str,
        weight: float,
        bestFriend: Human,
    ):
        super().__init__(name, age, gender, color, weight)
        self.bestFriend = bestFriend

    def bark(self):
        print("Woof")


dawg = Dog(":D", 10, "male", "white", 10.2, Human(":D", 10))
dawg.bark()
