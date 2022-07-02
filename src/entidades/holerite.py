


class Holerite():
    def __init__(self, dados_holerite: dict) -> None:
        self.__dados_holerite = dados_holerite

    
    @property
    def faltas(self) -> int:
        return self.__dados_holerite['Faltas']
    
    @property
    def fgts(self) -> int:
        return self.__dados_holerite['FGTS']

    @fgts.setter
    def fgts(self, value) -> int:
        self.__dados_holerite['FGTS'] = value

    @property
    def salario_bruto(self) -> int:
        return self.__dados_holerite['SalarioBruto']
    
    @salario_bruto.setter
    def salario_bruto(self, value) -> int:
        self.__dados_holerite['SalarioBruto'] = value

    @property
    def desconto_faltas(self) -> int:
        return self.__dados_holerite['DescontoFaltas']
    
    @desconto_faltas.setter
    def desconto_faltas(self, value) -> int:
        self.__dados_holerite['DescontoFaltas'] = value
    
    @property
    def inss(self) -> int:
        return self.__dados_holerite['INSS']
    
    @inss.setter
    def inss(self, value) -> int:
        self.__dados_holerite['INSS'] = value
    
    @property
    def irrf(self) -> int:
        return self.__dados_holerite['IRRF']
    
    @irrf.setter
    def irrf(self, value) -> int:
        self.__dados_holerite['IRRF'] = value
    
    @property
    def salario_liquido(self) -> int:
        return self.__dados_holerite['SalarioLiquido']
    
    @salario_liquido.setter
    def salario_liquido(self, value) -> int:
        self.__dados_holerite['SalarioLiquido'] = value
    
    @property
    def salario_base(self) -> int:
        return self.__dados_holerite['SalarioBase']
    
    @salario_base.setter
    def salario_base(self, value) -> int:
        self.__dados_holerite['SalarioBase'] = value
    
    @property
    def valor_comissao(self) -> int:
        return self.__dados_holerite['ValorComissao']
    
    @valor_comissao.setter
    def valor_comissao(self, value) -> int:
        self.__dados_holerite['ValorComissao'] = value
    

    def to_bd(self):
        return self.__dados_holerite

    
