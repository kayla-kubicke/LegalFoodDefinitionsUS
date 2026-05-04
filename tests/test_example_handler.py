# Individual test runner command:
# 'python3 -m unittest tests/test_example_handler.py'

# START: imports
import unittest
from api.example_handler import ExampleHandler as example_handler
import io
from contextlib import redirect_stdout
from unittest.mock import patch, mock_open
# END: imports

# START: TestExampleHandler Class
class TestExampleHandler(unittest.TestCase):
	# START: Tests
	def test_example_response_returns_expected_object(self):
		object_returned = example_handler.example_response('chocolate')

		self.assertIsInstance(object_returned, dict)


	def test_invalid_file_example_response_outputs_expected_message_to_terminal(self):
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			example_handler.example_response('invalidfile')

		captured_output = string_buffer.getvalue()

		self.assertEqual(captured_output[0:15], 'File not found.')


	@patch('api.example_handler.open')
	def test_example_response_outputs_expected_message_to_terminal(self, patch):
		string_buffer = io.StringIO()
		patch.side_effect = Exception('generic exception')
		with redirect_stdout(string_buffer):
			example_handler.example_response(patch)

		captured_output = string_buffer.getvalue()

		self.assertEqual(captured_output[0:21], 'Generic error caught:')
	# END: Tests
# END: TestExampleHandler Class