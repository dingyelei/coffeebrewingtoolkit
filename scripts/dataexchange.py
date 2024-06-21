from dataaccessor import DataAccessor
from models import CoffeeRepository

class DataExchange:

    def __init__(self, **param):
        self.data_accessor = DataAccessor.get_data_accessor(**param)
        
    def get_coffee_repositories(self, index):
        data = self.get_raw_data(index)
        return [CoffeeRepository(**item) for item in data]
    
    def get_raw_data(self, index):
        (schema, raw_data) = self.data_accessor.fetch_data(index)
        return [dict(zip(schema, item)) for item in raw_data]
        
if __name__ == '__main__':
    data_exchange = DataExchange(
        data_accessor = "SQLite",
        db_file = "...../example.db"
        )
    coffee_repositories  = data_exchange.get_coffee_repositories("coffee_repositories")
    for repository in coffee_repositories:
        print(repository)