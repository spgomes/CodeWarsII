
from src.services.ImpostoServices import ImpostoService
from src.services.holeriteServices import HoleriteServices



class Holerite():
    def __init__(self, faltas, impostoServices: ImpostoService, holeriteServices: HoleriteServices) -> None:

        self.__faltas = faltas
        self.__valor_comissao = holeriteServices.calculo_comissao()
        self.__desconto_faltas = holeriteServices.calculo_desconto_faltas()
        self.__inss = impostoServices.calculo_contribuicao_inss()
        self.__irrf = impostoServices.calculo_contribuicao_irrf()
        self.__salario_liquido = holeriteServices.calculo_salario_liquido()
        self.__salario_base_de_calculo = holeriteServices.calculo_salario_base_de_calculo()
        self.__fgts = holeriteServices.calculo_fgts()

    
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
    
    @property
    def __valor_comissao(self) -> int:
        return self.__valor_comissao
    



    
