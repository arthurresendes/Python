'''
Unittest -> Teste unitarios

para rodar os testes utilizamos unittest.main()


assertEqual(a,b) -> a==b
assertNotEqual(a,b) -> a!=b
assertTrue(x) -> bool x is true
assertFalse(x) -> bool x is false
assertIs(a,b) -> a is b
assertIsNot(a,b) -> a is not b
assertIsNotNone(x) -> x is not none
assertIn(a,b) -> a in b
assertNotIn(a,b) -> a not in b
assertIsInstance(a,b) -> isinstance(1,b)
assertNotIsInstance(a,b) -> not isinstance(1,b)



'''

import unittest

from atividade import comer , dormir

class AtividadesTeste(unittest.TestCase):
    def test_comer_saudavel(self):
        self.assertEqual(comer('quiabo', True), 'Estou comendo quiabo porque é saudavel')  
    def test_comer_saturada(self):
        self.assertEqual(comer('pizza', False), 'Estou comendo pizza porque quero viver')  

    def dormir_pouco(self):
        self.assertEqual(dormir(4)),'Continuo dormindo pouco'
    def dormir_muito(self):
        self.assertEqual(dormir(12)),'Continuo dormindo muito'

if __name__ == "__main__":
    unittest.main()
