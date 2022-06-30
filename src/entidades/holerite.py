
from src.services.ImpostoServices import ImpostoService
from src.services.funcionarioServices import FuncionarioServices
from src.services.holeriteServices import HoleriteServices



class Holerite():
    def __init__(self, faltas, matricula:int, funcionarioServices: FuncionarioServices, 
                impostoServices: ImpostoService, holeriteServices: HoleriteServices) -> None:
        
        query = Adapter().insert(matricula)
        dados_funcionario = funcionarioServices.get_one(matricula)

        self.__faltas = faltas
        self.__matricula = matricula
        self.__cargo = dados_funcionario['Descricao']
        self.__comissao = dados_funcionario['Comissao']
        self.__data_admissao = dados_funcionario['Nome']
        self.__salario_base = dados_funcionario['SalarioBase']
        self.__valor_comissao = holeriteServices.calculo_comissao()
        self.__desconto_faltas = holeriteServices.calculo_desconto_faltas()
        self.__inss = impostoServices.calculo_contribuicao_inss()
        self.__irrf = impostoServices.calculo_contribuicao_irrf()
        self.__salario_liquido = holeriteServices.calculo_salario_liquido
        self.__salario_base_de_calculo = holeriteServices.calculo_salario_base_de_calculo()
        self.__fgts = holeriteServices.calculo_fgts()

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
    
    



    
