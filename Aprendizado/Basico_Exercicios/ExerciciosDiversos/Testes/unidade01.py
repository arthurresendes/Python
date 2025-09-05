import unittest

def somar(a,b):
    return a + b

class SomaTeste(unittest.TestCase):
    
    def test_soma_positivos(self):
        self.assertEqual(somar(2, 3), 5)

    def test_soma_negativo_com_positivo(self):
        self.assertEqual(somar(-1, 1), 0)
        
    def testando_soma(self):
        self.assertIsInstance(somar(10, 5), int)


if __name__ == "__main__":
    unittest.main()
