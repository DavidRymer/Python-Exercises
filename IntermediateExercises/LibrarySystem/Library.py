class Library(object):
    def __init__(self, resources, people):
        self.resources = resources
        self.people = people

    def add_item(self, resource):
        self.resources.append(resource)

    def remove_item(self, resource_id):
        for resource in self.resources:
            if resource.resource_id == resource_id:
                self.resources.remove(resource)

    def get_item(self, resource_id):
        for resource in self.resources:
            if resource.resource_id == resource_id:
                return resource

    def register_person(self, person):
        self.people.append(person)

    def delete_person(self, person_id):
        for person in self.people:
            if person.person_id == person_id:
                self.people.remove(person)

    def get_person(self, person_id):
        for person in self.people:
            if person.person_id == person_id:
                return person







