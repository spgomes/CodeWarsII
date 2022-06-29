from abc import abstractmethod, ABC

class Imposto(ABC):
    def __init__(self, salario_base: int) -> None:
        self.salario_base = salario_base
    
    @abstractmethod
    def calculo_contribuicao(self):
        pass

class INSS(Imposto):
    def __init__(self, salario_base) -> None:
        super().__init__(salario_base)

    def calculo_contribuicao(self, salario_base)-> int:
        salario_base = self.salario_base
        aliquotas = [{
        'inicio': 0,
        'fim': 121200,
        'aliquota': 7.5,
        'deducao': 0,
    },
    {
        'inicio': 121201,
        'fim': 242735,
        'aliquota': 9,
        'deducao': 1818,
    },
    {
        'inicio': 242736,
        'fim': 364103,
        'aliquota': 12,
        'deducao': 9100,
    },
    {
        'inicio': 364104,
        'fim': 708722,
        'aliquota': 14,
        'deducao': 16382,
    }
    ]
        if salario_base >= aliquotas[aliquotas.count(1) - 1]['fim']:
            salario_base = aliquotas[aliquotas.count(1) - 1]['fim']

        for faixa in aliquotas:
            if salario_base < faixa['inicio']:
                continue
            if faixa['fim'] is not None and salario_base > faixa['fim']:
                continue
            return int((salario_base) * (faixa['aliquota'] / 100) - faixa['deducao'])
        return 0


class IRRF(Imposto):
    def __init__(self, salario_base) -> None:
        super().__init__(salario_base)

    def calculo_contribuicao(self, salario_base):
            
        salario_deduzido_inss = salario_base - INSS.calculo_contribuicao(self, salario_base)
        
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
            if salario_deduzido_inss < faixa['inicio']:
                continue
            if faixa['fim'] is not None and salario_deduzido_inss > faixa['fim']:
                continue
            return int(salario_deduzido_inss * (faixa['aliquota'] / 100) - faixa['deducao'])
        return 0

