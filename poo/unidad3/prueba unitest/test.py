from calculadora import *
import unittest


class Test(unittest.TestCase):
    def test_suma_1(self):
        self.assertEqual(suma(1, 2), 3)
        
    def testMaximo(self):
        lista = [1, 2, 3, 4, 5, 20, 100]
        self.assertGreater(maximo(lista), 10)
        self.assertLess(maximo(lista), 109)
        
    def testBuscar(self):
        lista = [1, 2, 3, 4, 5, 20, 100]
        self.assertTrue(buscarElemento(lista, 20))
        self.assertFalse(buscarElemento(lista, 10))
        self.assertIn(20, lista)

if __name__ == '__main__':
    unittest.main()
    
    