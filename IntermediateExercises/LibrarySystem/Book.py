from IntermediateExercises.LibrarySystem.Resource import Resource


class Book(Resource):
    def __init__(self, resource_id, price, description, author, title):
        Resource.__init__(self, resource_id, price, description)
        self.author = author
        self.title = title



