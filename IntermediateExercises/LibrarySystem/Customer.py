from IntermediateExercises.LibrarySystem.Person import Person


class Customer(Person):
    def __init__(self, person_id, name, age, number_of_resources):
        Person.__init__(self, person_id, name, age)
        self.name = name
        self.age = age
        self.number_of_resources = number_of_resources

