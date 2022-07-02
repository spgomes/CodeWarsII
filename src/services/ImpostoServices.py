from src.entidades.imposto import INSS, IRRF
from src.services.funcionarioServices import FuncionarioServices


class ImpostoService():
    def _init_(self, funcionarioServices: FuncionarioServices ):
        dados_funcionario = funcionarioServices.get_funcionario()
        self.salario_base = dados_funcionario['SalarioBase']


    def calculo_contribuicao_inss(self) -> int:
        return INSS.calculo_contribuicao(self, self.salario_base)
        

    def calculo_contribuicao_irrf(self, ) -> int:
        return IRRF.calculo_contribuicao(self, self.salario_base)
        
