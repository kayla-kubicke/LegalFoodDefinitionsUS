# Individual test runner command:
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
	def test_format_agency_parameter_returns_expected_string(self, mock_repsonse):
		# https://www.youtube.com/watch?v=1tsIxNci_dE
		test_slug_array = [api_handler.USDA, api_handler.EPA, api_handler.FDA, api_handler.FWS, api_handler.ATF, api_handler.MMC]
		test_string = api_handler.format_agency_parameter(test_slug_array)

		expected_string = 'agency_slugs%5B%5D=agriculture-department&' \
		'agency_slugs%5B%5D=environmental-protection-agency&' \
		'agency_slugs%5B%5D=food-and-drug-administration&' \
		'agency_slugs%5B%5D=fish-and-wildlife-service&' \
		'agency_slugs%5B%5D=alcohol-tobacco-firearms-and-explosives-bureau&' \
		'agency_slugs%5B%5D=marine-mammal-commission&' \

		self.assertEqual(test_string, expected_string)

	def test_successful_simple_call_returns_expected_object(self, mock_response):
		# Set value(s) for mock_response
		mock_response.return_value.status_code = 200
		mock_response.return_value.json.return_value = {'Example key': 'Example value'}

		test_response = api_handler.simple_call(mock_response)
		self.assertIsInstance(test_response, dict)

	def test_unsucessful_simple_call_raises_exception(self, mock_response):
		mock_response.return_value.status_code = 404

		with self.assertRaises(RuntimeError):
			api_handler.simple_call(mock_response)
	# END: Tests
# END: TestApiHandler Class