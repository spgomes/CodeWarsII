

from src.persistence.bdiServices import MySQLConnection


class FuncionarioPersistence():
    def _init_(self, conexao: MySQLConnection) -> None:
        self.db = conexao



    def save(self, dados_funcionario: dict) -> bool:
        try:
            self.db.execute(
                'INSERT INTO Funcionario (Matricula, Nome, CPF, DataAdmissao, Cargo, Comissao) Values (%(Matricula)s, %(Nome)s, %(CPF)s, %(DataAdmissao)s, %(Cargo)s, %(Comissao)s)',
                {
                'Matricula': dados_funcionario['Matricula'],
                'Nome': dados_funcionario['Nome'],
                'CPF': dados_funcionario['CPF'],
                'DataAdmissao': dados_funcionario['DataAdmissao'],
                'Cargo':dados_funcionario['Cargo'],
                'Comissao':dados_funcionario['Comissao']
                })
            return True
        except:
            return False
            


    def get_one(self, matricula: int) -> dict:
        return self.db.get_one('SELECT * FROM Funcionario WHERE Matricula = %(matricula)s', {'Matricula': matricula})


    def get_all(self) -> list:
        return self.db.get_all('SELECT * FROM Funcionario',{})


    def remove(self, matricula: int) -> None:
        return self.db.execute('DELETE FROM Funcionario WHERE Matricula = %(matricula)s', {'Matricula': matricula})


    def update(self, dados_funcionario: dict) -> bool:
        try:
            self.db.execute("""
                UPDATE Funcionario 
                SET Matricula =  %(Matricula)s, Nome =  %(Nome)s, CPF =  %(CPF)s, DataAdmissao =  %(DataAdmissao)s,
                Cargo =  %(Cargo)s, Comissao =  %(Comissao)s   
                WHERE Matricula = %(matricula)s""",
                {
                'Matricula': dados_funcionario['Matricula'],
                'Nome': dados_funcionario['Nome'],
                'CPF': dados_funcionario['CPF'],
                'DataAdmissao': dados_funcionario['DataAdmissao'],
                'Cargo':dados_funcionario['Cargo'],
                'Comissao':dados_funcionario['Comissao']
                })
            return True
        except:
            return False


    def get_last_matricula(self) -> int:
        atual = self.db.get_one('SELECT MAX(Matricula) as matricula FROM Funcionario', {})
        if atual is None:
            return 100000
        return atual['matricula']
