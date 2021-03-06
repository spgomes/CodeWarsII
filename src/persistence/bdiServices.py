from abc import ABC
import mysql.connector


class BDIAbstract(ABC):
    def __init__(self, host, user, password, db):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__db = db


    @property
    def host(self):
        return self.__host

    @property
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.__password

    @property
    def db(self):
        return self.__db

    
    
    def connect(self):
        pass
    def execute(self, query, parameters) -> bool:
        pass
    def get_one(self, query, parameters) -> dict:
        pass
    def get_all(self, query, parameters) -> list:
        pass
    

class MySQLConnection(BDIAbstract):
    def _init_(self):
        super().__init__(self.host, self.user, self.password, self.db)
        self.cnx = None

    
    def connect(self):
        try:
            self.cnx = mysql.connector.connect(user='sgomes', 
                                                password='1147',
                                                host='127.0.0.1',
                                                database='mydb')
        except mysql.connector.Error as err:
            print(err)
            return False
        return True


    def execute(self, query, parameters):
        try:
            if not self.connect():
                return False
            cursor = self.cnx.cursor()
            cursor.execute(query, parameters)
            self.cnx.commit()
            cursor.close()
            self.cnx.close()
        except Exception as e:
            print(e)
            return False
        return True
        
        
    def get_one(self, query, parameters) -> dict:
        try:
            if not self.connect():
                return False
            cursor = self.cnx.cursor()
            cursor.execute(query, parameters)
            resultado = cursor.fetchone()
            cursor.close()
            self.cnx.close()
        except Exception as e:
            print(e)
            return None
        return resultado


    def get_all(self, query, parameters) -> list:
        try:
            if not self.connect():
                return False
            cursor = self.cnx.cursor()
            cursor.execute(query, parameters)
            result = cursor.fetchall()
            cursor.close()
            self.cnx.close()
        except Exception as e:
            print(e)
            return False
        return result
        