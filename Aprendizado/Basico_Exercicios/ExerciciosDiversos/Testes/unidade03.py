import unittest

def verifica_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

class Testando(unittest.TestCase):
    def test_idade(self):
        self.assertEqual(verifica_idade(18) , 'Maior de idade')
    def test_idade(self):
        self.assertEqual(verifica_idade(62) , 'Maior de idade')
    def test_idade(self):
        self.assertEqual(verifica_idade(17) , 'Menor de idade')

if __name__ == "__main__":
    unittest.main()