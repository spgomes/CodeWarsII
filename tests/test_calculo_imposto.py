from unittest import TestCase
from src.entidades.imposto import INSS, IRRF


class TestImposto(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.inss = None
        self.irrf = None

    def setUp(self):
        self.inss = INSS('INSS')
        self.irrf = IRRF('IRRF')

    def test_contribuicao_inss_primeira_faixa(self):
        self.assertEqual(self.inss.calculo_contribuicao(100000),7500)

    def test_contribuicao_inss_segunda_faixa(self):
        self.assertEqual(self.inss.calculo_contribuicao(200000),16182)

    def test_contribuicao_inss_terceira_faixa(self):
        self.assertEqual(self.inss.calculo_contribuicao(300000),26900)
    
    def test_contribuicao_inss_quarta_faixa(self):
        self.assertEqual(self.inss.calculo_contribuicao(400000),39618)
    
    def test_contribuicao_inss_acima_quarta_faixa(self):
        self.assertEqual(self.inss.calculo_contribuicao(1000000),82839)

    def test_contribuicao_irrf_primeira_faixa(self):
        self.assertEqual(self.irrf.calculo_contribuicao(100000),0)

    def test_contribuicao_irrf_segunda_faixa(self):
        self.assertEqual(self.irrf.calculo_contribuicao(309000),6796)
    
    def test_contribuicao_irrf_terceira_faixa(self):
        self.assertEqual(self.irrf.calculo_contribuicao(400000),18577)
    
    def test_contribuicao_irrf_quarta_faixa(self):
        self.assertEqual(self.irrf.calculo_contribuicao(500000),36822)

    def test_contribuicao_irrf_quinta_faixa(self):
        self.assertEqual(self.irrf.calculo_contribuicao(1000000),165283)
    
    