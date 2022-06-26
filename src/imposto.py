from abc import abstractmethod, ABC

class Imposto(ABC):
    def __init__(self, tipo) -> None:
        self.tipo = tipo
        self.tirando_float = 1000
    
    @abstractmethod
    def calculo(self):
        pass

class INSS(Imposto):
    def __init__(self, tipo) -> None:
        super().__init__(tipo)

    def calculo(self, salario, valores_faixa, aliquotas, faixa):
        salario *= self.tirando_float 
        valores_faixa = [x*self.tirando_float for x in valores_faixa]
        aliquotas = [x*self.tirando_float for x in aliquotas]
        recolher = 0
        if faixa != 1:
            for f in range(faixa):
                if f == faixa:
                    recolher += (salario - valores_faixa[f][0])*aliquotas[f]
                elif f != 0:
                    recolher += (valores_faixa[f][1] - valores_faixa[f][0])*aliquotas[f]
                elif f == 0:
                    recolher += valores_faixa[f][1]*aliquotas[f]
            return recolher
        else:
            recolher += (valores_faixa[0][1] - salario)*aliquotas[0]
        return recolher

class IRRF(Imposto):
    def __init__(self, tipo) -> None:
        super().__init__(tipo)

    def calculo(self):
        pass
