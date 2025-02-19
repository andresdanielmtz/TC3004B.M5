'''
Seen example of UML diagram in class and its subsequent implementation.
'''

from abc import ABC, abstractmethod


class Company(ABC):
    @abstractmethod
    def create_employee(self):
        pass  # We will override this with polymorphism.

    @abstractmethod
    def create_software(self):
        pass


class Employee(ABC):
    @abstractmethod
    def do_work(self):
        pass


class Developer(Employee):  # lol
    def do_work(self):
        return "Developer is working..."


class Tester(Employee):
    def do_work(self):
        return "Tester is working..."


class Designer(Employee):
    def do_work(self):
        return "Designer is working..."


class GameDevCompany(Company):
    def get_employee(self):
        return [Developer(), Tester(), Designer()]

    def create_software(self):
        print("Providing software for game developer.")


class OutsourcingCompany(Company):
    def get_employee(self):
        return [Developer(), Tester()]


def main():
    game_dev_company = GameDevCompany()

    for employee in game_dev_company.get_employee():
        print(employee.do_work())


if __name__ == "__main__":
    main()
