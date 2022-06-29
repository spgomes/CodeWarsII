from datetime import datetime
import random


class Funcionario():
    def __init__(self, nome: str, cpf: str, data_admissao: datetime, cod_cargo: str, comissao: bool) -> None:
        self.__matricula = self.gerador_matricula()
        self.__nome = nome
        self.__cpf = cpf
        self.__data_admissao = data_admissao
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
    def data_admissao(self):
        return self.__data_admissao

    @property
    def cod_cargo(self):
        return self.__cod_cargo

    @property
    def comissao(self):
        return self.__comissao
    
    def comissaoSet(self, valor):
        self.__comissao = valor
    
    def gerador_matricula():
        return random.randint(100000,999999)