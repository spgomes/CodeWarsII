from src.entidades.imposto import INSS, IRRF, Imposto
from src.services.funcionarioServices import FuncionarioServices


class ImpostoService():
    def _init_(self, funcionarioServices: FuncionarioServices ):
        dados_funcionario = funcionarioServices.get_funcionario()
        self.salario_base = dados_funcionario['SalarioBase']


    def calculo_contribuicao_inss(self) -> int:
        impostoINSS = INSS.calculo_contribuicao_inss(self, self.salario_base)
        return impostoINSS

    def calculo_contribuicao_irrf(self, ) -> int:
        impostoIRRF = IRRF.calculo_contribuicao_irrf(self, self.salario_base)
        return impostoIRRF
