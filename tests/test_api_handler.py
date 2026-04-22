# Test runner command:
# 'python3 -m unittest tests/test_api_handler.py'

# START: imports & patch(es)
import unittest
from unittest.mock import patch
from api.api_handler import ApiHandler as api_handler
@patch('requests.get')
# END: imports & patch(es)

# START: TestApiHandler Class
class TestApiHandler(unittest.TestCase):
	# START: Tests
	def test_successful_simple_call_returns_expected_object(self, mock_response):
		# Set value(s) for mock_response
		mock_response.return_value.status_code = 200
		mock_response.return_value.json.return_value = {'Example key': 'Example value'}

		test_response = api_handler.simple_call(mock_response)
		self.assertIsInstance(test_response, dict)

	def test_unsucessful_simple_call_raises_exception(self, mock_response):
		mock_response.return_value.status_code = 404

		with self.assertRaises(RuntimeError):
			test_response = api_handler.simple_call(mock_response)
	# END: Tests
# END: TestApiHandler Class