from src.entidades.imposto import INSS, IRRF, Imposto
from src.services.funcionarioServices import FuncionarioServices


class ImpostoService():
    def _init_(self, funcionarioServices: FuncionarioServices ):
        dados_funcionario = funcionarioServices.get_one(matricula)
        
        self.salario_base = dados_funcionario['SalarioBase']


    def calculo_contribuicao_inss(self) -> int:
        impostoINSS = INSS(self.salario_base)
        return impostoINSS.calculo_contribuicao()

    def calculo_contribuicao_irrf(self, ) -> int:
        impostoIRRF = IRRF(self.salario_base)
        return impostoIRRF.calculo_contribuicao()
