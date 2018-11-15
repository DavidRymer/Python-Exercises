from IntermediateExercises.LibrarySystem.Book import Book
from IntermediateExercises.LibrarySystem.Newspaper import Newspaper
from IntermediateExercises.LibrarySystem.Magazine import Magazine
from IntermediateExercises.LibrarySystem.Customer import Customer
from IntermediateExercises.LibrarySystem.Employee import Employee


def load_resources():
    file = open("resources.txt", "r")
    return file.readlines()


def load_people():
    file = open("people.txt", "r")
    return file.readlines()


def get_value(word):
    index = word.find(":") + 2
    return word[index:]


def line_to_book(line):
    values = line.split(", ")
    return Book(get_value(values[0]),
                get_value(values[1]),
                get_value(values[2]),
                get_value(values[3]),
                get_value(values[4])
                )


def line_to_newspaper(line):
    values = line.split(", ")
    return Newspaper(get_value(values[0]),
                     get_value(values[1]),
                     get_value(values[2]),
                     get_value(values[3])
                     )


def line_to_magazine(line):
    values = line.split(", ")
    return Magazine(get_value(values[0]),
                    get_value(values[1]),
                    get_value(values[2]),
                    get_value(values[3])
                    )


def line_to_employee(line):
    values = line.split(", ")
    return Employee(get_value(values[0]),
                    get_value(values[1]),
                    get_value(values[2]),
                    get_value(values[3])
                    )


def line_to_customer(line):
    values = line.split(", ")
    return Customer(get_value(values[0]),
                    get_value(values[1]),
                    get_value(values[2]),
                    get_value(values[3])
                    )


def check_type(line):
    record = line.split(", ")

    if len(record) == 6:
        return "Book"
    elif record[3].find("Date") == 0:
        return "Newspaper"
    elif record[3].find("Publisher") == 0:
        return "Magazine"
    elif record[3].find("Salary") == 0:
        return "Employee"
    elif record[3].find("Number of resources") == 0:
        return "Customer"

