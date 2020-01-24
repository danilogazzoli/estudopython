import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO', 'o Foo não ficou maiusculo.')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()


    dentro do folder financas criar um arquivo __init__.py vazio
    criar os testes na pasta testes 
    from financas.correntista import Correntista

    dentro dos testes:

    import os
    import sys
    # para funcionar o visual studio code:
    sys.path.insert(0, os.path.abspath(os.path.join.(os.path.dirname(__file__), '..')))