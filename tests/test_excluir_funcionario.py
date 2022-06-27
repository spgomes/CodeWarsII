from unittest import TestCase
from datetime import datetime

from src.funcionarioServices import AcoesFuncionario
from src.funcionario import Funcionario

class TestExcluirFuncionario(TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.funcionario = None
        self.acoesFuncionario = None

    def setUp(self):
        self.acoesFuncionario = AcoesFuncionario()
        self.funcionario = Funcionario("111111", "Ana Maria", "11111111100", datetime(2019,7,2), "32", True)
        self.acoesFuncionario.inserir(self.funcionario)

    def test_excluir_deve_retornar_vazio(self):
        self.acoesFuncionario.excluir_por_matricula("111111")
        resultado = self.acoesFuncionario.listar_todos()
        self.assertEqual(len(resultado), 0)

    def test_excluir_deve_retornar_none(self):
        retornarNone = self.acoesFuncionario.excluir_por_matricula(self.funcionario.matricula)
        self.assertTrue(retornarNone == None)
