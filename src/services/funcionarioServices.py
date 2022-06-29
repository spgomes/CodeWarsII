from src.entidades.funcionario import Funcionario
from src.exceptions.funcionario_not_found_error import FuncionarioNotFoundError
from typing import List
from datetime import datetime
class FuncionarioServices():
    def __init__(self) -> None:
        self.lista_funcionario = []

    def inserir(self, funcionario: Funcionario) -> None:
        self.lista_funcionario.append(funcionario)

    def listar_todos(self) -> List[Funcionario]:
        return self.lista_funcionario

    def consulta(self, matricula: str) -> Funcionario:
        funcionarios = list(filter(lambda x: x.matricula == matricula, self.lista_funcionario))
        return funcionarios[0]

    def excluir_por_matricula(self, matricula: str) -> None:
        self.lista_funcionario.remove(self.consulta(matricula))

    def alterar_por_matricula(self, matricula: str, nome: str, cpf: str, dta_admissao: datetime, cod_cargo: str, comissao: bool) -> bool:
        try:
            funcionario = self.consulta(matricula)
            funcionario.comissaoSet(comissao)
        except FuncionarioNotFoundError as e:
            raise e

