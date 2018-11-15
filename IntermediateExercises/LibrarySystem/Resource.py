from abc import ABC, abstractmethod
from datetime import datetime
from datetime import timedelta


class Resource(ABC):
    def __init__(self, resource_id, price, description):
        self.resource_id = resource_id
        self.price = price
        self.description = description
        self.return_date = None

    def check_out(self):
        self.return_date = datetime.now() + timedelta(days=7)

    def check_in(self):
        self.return_date = None

    @abstractmethod
    def to_string(self):
        pass



