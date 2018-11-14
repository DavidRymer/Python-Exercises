from IntermediateExercises.LibrarySystem.Resource import Resource


class Newspaper(Resource):
    def __init__(self, resource_id, price, description, date):
        Resource.__init__(self, resource_id, price, description)
        self.date = date
