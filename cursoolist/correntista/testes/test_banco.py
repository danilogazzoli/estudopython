import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from source.banco import Banco

class TestBancoMethods(unittest.TestCase):
    def setUp(self):
        self.__banco = Banco()

    def test_saque(self):
        self.assertEqual(self.__correntista.saldo, 100, 'Saldo inicial está errado')
        self.__correntista.saque(50)
        self.assertEqual(self.__correntista.saldo, 50, 'Saldo ficou errado, deveria ser 50.')
        
    def test_deposita(self):
        self.assertEqual(self.__correntista.saldo, 100, 'Saldo inicial está errado, é esperado o valor de 100.')
        self.__correntista.deposita(100)
        self.assertEqual(self.__correntista.saldo, 200, 'Saldo ficou errado, deveria ser 200.')


if __name__ == '__main__':
    unittest.main()