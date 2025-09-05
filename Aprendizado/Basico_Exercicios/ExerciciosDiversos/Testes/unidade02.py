import unittest

def tem_fruta(fruta,lista):
    if fruta in lista:
        return "Fruta esta na lista"
    else:
        return "Não esta"

class TesteFruta(unittest.TestCase):
    def test_verifica_fruta(self):
        self.assertEqual(tem_fruta("maca", ["maca", "banana", "uva"]), "Fruta esta na lista")

    def test_fruta_nao_existe(self):
        self.assertEqual(tem_fruta("laranja", ["maca", "banana", "uva"]), "Não esta")

if __name__ == "__main__":
    unittest.main()
