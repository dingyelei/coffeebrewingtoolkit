
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
    
    def fetch_data(self, index, **param):
        raise Exception("method not implemented")

import sqlite3
from sqlite3 import Error
class DataAccessorSQLiteAdapter(DataAccessor):
    def __init__(self, db_file):
        self.name = "SQLite Data Accessor"
        self.db_file = db_file

    def fetch_data(self, index, **param):
        raw_schema = self.get_schema(index)
        schema = [item for row in raw_schema for item in row]
        return (schema, self.get_data(index, **param))
    
    def get_data(self, table, **param):
        conn = self.create_connection()
        cur = conn.cursor()
        rows = None

        condition = ''
        for key in param.keys():
            condition += f" {key}='{param[key]}'"
        
        sql = f"select * from {table}"
        if condition != '':
            sql = f"select * from {table} where{condition}"
        # print(f"SQL: {sql}")

        try:
            cur.execute(sql)
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