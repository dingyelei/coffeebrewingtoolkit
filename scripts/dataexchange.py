from dataaccessor import DataAccessor
from models import Coffee
from models import Barista
from models import Brewing

class DataExchange:

    def __init__(self, **param):
        self.data_accessor = DataAccessor.get_data_accessor(**param)
        
    def get_coffees(self, index):
        data = self.get_raw_data(index)
        return [Coffee(**item) for item in data]
    
    def get_baristas(self, index):
        data = self.get_raw_data(index)
        return [Barista(**item) for item in data]
    
    def get_brewings(self, index):
        data = self.get_raw_data(index)
        return [Brewing(**item) for item in data]

    def get_raw_data(self, index):
        (schema, raw_data) = self.data_accessor.fetch_data(index)
        return [dict(zip(schema, item)) for item in raw_data]
    