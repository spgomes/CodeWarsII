from src.entidades.funcionario import Funcionario
from src.exceptions.funcionario_not_found_error import FuncionarioNotFoundError
from datetime import datetime

from src.percistence.funcionarioPercistence import FuncionarioPersistence


class FuncionarioServices():
    def __init__(self, persistencia: FuncionarioPersistence) -> None:
        self.lista_funcionario = []
        self.persistencia = persistencia

    def save(self) -> None:
        return self.persistencia.save()

    def get_all(self) -> list:
        return self.persistencia.get_all()

    def get_one(self, matricula: str) -> dict:
        return self.persistencia.get_one()

    def excluir_por_matricula(self, matricula: str) -> None:
        self.lista_funcionario.remove(self.consulta(matricula))

    def alterar_por_matricula(self, matricula: str, nome: str, cpf: str, dta_admissao: datetime, cod_cargo: str, comissao: bool) -> bool:
        try:
            funcionario = self.consulta(matricula)
            funcionario.comissaoSet(comissao)
        except FuncionarioNotFoundError as e:
            raise e

