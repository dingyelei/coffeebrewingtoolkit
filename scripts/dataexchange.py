from dataaccessor import DataAccessor
from models import Coffee
from models import Barista
from models import Brewing

class DataExchange:

    def __init__(self, **param):
        self.data_accessor = DataAccessor.get_data_accessor(**param)
        
    def get_coffees(self, **param):
        data = self.get_raw_data('coffees', **param)
        return [Coffee(**item) for item in data]
    
    def get_baristas(self, **param):
        data = self.get_raw_data('baristas', **param)
        return [Barista(**item) for item in data]
    
    def get_brewings(self, **param):
        data = self.get_raw_data('brewings', **param)

        brewings = []
        for item in data:
            brewing = Brewing(**item)
            coffees = self.get_coffees(id=brewing.coffee_id)
            if len(coffees) != 1:
                raise Exception(f'Brewing #{brewing.id} failed to match coffee #{brewing.coffee_id}.')
            brewing.coffee = self.get_coffees(id=brewing.coffee_id)[0]
            brewings.append(brewing)

        return brewings

    def get_raw_data(self, index, **param):
        (schema, raw_data) = self.data_accessor.fetch_data(index, **param)
        return [dict(zip(schema, item)) for item in raw_data]
    