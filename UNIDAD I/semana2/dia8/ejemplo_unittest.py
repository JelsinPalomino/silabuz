import unittest
from random import randint

def mi_suma(a,b):
    return a+b


class TestCalculadoraAritmetica(unittest.TestCase):
    def __generate_pair_of_numbers(self):
        return [randint(1, 10), randint(1, 10)]

    def test_suma(self):
        a, b =self.__generate_pair_of_numbers()
        c = a + b
        c2 = mi_suma(a,b)
        self.assertEqual(c, c2)

if __name__=="__main__":
    unittest.main()
