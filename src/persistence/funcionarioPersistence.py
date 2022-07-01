


import random
from src.exceptions.funcionario_already_exist import FuncionarioAlreadyExist
from src.exceptions.not_found_error import NotFoundError
from src.persistence.bdiServices import MySQLConnection
from src.services.funcionarioServices import FuncionarioServices


class FuncionarioPersistence():
    def _init_(self, conexao: MySQLConnection, funcionarioServices: FuncionarioServices) -> None:
        self.db = conexao
        self.funcionarioServices = funcionarioServices
        self.dados_funcionario = funcionarioServices.dados_funcionario
        

        
    def gerador_matricula(self):
        return random.randint(100000,999999)

    def save(self, dados_funcionario: dict, matricula: int) -> bool:
        try:
            self.get_one(self, matricula)
            raise FuncionarioAlreadyExist("Esse Funcionario já está cadastrado!")
        except NotFoundError:
            matricula = self.gerador_matricula(self)
            self.db.execute(
                'INSERT INTO Funcionario (Nome, CPF, DataAdmissao, Cargo, Comissao = %(Nome)s, %(CPF)s, %(DataAdmissao)s, %(Cargo)s, %(Comissao)s)',
                {'Matricula': matricula,
                 'CPF': dados_funcionario['CPF'],
                 'DataAdmissao': dados_funcionario['DataAdmissao'],
                 'Cargo':dados_funcionario['Cargo'],
                 'Comissao':dados_funcionario['Comissao']
                 })
            return True
            

    
    def get_one(self, matricula: int) -> dict:
        return self.db.get_one('SELECT * FROM Funcionario WHERE Matricula = %(matricula)s', {'Matricula': matricula})


    def get_all(self) -> list:
        return self.db.get_all('SELECT * FROM Funcionario',{})

    def remove(self, matricula: int) -> None:
        try:
            self.get_one(self, matricula)
            raise NotFoundError("Esse Funcionario não foi encontrado!")
        except:
            self.db.execute('DELETE FROM Funcionario WHERE Matricula = %(matricula)s', {'Matricula': matricula})
            return True

    def update(self, matricula: int, dados_funcionario: dict) -> bool:
        try:
            self.get_one(self, matricula)
            raise NotFoundError("Esse Funcionario não foi encontrado!")
        except:
            for campos in self.dados_funcionario:
                nome_campo = campos
                novo_dado = input(f'Digite o novo dado do campo:', nome_campo)
                self.db.execute('UPDATE Funcionario SET %s WHERE Matricula = %(matricula)s', {'Campo': novo_dado})
            return True
