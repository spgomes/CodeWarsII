
from src.persistence.bdiServices import MySQLConnection


class HoleritePersistence():
    def _init_(self, conexao: MySQLConnection) -> None:
        self.db = conexao


    def save(self, dados_holerite: dict) -> bool:
        try:
            self.db.execute(
                """INSERT INTO Funcionario (Faltas, FGTS, SalarioBaseCalculo, DescontoFaltas, INSS, IRRF, SalarioLiquido, SalarioBase, ValorComissao) 
                Values (%(Faltas)s, %(FGTS)s, %(SalarioBaseCalculo)s, %(DescontoFaltas)s, %(INSS)s, %(IRRF)s, %(SalarioLiquido)s, %(SalarioBase)s, %(ValorComissao)s)""",
                {
                'Matricula': dados_holerite['Matricula'],
                'Faltas': dados_holerite['Faltas'],
                'FGTS': dados_holerite['FGTS'],
                'SalarioBaseCalculo': dados_holerite['SalarioBaseCalculo'],
                'DescontoFaltas': dados_holerite['DescontoFaltas'],
                'INSS':dados_holerite['INSS'],
                'IRRF':dados_holerite['IRRF'],
                'SalarioLiquido':dados_holerite['SalarioLiquido'],
                'SalarioBase':dados_holerite['SalarioBase'],
                'ValorComissao':dados_holerite['ValorComissao'],
                })
            return True
        except:
            return False


    def get_one(self, matricula: int) -> dict:
        return self.db.get_one('SELECT * FROM Holerite WHERE Matricula = %(matricula)s', {'Matricula': matricula})


    def get_all(self) -> list:
        return self.db.get_all('SELECT * FROM Holerite',{})


    def remove(self, matricula: int) -> None:
        return self.db.execute('DELETE FROM Holerite WHERE Matricula = %(matricula)s', {'Matricula': matricula})


    def update(self, dados_holerite: dict) -> bool:
        try:
            self.db.execute("""
                UPDATE Holerite 
                SET Matricula =  %(Matricula)s, Faltas =  %(Faltas)s, FGTS =  %(FGTS)s, SalarioBaseCalculo =  %(SalarioBaseCalculo)s,
                DescontoFaltas =  %(DescontoFaltas)s, INSS =  %(INSS)s, IRRF = %(IRRF)s, SalarioLiquido = %(SalarioLiquido)s,
                SalarioBase = %(SalarioBase)s, ValorComissao = %(ValorComissao)s    
                WHERE Matricula = %(matricula)s""",
                {
                'Matricula': dados_holerite['Matricula'],
                'Faltas': dados_holerite['Faltas'],
                'FGTS': dados_holerite['FGTS'],
                'SalarioBaseCalculo': dados_holerite['SalarioBaseCalculo'],
                'DescontoFaltas': dados_holerite['DescontoFaltas'],
                'INSS':dados_holerite['INSS'],
                'IRRF':dados_holerite['IRRF'],
                'SalarioLiquido':dados_holerite['SalarioLiquido'],
                'SalarioBase':dados_holerite['SalarioBase'],
                'ValorComissao':dados_holerite['ValorComissao'],
                })
            return True
        except:
            return False
