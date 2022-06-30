from src.entidades.funcionario import Funcionario
from src.exceptions.funcionario_not_found_error import FuncionarioNotFoundError
from datetime import datetime

from src.persistence.funcionarioPersistence import FuncionarioPersistence


class FuncionarioServices():
    def __init__(self, persistencia: FuncionarioPersistence, funcionario: Funcionario) -> None:
        self.persistencia = persistencia
        self.funcionario = funcionario
        self.matricula = self.get_matricula()

    def get_matricula(self):
        matricula = Adapter().insert_matricula()
        return matricula
    
    def save(self) -> None:
        return self.persistencia.save()

    def get_all(self) -> list:
        return self.persistencia.get_all()

    def get_one(self, matricula: str) -> dict:
        return self.persistencia.get_one(self, matricula)

    def excluir_por_matricula(self, matricula: str) -> None:
        return self.persistencia.remove()

    def alterar_por_matricula(self, matricula: str, nome: str, cpf: str, dta_admissao: datetime, cod_cargo: str, comissao: bool) -> bool:
        try:
            funcionario = self.consulta(matricula)
            funcionario.comissaoSet(comissao)
        except FuncionarioNotFoundError as e:
            raise e

