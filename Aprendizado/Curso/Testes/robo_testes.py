import unittest

from robo import Robo

class RoboTestes(unittest.TestCase):
    def setUp(self):
        self.megaman = Robo("Mega man" , bateria=50)
    
    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)
    
    def test_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(), "Meu nome é MEGA MAN")
    
    def tearDown(self):
        print("teardown() executando")

if __name__ == "__main__":
    unittest.main()