from IntermediateExercises.LibrarySystem.Person import Person


class Employee(Person):
    def __init__(self, person_id, name, age, salary):
        Person.__init__(self, person_id, name, age)
        self.name = name
        self.age = age
        self.salary = salary



