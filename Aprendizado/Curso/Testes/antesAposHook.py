'''
Uniteste - Antes e apos hooks


hook - são testes em si, a execução dos teste


setup() -> é executado antes de cada metodo de teste , é util para criarmos instancias de objetos e outros dados

tearDown() -> é executado ao final de cada metod de teste 


'''
import unittest

class ModuloTest(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_primeiro(self):
        pass

    def test_segundo(self):
        pass
    
    def tearDown(self):
        pass