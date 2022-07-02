from src.entidades.funcionario import Funcionario
from src.entidades.imposto import INSS, IRRF, Imposto
from src.services.funcionarioServices import FuncionarioServices


class ImpostoService():
    def _init_(self, imposto: Imposto):
        self.imposto = imposto


    def calculo_contribuicao_inss(self, funcionario: Funcionario) -> int:
        return INSS.calculo_contribuicao(self, funcionario.to_bd()['SalarioBase'])
        

    def calculo_contribuicao_irrf(self, funcionario: Funcionario) -> int:
        return IRRF.calculo_contribuicao(self, funcionario.to_bd()['SalarioBase'])
        
