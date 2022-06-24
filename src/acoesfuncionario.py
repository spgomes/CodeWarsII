from src.funcionario import Funcionario
from typing import List

class AcoesFuncionario():
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
