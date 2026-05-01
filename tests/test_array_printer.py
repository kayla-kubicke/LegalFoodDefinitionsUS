# Individual test runner command:
# 'python3 -m unittest tests/test_array_printer.py'

import unittest
from printer.array_printer import ArrayPrinter as array_printer
import io
from contextlib import redirect_stdout

# START: TestArrayPrinter Class
class TestArrayPrinter(unittest.TestCase):
	# START: Tests
	def test_array_custom_print_outputs_expected_list_to_terminal(self):
		# Really just tests the map joining stuff, but... better to include basic testing.
		test_array = ['One', 'Two', 'Three']
		expected_output = 'One\nTwo\nThree\n'
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			array_printer.array_custom_print(test_array)

		captured = string_buffer.getvalue()

		self.assertEqual(captured, expected_output)

	def test_array_custom_print_outputs_expected_message_to_terminal(self):
		test_array = []
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			array_printer.array_custom_print(test_array)

		captured = string_buffer.getvalue()

		self.assertEqual(captured, 'No results found. Food term does not appear in document.\n')
	# END: Tests
# END: TestArrayPrinter Class