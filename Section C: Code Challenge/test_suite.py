"""unittest module used for the test suite,
    as well as our main driver code to be tested
    imported"""
import unittest
import resistor_networks

# Tests based on the unittest module using example data
class test_suite(unittest.TestCase):
    def test_resistor_value(self):

        # Samples for correct outcomes and calculations
        input_data = resistor_networks.process_resistors("(10, [20, 30])")
        self.assertEqual(input_data, 22.0, "Failed test, incorrect outcome")

        input_data = resistor_networks.process_resistors("[10, (20, 30)]")
        self.assertEqual(input_data, 8.3, "Failed test, incorrect outcome")

        input_data = resistor_networks.process_resistors("([10, 20], (30, 40))")
        self.assertEqual(input_data, 76.7, "Failed test, incorrect outcome")

        input_data = resistor_networks.process_resistors("(1, [12, 4, (1, [10, (2, 8)])])")
        self.assertEqual(input_data, 3.0, "Failed test, incorrect outcome")

        input_data = resistor_networks.process_resistors("(6, [8, (4, [8, (4, [6, (8, [6, (10, 2)])])])])")
        self.assertEqual(input_data, 10.0, "Failed test, incorrect outcome")

        # Samples for error handling of incorrect input
        input_data = resistor_networks.process_resistors("a string of words")
        self.assertEqual(input_data, None, "Failed test, incorrect outcome")

        input_data = resistor_networks.process_resistors(8)
        self.assertEqual(input_data, None, "Failed test, incorrect outcome")

unittest.main()
