# Individual test runner command:
# 'python3 -m unittest tests/test_api_handler.py'

# START: imports
import unittest
from unittest.mock import patch
from api.api_handler import ApiHandler as api_handler
import requests
import io
from contextlib import redirect_stdout
# END: imports

# START: TestApiHandler Class
class TestApiHandler(unittest.TestCase):
	# format_agency_parameter test(s)
	def test_format_agency_parameter_returns_expected_string(self):
		test_slug_array = [
			api_handler.USDA, api_handler.EPA,
			api_handler.FDA, api_handler.FWS,
			api_handler.ATF, api_handler.MMC
		]
		test_string = api_handler.format_agency_parameter(test_slug_array)

		string_expected = 'agency_slugs%5B%5D=agriculture-department&' \
		'agency_slugs%5B%5D=environmental-protection-agency&' \
		'agency_slugs%5B%5D=food-and-drug-administration&' \
		'agency_slugs%5B%5D=fish-and-wildlife-service&' \
		'agency_slugs%5B%5D=alcohol-tobacco-firearms-and-explosives-bureau&' \
		'agency_slugs%5B%5D=marine-mammal-commission&' \

		self.assertEqual(test_string, string_expected)
	# format_agency_parameter test(s)


	# search_results_call tests
	@patch('requests.get')
	def test_search_results_call_successful_returns_expected_object(self, mock_response):
		mock_response.return_value.status_code = 200
		mock_response.return_value.json.return_value = {'Example key': 'Example value'}

		object_returned = api_handler.search_results_call(mock_response)
		self.assertIsInstance(object_returned, dict)


	@patch('requests.get')
	def test_search_results_call_non_200_terminates_with_expected_output(self, mock_response):
		mock_response.return_value.status_code = 404
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			captured_output = api_handler.search_results_call(mock_response)

		captured_output = string_buffer.getvalue()

		self.assertEqual(captured_output[0:16], 'Status code: 404')


	@patch('requests.get')
	def test_search_results_call_unsucessful_requests_call_raises_exception(self, mock_response):
		mock_response.side_effect = requests.exceptions.RequestException
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			captured_output = api_handler.search_results_call(mock_response)

		captured_output = string_buffer.getvalue()

		self.assertEqual(captured_output[0:26], 'requests exception caught:')


	@patch('requests.get')
	def test_search_results_call_unsucessful_raises_exception(self, mock_response):
		mock_response.side_effect = Exception('Generic exception')
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			captured_output = api_handler.search_results_call(mock_response)

		captured_output = string_buffer.getvalue()

		self.assertEqual(captured_output[0:25], 'Generic exception caught:')
	# search_results_call tests
# END: TestApiHandler Class