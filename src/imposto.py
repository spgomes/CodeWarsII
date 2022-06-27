from abc import abstractmethod, ABC

class Imposto(ABC):
    def __init__(self, tipo) -> None:
        self.tipo = tipo
    
    @abstractmethod
    def calculo_contribuicao(self):
        pass

class INSS(Imposto):
    def __init__(self, tipo) -> None:
        super().__init__(tipo)

    def calculo_contribuicao(self, salario)-> int:
        salario_inteiro = salario * 100
        
        aliquotas = [{
        'inicio': 0,
        'fim': 190398,
        'aliquota': 0,
        'deducao': 0,
    },
    {
        'inicio': 190398,
        'fim': 282665,
        'aliquota': 7.5,
        'deducao': 14280,
    },
    {
        'inicio': 282666,
        'fim': 375105,
        'aliquota': 15,
        'deducao': 35480,
    },
    {
        'inicio': 375106,
        'fim': 466468,
        'aliquota': 22.5,
        'deducao': 63613,
    },
    {
        'inicio': 466469,
        'fim': None,
        'aliquota': 27.5,
        'deducao': 86936,
    }
    ]
        for faixa in aliquotas:
            if salario_inteiro < faixa['inicio']:
                continue
            if faixa['fim'] is not None and salario_inteiro > faixa['fim']:
                continue
            return int((salario_inteiro) * (faixa['aliquota'] / 100) - faixa['deducao'])
        return 0


class IRRF(Imposto):
    def __init__(self, tipo) -> None:
        super().__init__(tipo)

    def calculo_contribuicao(self):
        pass
