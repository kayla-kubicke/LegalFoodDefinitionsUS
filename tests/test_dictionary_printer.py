# Individual test runner command:
# 'python3 -m unittest tests/test_dictionary_printer.py'

import unittest
from printer.dictionary_printer import DictionaryPrinter as dictionary_printer
import io
from contextlib import redirect_stdout

# START: TestDictionaryPrinter Class
class TestDictionaryPrinter(unittest.TestCase):
	# START: Tests
	def test_dict_key_custom_print_outputs_expected_key_list_to_terminal(self):
		test_dict = {'One': 'value_one', 'Two': 'value_two', 'Three': 'value_three'}
		output_expected = 'One\nTwo\nThree\n'
		string_stream = io.StringIO()

		with redirect_stdout(string_stream):
			dictionary_printer.dict_key_custom_print(test_dict)

		captured_output = string_stream.getvalue()

		self.assertEqual(captured_output, output_expected)


	def test_dict_key_custom_print_outputs_expected_message_to_terminal(self):
		test_dict = {}
		string_stream = io.StringIO()

		with redirect_stdout(string_stream):
			dictionary_printer.dict_key_custom_print(test_dict)

		captured_output = string_stream.getvalue()

		self.assertEqual(captured_output, 'No results found. Food term does not appear in document.\n')
	# END: Tests
# END: TestDictionaryPrinter Class