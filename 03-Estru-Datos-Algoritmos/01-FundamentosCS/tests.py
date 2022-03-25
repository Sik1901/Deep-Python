import unittest
import c_science as exr


class testsExercises(unittest.TestCase):

    def test_decimalToBinary_01(self):
        received_value = exr.decimalToBinary(24)
        expected_value = '11000'
        self.assertEqual(received_value, expected_value)

    def test_decimalToBinary_02(self):
        received_value = exr.decimalToBinary(7)
        expected_value = '111'
        self.assertEqual(received_value, expected_value)

    def test_decimalToBinary_03(self):
        received_value = exr.decimalToBinary(7)
        expected_value = '111'
        self.assertEqual(received_value, expected_value)

    def test_binaryToDecimal_01(self):
        received_value = exr.binaryToDecimal('10101')
        expected_value = 21
        self.assertEqual(received_value, expected_value)

    def test_binaryToDecimal_02(self):
        received_value = exr.binaryToDecimal('11111')
        expected_value = 31
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
