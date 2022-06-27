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

    def test_contribuicao_inss_minimo(self):
        self.assertEqual(self.inss.calculo_contribuicao(1900),0)

    def test_contribuicao_inss_maximo(self):
        self.assertEqual(self.inss.calculo_contribuicao(5000),50564)
    
