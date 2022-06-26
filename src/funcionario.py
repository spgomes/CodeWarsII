from datetime import datetime

class Funcionario():
    def __init__(self, matricula: str, nome: str, cpf: str, dta_admissao: datetime, cod_cargo: str, comissao: bool) -> None:
        self.__matricula = matricula
        self.__nome = nome
        self.__cpf = cpf
        self.__dta_admissao = dta_admissao
        self.__cod_cargo = cod_cargo
        self.__comissao = comissao


    @property
    def matricula(self):
        return self.__matricula

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def dta_admissao(self):
        return self.__dta_admissao

    @property
    def cod_cargo(self):
        return self.__cod_cargo

    @property
    def comissao(self):
        return self.__comissao
    
    def comissaoSet(self, valor):
        self.__comissao = valor