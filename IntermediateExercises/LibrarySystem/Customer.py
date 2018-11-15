from IntermediateExercises.LibrarySystem.Person import Person


class Customer(Person):
    def __init__(self, person_id, name, age, number_of_resources):
        Person.__init__(self, person_id, name, age)
        self.name = name
        self.age = age
        self.number_of_resources = number_of_resources

    def to_string(self):
        return "ID: " + str(self.person_id) + ", Name: " \
               + str(self.name) + ", Age: " + str(self.age) \
                + ", Number of resources: " + str(self.number_of_resources)

