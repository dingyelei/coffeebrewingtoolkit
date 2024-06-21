
class DataAccessor:

    @staticmethod
    def get_data_accessor(**param):    
        data_accessor = None
        match param['data_accessor']:
            case 'SQLite': 
                data_accessor = DataAccessorSQLiteAdapter(param['db_file'])
        return data_accessor

    def __init__(self):
        self.name = "Abstract Data Accessor"

    def __str__(self):
        return self.name
    
    def fetch_data(self, index):
        raise Exception("method not implemented")
    

import sqlite3
from sqlite3 import Error
class DataAccessorSQLiteAdapter(DataAccessor):
    def __init__(self, db_file):
        self.name = "SQLite Data Accessor"
        self.db_file = db_file

    def fetch_data(self, index):
        raw_schema = self.get_schema(index)
        schema = [item for row in raw_schema for item in row]
        return (schema, self.get_data(index))
    
    def get_data(self, table):
        conn = self.create_connection()
        cur = conn.cursor()
        rows = None

        try:
            cur.execute(f"select * from {table}")
            rows = cur.fetchall()
        except Error as e:
                print(e)
        finally:
            if conn:
                conn.close()
        return rows
    
    def get_schema(self, table):
        conn = self.create_connection()
        cur = conn.cursor()
        rows = None

        try:
            cur.execute(f"select name from pragma_table_info('{table}')")
            rows = cur.fetchall()
        except Error as e:
                print(e)
        finally:
            if conn:
                conn.close()
        return rows
    
    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print(e)
        return conn

if __name__ == '__main__':
    da = DataAccessor.get_data_accessor(
        data_accessor = "SQLite",
        db_file = "/Users/yeleiding/workbench/coffee/it/repository/coffeebrewingtoolkit/samples/db/example.db"
    )
    print(da.fetch_data("coffee_repositories"))