


class Holerite():
    def __init__(self, dados_holerite: dict) -> None:
        self.__dados_holerite = dados_holerite

    
    @property
    def faltas(self) -> int:
        return self.__dados_holerite['Faltas']
    
    @property
    def fgts(self) -> int:
        return self.__dados_holerite['FGTS']

    @property
    def salario_base_de_calculo(self) -> int:
        return self.__dados_holerite['SalarioBaseCalculo']

    @property
    def desconto_faltas(self) -> int:
        return self.__dados_holerite['DescontoFaltas']
    
    @property
    def inss(self) -> int:
        return self.__dados_holerite['INSS']
    
    @property
    def irrf(self) -> int:
        return self.__dados_holerite['IRRF']
    
    @property
    def salario_liquido(self) -> int:
        return self.__dados_holerite['SalarioLiquido']
    
    @property
    def salario_base(self) -> int:
        return self.__dados_holerite['SalarioBase']
    
    @property
    def valor_comissao(self) -> int:
        return self.__dados_holerite['ValorComissao']
    

    def to_bd(self, dados_holerite):
        return dados_holerite

    
