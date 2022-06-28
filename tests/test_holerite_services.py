from unittest import TestCase
from datetime import datetime

from src.services.holeriteServices import consultar_cargo, consultar_comissao, consultar_data_admissao, consultar_salario_base


class TestHoleriteServices(TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)


    def test_consultar_salario_base_funcionario(self):
        consulta_salario_base_deve_ser_3000 = consultar_salario_base('111111')
        self.assertTrue(consulta_salario_base_deve_ser_3000 == 3000)
    
    def test_consultar_comissao_funcionario_True_or_False(self):
        consulta_comissao_deve_ser_true = consultar_comissao('111111')
        self.assertTrue(consulta_comissao_deve_ser_true == True)

    def test_consultar_valor_comissao(self):
        consultar_valor_comissao_deve_ser_3 = consultar_comissao('111111')
        self.assertTrue(consultar_valor_comissao_deve_ser_3 == 3)

    def test_consultar_data_admissao_funcionario(self):
        consulta_data_admissao_deve_ser_2019_7_2 = consultar_data_admissao('111111')
        self.assertTrue(consulta_data_admissao_deve_ser_2019_7_2 == datetime(2019,7,2))

    def test_consultar_funcao_funcionario(self):
        consulta_funcao_deve_ser_Desenvolverdo_Junior = consultar_cargo('111111')
        self.assertTrue(consulta_funcao_deve_ser_Desenvolverdo_Junior == 'Desenvolvedor Junior')
    
