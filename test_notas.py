import unittest
from notas import avaliar_notas

class Test_Avaliar_nota(unittest.TestCase):
    def test_excecao_caso_01(self):
        self.assertRaises(ValueError, avaliar_notas,-1,0,0,0)
    
    def test_mensagem_excecao_caso_02(self):
        msg = 'Valor inválido para n1'
        try:
            avaliar_notas(-1,0,0,0)
        except ValueError as e:
            message = str(e)
            self.assertEqual(msg, message)

    def test_excecao_caso_03(self):
        self.assertRaises(ValueError, avaliar_notas,0,-1,0,0)
    
    def test_mensagem_excecao_caso_04(self):
        msg = 'Valor inválido para n2'
        try:
            avaliar_notas(0,-1,0,0)
        except ValueError as e:
            message = str(e)
            self.assertEqual(msg, message)
    
    def test_excecao_caso_05(self):
        self.assertRaises(ValueError, avaliar_notas,0,-1,0,0)
    
    def test_mensagem_excecao_caso_06(self):
        msg = 'Valor inválido para n3'
        try:
            avaliar_notas(0,0,-1,0)
        except ValueError as e:
            message = str(e)
            self.assertEqual(msg, message)

    def test_letra_A_caso_07(self):
        self.assertEqual(avaliar_notas(10, 10, 10, 10), 'A')

    def test_letra_A_caso_08(self):
        self.assertEqual(avaliar_notas(9, 9, 9, 9), 'A')

    def test_letra_B_caso_09(self):
        self.assertEqual(avaliar_notas(8.9, 8.9, 8.9, 8.9), 'B')

    def test_letra_B_caso_10(self):
        self.assertEqual(avaliar_notas(7.5, 7.5, 7.5, 7.5), 'B')

    def test_letra_C_caso_11(self):
        self.assertEqual(avaliar_notas(7.4, 7.4, 7.4, 7.4), 'C')


    def test_letra_C_caso_12(self):
        self.assertEqual(avaliar_notas(6.0, 6.0, 6.0, 6.0), 'C')

    def test_letra_D_caso_13(self):
        self.assertEqual(avaliar_notas(5.9, 5.9, 5.9, 5.9), 'D')

    def test_letra_D_caso_14(self):
        self.assertEqual(avaliar_notas(0.0, 0.0, 0.0, 0.0), 'D')

    def test_mensagem_excecao_caso_15(self):
        msg = 'Valor inválido para media_exercicios'
        try:
            avaliar_notas(0,0,0,-1)
        except ValueError as e:
            message = str(e)
            self.assertEqual(msg, message)

    def test_mensagem_excecao_caso_16(self):
        msg = 'Valor inválido para media_exercicios'
        try:
            avaliar_notas(0,0,0,11)
        except ValueError as e:
            message = str(e)
            self.assertEqual(msg, message)

    

if __name__ == '__main__':
    unittest.main()