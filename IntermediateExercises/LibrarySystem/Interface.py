from IntermediateExercises.LibrarySystem.InterfaceLogic import *


def interface():
    choice = input("Would you like to: \nA) Add a resource. "
                   " \nB) Remove a resource. "
                   "\nC) Add a person. "
                   "\nD) Remove a person. \n").upper()

    if choice == "A":
        add_resource()
    elif choice == "B":
        remove_resource()
    elif choice == "C":
        add_person()
    elif choice == "D":
        remove_person()
    else:
        print("Please choose one of the options")
        interface()

    end_prompt()


def add_resource():
    choice = input("Would you like to: \nA) Add a book. "
                   " \nB) Add a newspaper "
                   "\nC) Add a magazine. \n").upper()

    if choice == "A":
        add_book()
    elif choice == "B":
        add_newspaper()
    elif choice == "C":
        add_magazine()
    else:
        print("Please choose one of the options")
        add_resource()


def add_person():
    choice = input("Would you like to: \nA) Add a customer. "
                   " \nB) Add an employee. \n").upper()

    if choice == "A":
        add_customer()
    elif choice == "B":
        add_employee()
    else:
        print("Please choose one of the options.")
        add_person()


def end_prompt():
    choice = input("Would you like to: \nA) Continue."
                   " \nB) Logout. \n").upper()

    if choice == "A":
        interface()
    elif choice == "B":
        print("Goodbye.")
    else:
        print("Please choose one of the options")
        end_prompt()


interface()
