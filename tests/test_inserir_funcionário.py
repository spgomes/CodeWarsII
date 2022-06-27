from unittest import TestCase
from datetime import datetime

from src.funcionarioServices import AcoesFuncionario
from src.funcionario import Funcionario

class TestInserirFuncionario(TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.funcionario = None
        self.acoesFuncionario = None

    def setUp(self):
        self.acoesFuncionario = AcoesFuncionario()
        self.funcionario = Funcionario("111111", "Ana Maria", "11111111100", datetime(2019,7,2), "32", True)
        self.acoesFuncionario.inserir(self.funcionario)

    def test_inserir_deve_inserir_funcionario_quantidade(self):
        lista_funcionarios = self.acoesFuncionario.listar_todos()
        self.assertEqual(len(lista_funcionarios), 1)
            
    def test_inserir_deve_retornar_none(self):
        retornarNone = self.acoesFuncionario.inserir(self.funcionario)
        self.assertTrue(retornarNone == None)

    def test_inserir_deve_inserir_funcionario(self):
        retornarCPF = self.acoesFuncionario.listar_todos()
        self.assertTrue(retornarCPF[0].cpf == "11111111100")
    