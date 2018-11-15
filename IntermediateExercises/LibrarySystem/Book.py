from IntermediateExercises.LibrarySystem.Resource import Resource


class Book(Resource):
    def __init__(self, resource_id, price, description, author, title):
        Resource.__init__(self, resource_id, price, description)
        self.author = author
        self.title = title

    def to_string(self):
        return "ID: " + str(self.resource_id) + ", Price: " \
               + str(self.price) + ", Description: " + str(self.description) \
                + ", Author: " + str(self.author) + ", Title: " + str(self.title) \
               + ", Return date: " + str(self.return_date)




