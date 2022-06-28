from unittest import TestCase
from datetime import datetime

from src.services.funcionarioServices import AcoesFuncionario
from src.entidades.funcionario import Funcionario

class TestConsultarFuncionario(TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.funcionario = None
        self.acoesFuncionario = None
    
    def setUp(self):
        self.acoesFuncionario = AcoesFuncionario()
        self.funcionario = Funcionario("111111", "Ana Maria", "11111111100", datetime(2019,7,2), "32", True)
        self.acoesFuncionario.inserir(self.funcionario)
    
    def test_consulta_deve_retornar_111111(self):
        resultado = self.acoesFuncionario.consulta("111111")
        self.assertEqual(resultado.nome, "Ana Maria")

    def test_consulta_deve_retornar_tipo_funcionario(self):
        resultado = self.acoesFuncionario.consulta("111111")
        self.assertEqual(type(resultado), Funcionario)

    def test_listar_todos_deve_retornar_todos_cadastrados(self):
        resultado = []
        resultado.append(len(self.acoesFuncionario.listar_todos()))
        self.funcionario1 = Funcionario("111112", "Paulo Maria", "11111111199", datetime(2020,7,2), "32", True)
        self.acoesFuncionario.inserir(self.funcionario1)
        resultado.append(len(self.acoesFuncionario.listar_todos()))
        self.assertEqual(resultado, [1,2])
