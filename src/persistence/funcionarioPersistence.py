


import random
from src.entidades.funcionario import Funcionario
from src.persistence.bdiServices import BDIAbstract
from src.services.funcionarioServices import FuncionarioServices


class FuncionarioPersistence():
    def _init_(self, conexao: BDIAbstract, funcionario: Funcionario, funcionarioServices: FuncionarioServices) -> None:
        self.db = conexao
        self.funcionario = funcionario
        self.funcionarioServices = funcionarioServices
        self.matricula = funcionarioServices.matricula

        
    def gerador_matricula():
        return random.randint(100000,999999)

    def save(self, funcionario) -> None:
        pass
    
    def get_one(self, matricula: int, ) -> dict:
        return dados_funcionario

    def get_all(self) -> list:
        pass

    def remove(self, matricula: int) -> None:
        pass

    def update(self, matricula: str, nome: str, cpf: str, data_admissao, cod_cargo: str, comissao: bool) -> bool:
        pass
