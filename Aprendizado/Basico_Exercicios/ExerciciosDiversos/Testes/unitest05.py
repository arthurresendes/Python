import unittest

def somar(a,b):
    return a + b
def sub(a,b):
    return a - b
def multi(a,b):
    return a * b
def dividir(a,b):
    if b == 0:
        return "Erro"
    return a / b

class Tests(unittest.TestCase):
    def test_somas(self):
        self.assertEqual(somar(5,5),10)
    def test_sub(self):
        self.assertEqual(sub(15,5),10)
    def test_multi(self):
        self.assertEqual(multi(5,2),10)
    def test_dividi(self):
        self.assertEqual(dividir(50,5),10)
    def test_dividi_erro(self):
        self.assertEqual(dividir(50,0),"Erro")

if __name__ == "__main__":
    unittest.main()