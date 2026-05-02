# Individual test runner command:
# 'python3 -m unittest tests/test_example_handler.py'

# START: imports
import unittest
from api.example_handler import ExampleHandler as example_handler
import io
from contextlib import redirect_stdout
from unittest.mock import patch
# END: imports

# START: TestExampleHandler Class
class TestExampleHandler(unittest.TestCase):
	# START: Tests

	# ADD TESTS: example_response(query)
	def test_example_response_returns_expected_object(self):
		returned_object = example_handler.example_response('chocolate')

		self.assertIsInstance(returned_object, dict)

	def test_invalid_file_example_response_outputs_expected_message_to_terminal(self):
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			example_handler.example_response('invalidfile')

		captured = string_buffer.getvalue()

		self.assertEqual(captured[0:15], 'File not found.')

	# Nope.
	# def test_example_response_outputs_expected_message_to_terminal(self):
	# 	with patch('example_handler.example_response', side_effect = OSError('whatever')):
	# 		captured = example_handler.example_response('whatever')

	# 		self.assertEqual(captured[0:20], 'Generic error caught:')
# END: Tests
# END: TestExampleHandler Class