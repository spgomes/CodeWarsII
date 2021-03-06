

class Funcionario():
    def __init__(self, dados_funcionario: dict) -> None:
        self.__dados_funcionario = dados_funcionario

    
    @property
    def matricula(self):
        return self.__dados_funcionario['Matricula']

    @property
    def nome(self):
        return self.__dados_funcionario['Nome']

    @property
    def cpf(self):
        return self.__dados_funcionario['CPF']

    @property
    def data_admissao(self):
        return self.__dados_funcionario['DataAdmissao']

    @property
    def cod_cargo(self):
        return self.__dados_funcionario['Cargo']

    @property
    def comissao(self):
        return self.__dados_funcionario['Comissao']
    
    
    def to_bd(self):
        return self.__dados_funcionario
    