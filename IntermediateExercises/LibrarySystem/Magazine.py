from IntermediateExercises.LibrarySystem.Resource import Resource


class Magazine(Resource):
    def __init__(self, resource_id, price, description, publisher):
        Resource.__init__(self, resource_id, price, description)
        self.publisher = publisher
