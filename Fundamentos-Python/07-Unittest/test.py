import unittest
import funciones as func

# creo una clase que herede de unittest.TestCase


class My_test(unittest.TestCase):
    # creo una funcion (antecede la palabra test_nombre)
    def test_listaEnteros_01(self):
        # recibe dos parametros, el valor a analizar y el valor esperado
        valor_func = func.ListaEnteros(3, 5)
        valor_esperado = [3, 4, 5, 6, 7]
        self.assertEqual(valor_func, valor_esperado)

    def test_DividirDosNumeros_01(self):
        parte_entera, resto = func.DividirDosNumeros(9, 2)
        valor_func = [parte_entera, resto]
        valor_esperado = [4, 1]
        self.assertEqual(valor_func, valor_esperado)


# objeto con detalles y resultados de los test
resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)
# cantidad total de tests corridos
total_test = resultado_test.result.testsRun
# cantidad de fallas en los tests
fallas_test = len(resultado_test.result.failures)
# cantidad de errores en los tests
errores_test = len(resultado_test.result.errors)
# total de test correctos
ok_test = total_test - fallas_test - errores_test

print('resultados global: ', resultado_test)
print('resultados tests corridos: ', total_test)
print('fallas test: ', fallas_test)
print('errores test: ', errores_test)
print('Correctos test: ', ok_test)
