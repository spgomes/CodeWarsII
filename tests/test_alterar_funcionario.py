from unittest import TestCase
from datetime import datetime

from src.acoesfuncionario import AcoesFuncionario
from src.funcionario import Funcionario

class TestAlterarFuncionario(TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.funcionario = None
        self.acoesFuncionario = None
    
    def setUp(self):
        self.acoesFuncionario = AcoesFuncionario()
        self.funcionario = Funcionario("111111", "Ana Maria", "11111111100", datetime(2019,7,2), "32", True)
        self.acoesFuncionario.inserir(self.funcionario)
    
    def test_deve_alterar_nome_funcionario(self):
        self.acoesFuncionario.alterar_por_matricula("111111", "Ana Maria", "11111111100", datetime(2019,7,2), "32", False)
        funcionario = self.acoesFuncionario.consulta("111111")
        self.assertEqual(funcionario.comissao, False)