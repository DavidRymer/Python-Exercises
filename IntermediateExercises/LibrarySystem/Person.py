from abc import ABC


class Person(ABC):
    def __init__(self, person_id, name, age):
        self.person_id = person_id
        self.name = name
        self.age = age



