from IntermediateExercises.LibrarySystem.Resource import Resource


class Newspaper(Resource):
    def __init__(self, resource_id, price, description, date):
        Resource.__init__(self, resource_id, price, description)
        self.date = date

    def to_string(self):
        return "ID: " + str(self.resource_id) + ", Price: " \
               + str(self.price) + ", Description: " + str(self.description) \
                + ", Date: " + str(self.date) + ", Return date: " + str(self.return_date)
