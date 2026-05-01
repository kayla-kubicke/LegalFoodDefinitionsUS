# Individual test runner command:
# 'python3 -m unittest tests/test_dictionary_printer.py'

import unittest
# import subprocess
from printer.dictionary_printer import DictionaryPrinter as dictionary_printer
import io
from contextlib import redirect_stdout

# START: TestDictionaryPrinter Class
class TestDictionaryPrinter(unittest.TestCase):
	# START: Tests

	# ADD TESTS: dict_key_custom_print(dictionary)
	def test_dict_key_custom_print_outputs_expected_key_list_to_terminal(self):
		test_dict = {'One': 'value_one', 'Two': 'value_two', 'Three': 'value_three'}
		expected_output = 'One\nTwo\nThree\n'
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			dictionary_printer.dict_key_custom_print(test_dict)

		captured = string_buffer.getvalue()

		self.assertEqual(captured, expected_output)

	def test_dict_key_custom_print_outputs_expected_message_to_terminal(self):
		test_dict = {}
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			dictionary_printer.dict_key_custom_print(test_dict)

		captured = string_buffer.getvalue()

		self.assertEqual(captured, 'No results found. Food term does not appear in document.\n')
	# END: Tests
# END: TestDictionaryPrinter Class