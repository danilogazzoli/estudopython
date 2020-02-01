import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from source.banco import Banco

class TestBancoMethods(unittest.TestCase):
    def setUp(self):
        self.__banco = Banco()

    def test_cadastra_correntista(self):
        c = self.__banco.findCorrentistaPorCodigo(-1)
        self.assertEqual(c, None, 'Correntista tem que ser None')
        self.__banco.cadastra_correntista()
        
        self.__correntista.saque(50)
        self.assertEqual(self.__correntista.saldo, 50, 'Saldo ficou errado, deveria ser 50.')
        


if __name__ == '__main__':
    unittest.main()