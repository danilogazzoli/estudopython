import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from source.auditoriaCorrentistas import AuditoriaCorrentistas



class TestAuditoriaMethods(unittest.TestCase):
    def setUp(self):
        self.__auditoria = AuditoriaCorrentistas()

    def test_adicionar(self):
        self.__auditoria.get_instance().adicionar_registros()

if __name__ == '__main__':
    unittest.main()


