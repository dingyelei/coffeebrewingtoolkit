from dataaccessor import DataAccessor
from dataaccessor import DataAccessorSQLiteAdapter

class DataExchange:

    def __init__(self, **param):
        self.data_accessor = DataAccessor.get_data_accessor(**param)
        
    def get_coffee_repositories(self, index):
        (schema, raw_data) = self.data_accessor.fetch_data(index)

        data = []
        for item in raw_data:
            data.append(dict(zip(schema, item)))

        print(data)

        coffee_repositories = None
        return coffee_repositories

if __name__ == '__main__':
    de = DataExchange(
        data_accessor = "SQLite",
        db_file = "/Users/yeleiding/workbench/coffee/it/repository/coffeebrewingtoolkit/samples/db/example.db"
        )
    print(de.get_coffee_repositories("coffee_repositories"))