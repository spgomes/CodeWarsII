


import random
from src.entidades.funcionario import Funcionario
from src.persistence.bdiServices import BDIAbstract
from src.services.funcionarioServices import FuncionarioServices


class FuncionarioPersistence():
    def _init_(self, conexao: BDIAbstract, funcionarioServices: FuncionarioServices) -> None:
        self.db = conexao
        self.funcionarioServices = funcionarioServices
        
        

        
    def gerador_matricula():
        return random.randint(100000,999999)

    def save(self) -> None:
        pass
    
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

    def remove(self, matricula: int) -> None:
        pass

    def update(self, dados_funcionario: dict) -> bool:
        pass
