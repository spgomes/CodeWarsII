


from datetime import datetime
from src.entidades.funcionario import Funcionario
from src.entidades.holerite import Holerite
from src.persistence.holeritePersistence import HoleritePersistence
from src.services.ImpostoServices import ImpostoService


class HoleriteServices():
    def __init__(self, persistencia: HoleritePersistence) -> None:
        self.persistencia = persistencia

    def save(self, holerite: Holerite) -> bool:
        try:
            if self.get_one(self, holerite.__dados_holerite['AnoMes'], holerite.__dados_holerite['Matricula']):
                raise HoleriteAlreadyExist("Existe um holerite gerado esse mes.")
            self.persistencia.save(holerite.to_bd())
            return True
        except:
            return False    

    def get_one(self, AnoMes: datetime, Matricula: int):
        return self.persistencia.get_one(AnoMes, Matricula)


    def get_all(self) -> list:
        return self.persistencia.get_all()


    def gera_holerite(self, holerite: Holerite, impostoService: ImpostoService, funcionario: Funcionario):
        holerite.salario_liquido = self.calculo_salario_liquido(funcionario, impostoService)
        holerite.fgts = self.calculo_fgts()
        holerite.faltas = self.calculo_desconto_faltas(funcionario)
        holerite.salario_bruto = self.calculo_salario_bruto(funcionario)
        holerite.inss = impostoService.calculo_contribuicao_inss(funcionario)
        holerite.irrf = impostoService.calculo_contribuicao_irrf(funcionario)
        return holerite.to_bd 
    
    
    def calculo_salario_liquido(self, funcionario: Funcionario, impostoService: ImpostoService):
        return funcionario.to_bd['SalarioBase'] -   (
                                                    self.calculo_fgts() + 
                                                    self.calculo_desconto_faltas() + 
                                                    impostoService.calculo_contribuicao_inss() + 
                                                    impostoService.calculo_contribuicao_irrf()
                                                    )
        

    def calculo_fgts(self):
        return self.calculo_salario_bruto() * 0.08
        

    def calculo_salario_bruto(self, funcionario: Funcionario):
        return funcionario.to_bd['SalarioBase'] + self.calculo_comissao()
        

    def calculo_comissao(funcionario: Funcionario):
        if funcionario.to_bd['Comissao'] == 1:
            return funcionario.to_bd['SalarioBase'] * ((funcionario.to_bd['ValorComissao'])/100)
        return 0
    

    def calculo_desconto_faltas(Faltas):
        return Faltas * 100
        
