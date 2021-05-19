from pony.orm import Database
from singleton_decorator import singleton

@singleton
class Db():
    def __init__(self):
        self.database = Database()
        self.database.bind(provider='postgres', user='tom', database='cmts', port='5432')
        sql_debug = True

    def getDb(self) -> Database:
        return self.database
