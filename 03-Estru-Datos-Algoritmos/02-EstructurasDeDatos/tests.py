import unittest
import ejercicios as exc


class testRecursion(unittest.TestCase):

    def test_nFactorial_01(self):
        received_value = exc.nFactorial(5)
        expected_value = 120
        self.assertEqual(received_value, expected_value)

    def test_nFactorial_02(self):
        received_value = exc.nFactorial(8)
        expected_value = 40320
        self.assertEqual(received_value, expected_value)

    def test_nFactorial_03(self):
        received_value = exc.nFactorial(3)
        expected_value = 6
        self.assertEqual(received_value, expected_value)

    def test_nFibonacci_01(self):
        received_value = exc.nFibonnacci(3)
        expected_value = 2
        self.assertEqual(received_value, expected_value)

    def test_nFibonacci_02(self):
        received_value = exc.nFibonnacci(6)
        expected_value = 8
        self.assertEqual(received_value, expected_value)

    def test_nFibonacci_03(self):
        received_value = exc.nFibonnacci(8)
        expected_value = 21
        self.assertEqual(received_value, expected_value)


tests_results = unittest.main(argv=[''], verbosity=2, exit=False)
total_tests = tests_results.result.testsRun
fail_tests = len(tests_results.result.failures)
error_tests = len(tests_results.result.errors)
ok_tests = total_tests - fail_tests - error_tests

print('resultados global: ', tests_results)
print('resultados tests corridos: ', total_tests)
print('fallas test: ', fail_tests)
print('errores test: ', error_tests)
print('Correctos test: ', ok_tests)
