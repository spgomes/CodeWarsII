from src.entidades.funcionario import Funcionario
from src.persistence.bdiServices import BDIAbstract


class HoleritePersistence():
    def _init_(self, conexao: BDIAbstract, funcionario: Funcionario) -> None:
        self.db = conexao
        self.funcionario = funcionario
        self.matricula = funcionario.matricula
    

    def save_holerite():
        pass

    def get_one_holerite():
        pass

    def get_all_holerite():
        pass

