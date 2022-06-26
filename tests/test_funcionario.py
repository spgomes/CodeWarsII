from unittest import TestCase
from datetime import datetime

from src.funcionario import Funcionario

class TestFuncionario(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.funcionario = None
    
    def setUp(self):
        self.funcionario = Funcionario("111111", "Ana Maria", "11111111100", datetime(2019,7,2), "32", True)
        
    def test_deve_retornar_matricula(self):
        resultado = self.funcionario.matricula
        self.assertEqual(resultado, "111111")

    def test_deve_retornar_nome(self):
        resultado = self.funcionario.nome
        self.assertEqual(resultado, "Ana Maria")

    def test_deve_retornar_cpf(self):
        resultado = self.funcionario.cpf
        self.assertEqual(resultado, "11111111100")

    def test_deve_retornar_data_admissao(self):
        resultado = self.funcionario.dta_admissao
        self.assertEqual(resultado, datetime(2019,7,2))

    def test_deve_retornar_cod_cargo(self):
        resultado = self.funcionario.cod_cargo
        self.assertEqual(resultado, "32")

    def test_deve_retornar_comissao(self):
        resultado = self.funcionario.comissao
        self.assertEqual(resultado, True)

    def test_nao_deve_alterar_nome(self):
        with self.assertRaises(AttributeError):
            self.funcionario.nome = "Pedro"