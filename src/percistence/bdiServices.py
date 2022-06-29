from abc import ABC


class BDIAbstract(ABC):
    def connect(self):
        pass
    def execute(self, query, parameters) -> bool:
        pass
    def getOne(self, query, parameters) -> dict:
        pass
    def getAll(self, query, parameters) -> list:
        pass
    

class MySQLConnection:
    def _init_(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
    
    def connect(self):
        return f'Connecting to MySQL Server: {self.host}'

    def execute(self, query, parameters):
        return f'Executing query: {query}'