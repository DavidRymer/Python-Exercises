class Person(object):
    def __init__(self, name, occupation, age):
        self.name = name
        self.occupation = occupation
        self.age = age


people = [
    Person("David Rymer", "Software Developer", 21),
    Person("Donny Soldier", "Joiner", 32),
    Person("Donald Trump", "President", 72),
    Person("John Smith", "Plumber", 33),
    Person("Paul Hawkins", "Chemist", 45)
]

file = open("test.txt", "w")

for person in people:
    file.write("Name: " + person.name + "\nOccupation: " + person.occupation + "\nAge: " + str(person.age) + "\n \n")

file.close()

with open("test.txt", "a") as file:
    for person in people:
        file.write(
            "Name: " + person.name + "\nOccupation: " + person.occupation + "\nAge: " + str(person.age) + "\n \n")
