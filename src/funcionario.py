from datetime import datetime

class Funcionario():
    def __init__(self, matricula: str, nome: str, cpf: str, dta_admissao: datetime, cod_cargo: str, comissao: bool) -> None:
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.dta_admissao = dta_admissao
        self.cod_cargo = cod_cargo
        self.comissao = comissao