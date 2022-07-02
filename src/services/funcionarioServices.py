from src.entidades.funcionario import Funcionario
from src.exceptions.funcionario_already_exist import FuncionarioAlreadyExist
from src.exceptions.funcionario_not_found_error import FuncionarioNotFoundError

from src.persistence.funcionarioPersistence import FuncionarioPersistence


class FuncionarioServices():
    def __init__(self, persistencia: FuncionarioPersistence, funcionario: Funcionario) -> None:
        self.persistencia = persistencia
        self.funcionario = funcionario
        self.dados_funcionario = funcionario.__dados_funcionario

    
    def save(self, dados_funcionario) -> None:
        try:
            if self.get_one(self, dados_funcionario['Matricula']) is not None:
                raise FuncionarioAlreadyExist("Esse Funcionario já está cadastrado!")
            self.persistencia.save(dados_funcionario)
            return True
        except:
            return False

    def get_all(self) -> list:
        return self.persistencia.get_all()
    
    def get_one(self, matricula: int) -> dict:
        return self.persistencia.get_one(matricula)
    
    def get_funcionario(self, matricula: int) -> Funcionario:
        dados_funcionario = self.persistencia.get_one(matricula)
        funcionario = Funcionario(dados_funcionario)
        return funcionario

    def excluir_por_matricula(self, matricula) -> bool:
        return self.persistencia.remove(matricula)

    def updade(self, dados_funcionario: dict) -> bool:
        try:
            if self.get_one(self, dados_funcionario['Matricula']) is None:
                raise FuncionarioNotFoundError("Esse Funcionario não foi encontrado!")
            self.persistencia.update(dados_funcionario['Matricula'])
            return True
        except:
            return False




