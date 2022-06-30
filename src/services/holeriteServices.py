


from src.entidades.funcionario import Funcionario


class HoleriteServices():
    def __init__(self, faltas: int, funcionario: Funcionario) -> None:
        super().__init__(faltas)
        self.matricula = funcionario.matricula

    
    def save_holerite():
        pass

    def get_one_holerite():
        pass

    def get_all_holerite():
        pass

    def calculo_salario_liquido():
        pass

    def calculo_fgts():
        pass

    def calculo_salario_base_de_calculo():
        pass

    def calculo_comissao():
        pass

    def calculo_desconto_faltas():
        pass
