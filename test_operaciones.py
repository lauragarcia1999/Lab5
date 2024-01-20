import unittest
from operaciones import sumar

class TestSumar(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()


from operaciones import restar

class TestRestar(unittest.TestCase):
    def test_restar(self):
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(5, 1), 4)
        self.assertEqual(restar(6, 1), 5)

if __name__ == '__main__':
    unittest.main()


from operaciones import multiplicar

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(1, 1), 1)
        self.assertEqual(multiplicar(8, 3), 24)

if __name__ == '__main__':
    unittest.main()    



from operaciones import dividir

class TestDividir(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(3, 2), 1.5)
        self.assertEqual(dividir(2, 1), 2)
        self.assertEqual(dividir(20, 10), 2)

if __name__ == '__main__':
    unittest.main()    