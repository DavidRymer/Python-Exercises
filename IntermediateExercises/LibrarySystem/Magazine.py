from IntermediateExercises.LibrarySystem.Resource import Resource


class Magazine(Resource):
    def __init__(self, resource_id, price, description, publisher):
        Resource.__init__(self, resource_id, price, description)
        self.publisher = publisher

    def to_string(self):
        return "ID: " + str(self.resource_id) + ", Price: " \
               + str(self.price) + ", Description: " + str(self.description) \
                + ", Publisher: " + str(self.publisher) + ", Return date: " + str(self.return_date)
