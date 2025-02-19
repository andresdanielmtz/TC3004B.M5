'''
Implementation of abstract class through UML diagrams.
'''

from abc import ABC, abstractmethod


class School(ABC):
    @abstractmethod
    def get_teachers(self):
        pass

    @abstractmethod
    def get_subject(self):
        pass


class Teacher:
    @abstractmethod
    def get_info(self):
        pass


class MathTeacher(Teacher):
    def get_info(self):
        return "I am the Math Teacher"


class LiteratureTeacher(Teacher):
    def get_info(self):
        return "I am the Literature Teacher"


class University(School):
    def get_teachers(self):
        return [MathTeacher()]

    def get_subject(self):
        return "There is no subjects yet"


class HighSchool(School):
    def get_teachers(self):
        return [MathTeacher(), LiteratureTeacher()]

    def get_subject(self):
        return "There is no subjects yet"


def main():
    tec_de_monterrey = University()

    for teacher in enumerate(tec_de_monterrey.get_teachers()):
        print(f"Teacher #{teacher[0]}: \t {teacher[1].get_info()}")


if __name__ == "__main__":
    main()
