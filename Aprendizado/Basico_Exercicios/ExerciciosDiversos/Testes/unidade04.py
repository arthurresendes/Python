import unittest

def eh_palindromo(palavra):
    return palavra == palavra[::-1]

class Testando(unittest.TestCase):
    def test_palindromo(self):
        self.assertTrue(eh_palindromo('arara'))
    def test_palindromo(self):
        self.assertFalse(eh_palindromo('bola'))

if __name__ == "__main__":
    unittest.main()
