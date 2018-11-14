from IntermediateExercises.LibrarySystem.Library import Library
from IntermediateExercises.LibrarySystem.Book import Book
from IntermediateExercises.LibrarySystem.Newspaper import Newspaper
from IntermediateExercises.LibrarySystem.Magazine import Magazine
from IntermediateExercises.LibrarySystem.Customer import Customer
from IntermediateExercises.LibrarySystem.Employee import Employee

system = Library([], [])


def add_book():
    chosen_id = input("Choose an ID. ")
    chosen_price = input("Choose a price. ")
    chosen_description = input("Choose a description. ")
    chosen_author = input("Choose an author. ")
    chosen_title = input("Choose a title. \n")

    chosen_book = Book(chosen_id, chosen_price, chosen_description, chosen_author, chosen_title)

    global system
    system.add_item(chosen_book)


def add_newspaper():
    chosen_id = input("Choose an ID. ")
    chosen_price = input("Choose a price. ")
    chosen_description = input("Choose a description. ")
    chosen_date = input("Choose a date. \n")

    chosen_newspaper = Newspaper(chosen_id, chosen_price, chosen_description, chosen_date)

    global system
    system.add_item(chosen_newspaper)


def add_magazine():
    chosen_id = input("Choose an ID. ")
    chosen_price = input("Choose a price. ")
    chosen_description = input("Choose a description. ")
    chosen_publisher = input("Choose a publisher. \n")

    chosen_magazine = Magazine(chosen_id, chosen_price, chosen_description, chosen_publisher)

    global system
    system.add_item(chosen_magazine)


def add_customer():
    chosen_id = input("Choose an ID. ")
    chosen_name = input("Choose a name. ")
    chosen_age = input("Choose an age. \n")

    chosen_customer = Customer(chosen_id, chosen_name, chosen_age, 0)

    global system
    system.register_person(chosen_customer)


def add_employee():
    chosen_id = input("Choose an ID. ")
    chosen_name = input("Choose a name. ")
    chosen_age = input("Choose an age. ")
    chosen_salary = input("Choose a salary. \n")

    chosen_employee = Employee(chosen_id, chosen_name, chosen_age, chosen_salary)

    global system
    system.register_person(chosen_employee)


def remove_resource():
    chosen_resource = input("Please enter the ID of the resource you would like to remove. \n")
    global system
    system.remove_item(chosen_resource)


def remove_person():
    chosen_person = input("Please enter the ID of the person you would like to remove. \n")
    global system
    system.delete_person(chosen_person)
