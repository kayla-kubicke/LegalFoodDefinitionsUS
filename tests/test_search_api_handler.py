# Individual test runner command:
# 'python3 -m unittest tests/test_search_api_handler.py'

# START: imports
import unittest
from unittest.mock import patch
from api.api_handler import ApiHandler as api_handler
from api.search_api_handler import SearchApiHandler as search_api_handler
import api.api_constants as api_constants
import requests
import io
from contextlib import redirect_stdout
# END: imports

# UPDATE: Need to test all Enums...

# START: TestSearchApiHandler Class
class TestSearchApiHandler(unittest.TestCase):
	# format_agency_parameter test(s)
	def test_format_agency_parameter_returns_expected_string(self):
		test_slug_array = [
			api_constants.USDA, api_constants.EPA,
			api_constants.FDA, api_constants.FWS,
			api_constants.ATF, api_constants.MMC
		]

		test_string = search_api_handler.format_agency_parameter(test_slug_array)

		string_expected = 'agency_slugs%5B%5D=agriculture-department&' \
		'agency_slugs%5B%5D=environmental-protection-agency&' \
		'agency_slugs%5B%5D=food-and-drug-administration&' \
		'agency_slugs%5B%5D=fish-and-wildlife-service&' \
		'agency_slugs%5B%5D=alcohol-tobacco-firearms-and-explosives-bureau&' \
		'agency_slugs%5B%5D=marine-mammal-commission&' \

		self.assertEqual(test_string, string_expected)
	# format_agency_parameter test(s)


	# START: RESULTS Enum
	# build_url test(s)
	def test_build_url_returns_expected_object_results(self):
		search_api_handler_object = search_api_handler(search_api_handler.SearchType.RESULTS)
		object_returned = search_api_handler_object.build_url('example_query')

		self.assertIsInstance(object_returned, str)

	def test_build_url_returns_expected_url(self):
		search_api_handler_object = search_api_handler(search_api_handler.SearchType.RESULTS)
		url_returned = search_api_handler_object.build_url('chocolate')

		url_expected = 'https://www.ecfr.gov/api/search/v1/results?query=chocolate&agency_slugs%5B%5D=agriculture-department&agency_slugs%5B%5D=food-and-drug-administration&agency_slugs%5B%5D=environmental-protection-agency&agency_slugs%5B%5D=fish-and-wildlife-service&agency_slugs%5B%5D=alcohol-tobacco-firearms-and-explosives-bureau&agency_slugs%5B%5D=marine-mammal-commission&per_page=3&page=1&order=relevance&paginate_by=results'

		self.assertEqual(url_returned[0:60], url_expected[0:60])
	# build_url test(s)


	# api_call tests
	@patch('requests.get')
	def test_api_call_successful_returns_expected_object_results(self, mock_response):
		mock_response.return_value.status_code = 200
		mock_response.return_value.json.return_value = {'Example key': 'Example value'}

		search_api_handler_object = search_api_handler(search_api_handler.SearchType.RESULTS)
		object_returned = search_api_handler_object.api_call(mock_response)
		self.assertIsInstance(object_returned, dict)


	@patch('requests.get')
	def test_api_call_non_200_terminates_with_expected_output_results(self, mock_response):
		mock_response.return_value.status_code = 404
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			search_api_handler_object = search_api_handler(search_api_handler.SearchType.RESULTS)
			captured_output = search_api_handler_object.api_call(mock_response)

		captured_output = string_buffer.getvalue()

		self.assertEqual(captured_output[0:16], 'Status code: 404')


	@patch('requests.get')
	def test_api_call_unsucessful_requests_call_raises_exception_results(self, mock_response):
		mock_response.side_effect = requests.exceptions.RequestException
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			search_api_handler_object = search_api_handler(search_api_handler.SearchType.RESULTS)
			captured_output = search_api_handler_object.api_call(mock_response)

		captured_output = string_buffer.getvalue()

		self.assertEqual(captured_output[0:26], 'requests exception caught:')


	@patch('requests.get')
	def test_api_call_unsucessful_raises_exception_results(self, mock_response):
		mock_response.side_effect = Exception('Generic exception')
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			search_api_handler_object = search_api_handler(search_api_handler.SearchType.RESULTS)
			captured_output = search_api_handler_object.api_call(mock_response)

		captured_output = string_buffer.getvalue()

		self.assertEqual(captured_output[0:25], 'Generic exception caught:')
	# api_call tests
	# END: RESULTS Enum

	# START: COUNT Enum
	# build_url test(s)
	def test_build_url_returns_expected_object_count(self):
		search_api_handler_object = search_api_handler(search_api_handler.SearchType.COUNT)
		object_returned = search_api_handler_object.build_url('example_query')

		self.assertIsInstance(object_returned, str)

	def test_build_url_returns_expected_url(self):
		search_api_handler_object = search_api_handler(search_api_handler.SearchType.COUNT)
		url_returned = search_api_handler_object.build_url('chocolate')

		url_expected = 'https://www.ecfr.gov/api/search/v1/count?query=chocolate&agency_slugs%5B%5D=agriculture-department&agency_slugs%5B%5D=food-and-drug-administration&agency_slugs%5B%5D=environmental-protection-agency&agency_slugs%5B%5D=fish-and-wildlife-service&agency_slugs%5B%5D=alcohol-tobacco-firearms-and-explosives-bureau&agency_slugs%5B%5D=marine-mammal-commission&per_page=3&page=1&order=relevance&paginate_by=results'

		self.assertEqual(url_returned[0:60], url_expected[0:60])
	# build_url test(s)


	# api_call tests
	@patch('requests.get')
	def test_api_call_successful_returns_expected_object_count(self, mock_response):
		mock_response.return_value.status_code = 200
		mock_response.return_value.json.return_value = {'Example key': 'Example value'}

		search_api_handler_object = search_api_handler(search_api_handler.SearchType.COUNT)
		object_returned = search_api_handler_object.api_call(mock_response)
		self.assertIsInstance(object_returned, dict)


	@patch('requests.get')
	def test_api_call_non_200_terminates_with_expected_output_count(self, mock_response):
		mock_response.return_value.status_code = 404
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			search_api_handler_object = search_api_handler(search_api_handler.SearchType.COUNT)
			captured_output = search_api_handler_object.api_call(mock_response)

		captured_output = string_buffer.getvalue()

		self.assertEqual(captured_output[0:16], 'Status code: 404')


	@patch('requests.get')
	def test_api_call_unsucessful_requests_call_raises_exception_count(self, mock_response):
		mock_response.side_effect = requests.exceptions.RequestException
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			search_api_handler_object = search_api_handler(search_api_handler.SearchType.COUNT)
			captured_output = search_api_handler_object.api_call(mock_response)

		captured_output = string_buffer.getvalue()

		self.assertEqual(captured_output[0:26], 'requests exception caught:')


	@patch('requests.get')
	def test_api_call_unsucessful_raises_exception_count(self, mock_response):
		mock_response.side_effect = Exception('Generic exception')
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			search_api_handler_object = search_api_handler(search_api_handler.SearchType.COUNT)
			captured_output = search_api_handler_object.api_call(mock_response)

		captured_output = string_buffer.getvalue()

		self.assertEqual(captured_output[0:25], 'Generic exception caught:')
	# api_call tests
	# END: COUNT Enum

	# START: SUMMARY Enum
	# build_url test(s)
	def test_build_url_returns_expected_object_summary(self):
		search_api_handler_object = search_api_handler(search_api_handler.SearchType.SUMMARY)
		object_returned = search_api_handler_object.build_url('example_query')

		self.assertIsInstance(object_returned, str)

	def test_build_url_returns_expected_url(self):
		search_api_handler_object = search_api_handler(search_api_handler.SearchType.SUMMARY)
		url_returned = search_api_handler_object.build_url('chocolate')

		url_expected = 'https://www.ecfr.gov/api/search/v1/summary?query=chocolate&agency_slugs%5B%5D=agriculture-department&agency_slugs%5B%5D=food-and-drug-administration&agency_slugs%5B%5D=environmental-protection-agency&agency_slugs%5B%5D=fish-and-wildlife-service&agency_slugs%5B%5D=alcohol-tobacco-firearms-and-explosives-bureau&agency_slugs%5B%5D=marine-mammal-commission&per_page=3&page=1&order=relevance&paginate_by=results'

		self.assertEqual(url_returned[0:60], url_expected[0:60])
	# build_url test(s)


	# api_call tests
	@patch('requests.get')
	def test_api_call_successful_returns_expected_object_summary(self, mock_response):
		mock_response.return_value.status_code = 200
		mock_response.return_value.json.return_value = {'Example key': 'Example value'}

		search_api_handler_object = search_api_handler(search_api_handler.SearchType.SUMMARY)
		object_returned = search_api_handler_object.api_call(mock_response)
		self.assertIsInstance(object_returned, dict)


	@patch('requests.get')
	def test_api_call_non_200_terminates_with_expected_output_summary(self, mock_response):
		mock_response.return_value.status_code = 404
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			search_api_handler_object = search_api_handler(search_api_handler.SearchType.SUMMARY)
			captured_output = search_api_handler_object.api_call(mock_response)

		captured_output = string_buffer.getvalue()

		self.assertEqual(captured_output[0:16], 'Status code: 404')


	@patch('requests.get')
	def test_api_call_unsucessful_requests_call_raises_exception_summary(self, mock_response):
		mock_response.side_effect = requests.exceptions.RequestException
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			search_api_handler_object = search_api_handler(search_api_handler.SearchType.SUMMARY)
			captured_output = search_api_handler_object.api_call(mock_response)

		captured_output = string_buffer.getvalue()

		self.assertEqual(captured_output[0:26], 'requests exception caught:')


	@patch('requests.get')
	def test_api_call_unsucessful_raises_exception_summary(self, mock_response):
		mock_response.side_effect = Exception('Generic exception')
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			search_api_handler_object = search_api_handler(search_api_handler.SearchType.SUMMARY)
			captured_output = search_api_handler_object.api_call(mock_response)

		captured_output = string_buffer.getvalue()

		self.assertEqual(captured_output[0:25], 'Generic exception caught:')
	# api_call tests
	# END: SUMMARY Enum

	# START: COUNTS_DATES Enum
	# build_url test(s)
	def test_build_url_returns_expected_object_counts_dates(self):
		search_api_handler_object = search_api_handler(search_api_handler.SearchType.COUNTS_DATES)
		object_returned = search_api_handler_object.build_url('example_query')

		self.assertIsInstance(object_returned, str)

	def test_build_url_returns_expected_url(self):
		search_api_handler_object = search_api_handler(search_api_handler.SearchType.COUNTS_DATES)
		url_returned = search_api_handler_object.build_url('chocolate')

		url_expected = 'https://www.ecfr.gov/api/search/v1/counts/daily?query=chocolate&agency_slugs%5B%5D=agriculture-department&agency_slugs%5B%5D=food-and-drug-administration&agency_slugs%5B%5D=environmental-protection-agency&agency_slugs%5B%5D=fish-and-wildlife-service&agency_slugs%5B%5D=alcohol-tobacco-firearms-and-explosives-bureau&agency_slugs%5B%5D=marine-mammal-commission&per_page=3&page=1&order=relevance&paginate_by=results'

		self.assertEqual(url_returned[0:60], url_expected[0:60])
	# build_url test(s)


	# api_call tests
	@patch('requests.get')
	def test_api_call_successful_returns_expected_object_counts_dates(self, mock_response):
		mock_response.return_value.status_code = 200
		mock_response.return_value.json.return_value = {'Example key': 'Example value'}

		search_api_handler_object = search_api_handler(search_api_handler.SearchType.COUNTS_DATES)
		object_returned = search_api_handler_object.api_call(mock_response)
		self.assertIsInstance(object_returned, dict)


	@patch('requests.get')
	def test_api_call_non_200_terminates_with_expected_output_counts_dates(self, mock_response):
		mock_response.return_value.status_code = 404
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			search_api_handler_object = search_api_handler(search_api_handler.SearchType.COUNTS_DATES)
			captured_output = search_api_handler_object.api_call(mock_response)

		captured_output = string_buffer.getvalue()

		self.assertEqual(captured_output[0:16], 'Status code: 404')


	@patch('requests.get')
	def test_api_call_unsucessful_requests_call_raises_exception_counts_dates(self, mock_response):
		mock_response.side_effect = requests.exceptions.RequestException
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			search_api_handler_object = search_api_handler(search_api_handler.SearchType.COUNTS_DATES)
			captured_output = search_api_handler_object.api_call(mock_response)

		captured_output = string_buffer.getvalue()

		self.assertEqual(captured_output[0:26], 'requests exception caught:')


	@patch('requests.get')
	def test_api_call_unsucessful_raises_exception_counts_dates(self, mock_response):
		mock_response.side_effect = Exception('Generic exception')
		string_buffer = io.StringIO()

		with redirect_stdout(string_buffer):
			search_api_handler_object = search_api_handler(search_api_handler.SearchType.COUNTS_DATES)
			captured_output = search_api_handler_object.api_call(mock_response)

		captured_output = string_buffer.getvalue()

		self.assertEqual(captured_output[0:25], 'Generic exception caught:')
	# api_call tests
	# END: COUNTS_DATES Enum

	# START: COUNTS_TITLE Enum
	# END: COUNTS_TITLE Enum

	# START:COUNTS_HIERARCHY Enum
	# END: COUNTS_HIERARCHY Enum

	# START: SUGGESTIONS Enum
	# END: SUGGESTIONS Enum
# END: TestSearchApiHandler Class