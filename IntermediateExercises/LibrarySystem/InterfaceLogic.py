from IntermediateExercises.LibrarySystem.Library import Library
from IntermediateExercises.LibrarySystem.helper import *

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


def check_in():
    chosen_resource = input("Please enter the ID of the resource you would like to check in. \n")
    global system
    system.get_item(chosen_resource).check_in()


def check_out():
    chosen_resource = input("Please enter the ID of the resource you would like to check out. \n")
    global system
    system.get_item(chosen_resource).check_out()


def show_resources():
    global system

    if not system.resources:
        print("There are currently no resources in the system. \n")
    else:
        for resource in system.resources:
            print(resource.to_string())

    write_resources_to_file()


def show_people():
    global system

    if not system.people:
        print("There are currently no people in the system. \n")
    else:
        for person in system.people:
            print(person.to_string())

    write_people_to_file()


def write_people_to_file():
    choice = input("Would you like to write the current list of people to a file? "
                   "\nA) Yes. "
                   "\nB) No. ").upper()

    if choice == "A":
        global system
        print("You chose to write to the file")
        file = open("people.txt", "a")
        for person in system.people:
            file.write(str(person.to_string()) + "\n")
        file.close()
    elif choice == "B":
        print("You chose not to write to the file")
    else:
        print("Please choose one of the options")
        write_people_to_file()


def write_resources_to_file():
    choice = input("Would you like to write the current list of resources to a file? "
                   "\nA) Yes. "
                   "\nB) No. ").upper()

    if choice == "A":
        global system
        file = open("resources.txt", "a")
        print("You chose to write to the file")
        for resource in system.resources:
            file.write(str(resource.to_string()) + "\n")
        file.close()
    elif choice == "B":
        print("You chose not to write to the file")
    else:
        print("Please choose one of the options")
        write_people_to_file()


def load_resources_from_file():
    global system
    for line in load_resources():
        if check_type(line) == "Book":
            system.resources.append(line_to_book(line))
        elif check_type(line) == "Newspaper":
            system.resources.append(line_to_newspaper(line))
        elif check_type(line) == "Magazine":
            system.resources.append(line_to_magazine(line))


def load_people_from_file():
    global system
    for line in load_people():
        if check_type(line) == "Customer":
            system.people.append(line_to_customer(line))
        elif check_type(line) == "Employee":
            system.people.append(line_to_employee(line))
