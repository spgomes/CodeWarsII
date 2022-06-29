
from src.entidades.funcionario import Funcionario



class Holerite():
    def __init__(self, faltas) -> None:
        self.__matricula = Funcionario.matricula
        self.__data_admissao = self.__data_admissao
        self.__cargo = self.__cargo
        self.__comissao = self.__comissao
        self.__valor_comissao = self.__valor_comissao
        self.__faltas = faltas
        self.__desconto_faltas = self.__desconto_faltas
        self.__inss = self.__inss
        self.__irrf = self.__irrf
        self.__salario_liquido = self.__salario_liquido
        self.__salario_base = self.__salario_base
        self.__salario_base_de_calculo = self.__salario_base_de_calculo
        self.__fgts = self.__fgts

    @property
    def __matricula(self) -> int:
        return self.__matricula
    
    @property
    def __data_admissao(self) -> str:
        return self.__data_admissao
    
    @property
    def __cargo(self) -> str:
        return self.__cargo
    
    @property
    def __comissao(self) -> int:
        return self.__comissao
    
    @property
    def __faltas(self) -> int:
        return self.__faltas
    
    @property
    def __fgts(self) -> int:
        return self.__fgts

    @property
    def __salario_base_de_calculo(self) -> int:
        return self.__salario_base_de_calculo

    @property
    def __desconto_faltas(self) -> int:
        return self.__desconto_faltas
    
    @property
    def __inss(self) -> int:
        return self.__inss
    
    @property
    def __irrf(self) -> int:
        return self.__irrf
    
    @property
    def __salario_liquido(self) -> int:
        return self.__salario_liquido
    
    @property
    def __salario_base(self) -> int:
        return self.__salario_base
    
    



    
