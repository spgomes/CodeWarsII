from src.entidades.funcionario import Funcionario
from src.exceptions.funcionario_not_found_error import FuncionarioNotFoundError

from src.persistence.funcionarioPersistence import FuncionarioPersistence


class FuncionarioServices():
    def __init__(self, persistencia: FuncionarioPersistence, funcionario: Funcionario) -> None:
        self.persistencia = persistencia
        self.funcionario = funcionario
        self.dados_funcionario = funcionario.__dados_funcionario

    
    def save(self, dados_funcionario) -> None:
        return self.persistencia.save(self, dados_funcionario)

    def get_all(self) -> list:
        return self.persistencia.get_all(self)
    
    def get_one(self, matricula: int) -> dict:
        return self.persistencia.get_one(self, matricula)
    
    def get_funcionario(self, matricula: str) -> Funcionario:
        funcionario: Funcionario = self.persistencia.get_one(self, matricula)
        return funcionario

    def excluir_por_matricula(self, matricula: str) -> None:
        return self.persistencia.remove()

    def alterar_por_matricula(self, matricula: str, nome: str, cpf: str, dta_admissao: datetime, cod_cargo: str, comissao: bool) -> bool:
        try:
            funcionario = self.consulta(matricula)
            funcionario.comissaoSet(comissao)
        except FuncionarioNotFoundError as e:
            raise e

