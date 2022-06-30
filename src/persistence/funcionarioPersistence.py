


from src.entidades.funcionario import Funcionario
from src.persistence.bdiServices import BDIAbstract


class FuncionarioPersistence():
    def _init_(self, conexao: BDIAbstract, funcionario: Funcionario) -> None:
        self.db = conexao
        self.funcionario = funcionario
        self.matricula = funcionario.matricula

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
