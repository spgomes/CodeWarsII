from src.entidades.imposto import INSS, IRRF, Imposto


class ImpostoService:
    def _init_(self, salario_base: int) -> None:
        self.salario_base = salario_base


    def calculo_contribuicao(self) -> int:
        impostoINSS = INSS(self.salario_base)
        return impostoINSS.calculo_contribuicao()

    def calculo_contribuicao_irrf(self, salario_base: int) -> int:
        impostoIRRF = IRRF(salario_base)
        return impostoIRRF.calculo_contribuicao()

    def save(self, imposto: Imposto) -> None:
        self.persistencia.save(self, imposto)