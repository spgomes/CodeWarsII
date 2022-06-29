


from src.entidades.funcionario import Funcionario


class HoleriteServices():
    def __init__(self, faltas: int) -> None:
        super().__init__(faltas)
        self.matricula = Funcionario.matricula

    
    def consultar_cargo(self):
        pass

    def consultar_data_admissao(self):
        pass

    def consultar_comissao(self):
        pass

    def consultar_salario_base(self):
        pass
