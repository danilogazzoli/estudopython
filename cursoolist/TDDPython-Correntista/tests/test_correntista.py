import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from financas.correntista import Correntista

class TestCorrentista(unittest.TestCase):
    def setUp(self):
        self.correntista = Correntista("Nome", "12345678901", 10.0)

    def test_atributos(self):
        self.assertEqual(self.correntista.nome(), "Nome")
        self.assertEqual(self.correntista.cpf(), "12345678901")
        self.assertEqual(self.correntista.saldo(), 10.0)

    def test_deposito(self):
        self.correntista.deposita(10.0)
        self.assertEqual(self.correntista.saldo(), 20.0)

    def test_deposito_invalido(self):
        with self.assertRaises(ValueError):
            self.correntista.deposita(-5.0)
        with self.assertRaises(ValueError):
            self.correntista.deposita(0.0)
        with self.assertRaises(TypeError):
            self.correntista.deposita("aa")

    def test_saque(self):
        self.correntista.saque(5.0)
        self.assertEqual(self.correntista.saldo(), 5.0)
        self.correntista.saque(1.0)
        self.assertEqual(self.correntista.saldo(), 4.0)

    def test_saque_invalido(self):
        with self.assertRaises(ValueError):
            self.correntista.saque(-10.0)
        with self.assertRaises(ValueError):
            self.correntista.saque(0.0)
        with self.assertRaises(TypeError):
            self.correntista.saque("a")

    def test_saque_proibido(self):
        with self.assertRaises(ValueError):
            self.correntista.saque(20.0)

if __name__ == "__main__":
    unittest.main()