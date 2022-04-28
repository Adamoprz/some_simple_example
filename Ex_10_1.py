# MRO - Method Resolution Order; diamond problem

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name):
        self.name = name



    @abstractmethod
    def calc_area(self):
        raise NotImplementedError

class Square(Shape):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def calc_area(self):
        return self.length ** 2


s = Shape()