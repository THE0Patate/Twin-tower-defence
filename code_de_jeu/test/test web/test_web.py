from code_de_l_application_web.Contrôle import Controle
import unittest

class TEST(unittest.TestCase):

    def __init__(self) -> None:
        Controle(3000)

if __name__ == '__main__':
    unittest.main()