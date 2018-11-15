from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, person_id, name, age):
        self.person_id = person_id
        self.name = name
        self.age = age

    @abstractmethod
    def to_string(self):
        pass





