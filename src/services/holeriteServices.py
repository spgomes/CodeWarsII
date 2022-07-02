


from datetime import datetime
from src.entidades.holerite import Holerite
from src.persistence.holeritePersistence import HoleritePersistence


class HoleriteServices():
    def __init__(self, faltas: int, persistencia: HoleritePersistence) -> None:
        super().__init__(faltas)
        self.persistencia = persistencia

    def save(self, holerite: Holerite) -> bool:
        try:
            if self.get_one(self, holerite.__dados_holerite['AnoMes']):
                raise HoleriteAlreadyExist("Existe um holerite gerado esse mes.")
            self.persistencia.save(holerite.to_bd())
            return True
        except:
            return False    

    def get_one(self, AnoMes: datetime, Matricula: int):
        return self.persistencia.get_one(AnoMes, Matricula)

    def get_all(self) -> list:
        return self.persistencia.get_all()

    def calculo_salario_liquido(self, holerite: Holerite):
        SalarioLiquido = SalarioBaseCalculo - Descontos
        return SalarioLiquido

    def calculo_fgts():
        FGTS = SalarioBaseCalculo * 0.08
        return FGTS

    def calculo_salario_base_de_calculo():
        SalarioBaseCalculo = SalarioBase + Comissao
        return SalarioBaseCalculo

    def calculo_comissao():
        ValorComissao = Comissao * SalarioBase
        return ValorComissao

    def calculo_desconto_faltas():
        DescontoFaltas = Faltas * 100
        return DescontoFaltas
