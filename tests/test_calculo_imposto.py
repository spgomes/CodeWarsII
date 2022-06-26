from unittest import TestCase

from src.imposto import INSS, IRRF

class TestImposto(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.inss = None
        self.irrf = None

    def setUp(self):
        self.inss = INSS('INSS')
        self.irrf = IRRF('IRRF')

    def test_inss_faixa1(self):
        salario = 1100
        valores_da_faixa = [[0, 1212], [1212.01, 2427.35], [2427.36, 3641.03], [3641.04, 7087.22]] 
        aliquotas = [0.075, 0.09, 0.12, 0.14]
        faixa = 1
        resultado = self.inss.calculo(salario, valores_da_faixa, aliquotas, faixa)
        self.assertEqual((resultado/1_000_000), 8.40)
        
    def test_inss_faixa2(self):
        salario = 1500
        valores_da_faixa = [[0, 1212], [1212.01, 2427.35], [2427.36, 3641.03], [3641.04, 7087.22]] 
        aliquotas = [0.075, 0.09, 0.12, 0.14]
        faixa = 2
        resultado = self.inss.calculo(salario, valores_da_faixa, aliquotas, faixa)
        self.assertEqual(resultado, 116.82*1_000_000)
        
    def test_inss_faixa3(self):
        salario = 5000
        valores_da_faixa = [[0, 1212], [1212.01, 2427.35], [2427.36, 3641.03], [3641.04, 7087.22]] 
        aliquotas = [0.075, 0.09, 0.12, 0.14]
        faixa = 4
        resultado = self.inss.calculo(salario, valores_da_faixa, aliquotas, faixa)
        self.assertEqual(resultado, 536.18*1_000_000)

    def test_inss_faixa4(self):
        salario = 8000
        valores_da_faixa = [[0, 1212], [1212.01, 2427.35], [2427.36, 3641.03], [3641.04, 7087.22]] 
        aliquotas = [0.075, 0.09, 0.12, 0.14]
        faixa = 4
        resultado = self.inss.calculo(salario, valores_da_faixa, aliquotas, faixa)
        self.assertEqual(resultado, 828.3897*1_000_000)
