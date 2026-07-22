# Individual test runner command:
# 'python3 -m unittest tests/test_admin_api_handler.py'

# START: imports
import unittest
from unittest.mock import patch
from api.api_handler import ApiHandler as api_handler
from api.admin_api_handler import AdminApiHandler as admin_api_handler
import api.api_constants as api_constants
import requests
import io
from contextlib import redirect_stdout
# END: imports

# This needs to be redone...

# class TestAdminApiHandler(unittest.TestCase):
# 	# START: AGENCIES Enum
# 	# ADD: same tests w/ ...build_url('wow params so magical')
#  	# build_url test(s)
# 	def test_build_url_returns_expected_object_agencies(self):
# 		admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.AGENCIES)
# 		object_returned = admin_api_handler_object.build_url()

# 		self.assertIsInstance(object_returned, str)

# 	def test_build_url_returns_expected_url_agencies(self):
# 		admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.AGENCIES)
# 		url_returned = admin_api_handler_object.build_url()

# 		url_expected = 'https://www.ecfr.gov/api/admin/v1/agencies.json'

# 		self.assertEqual(url_returned[0:47], url_expected)
# 	# build_url test(s)


# 	# api_call tests
# 	@patch('requests.get')
# 	def test_api_call_successful_returns_expected_object_agencies(self, mock_response):
# 		mock_response.return_value.status_code = 200
# 		mock_response.return_value.json.return_value = {'Example key': 'Example value'}

# 		admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.AGENCIES)
# 		object_returned = admin_api_handler_object.api_call(mock_response)
# 		self.assertIsInstance(object_returned, dict)


# 	@patch('requests.get')
# 	def test_api_call_non_200_terminates_with_expected_output_agencies(self, mock_response):
# 		mock_response.return_value.status_code = 404
# 		string_buffer = io.StringIO()

# 		with redirect_stdout(string_buffer):
# 			admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.AGENCIES)
# 			captured_output = admin_api_handler_object.api_call(mock_response)

# 		captured_output = string_buffer.getvalue()

# 		self.assertEqual(captured_output[0:16], 'Status code: 404')


# 	@patch('requests.get')
# 	def test_api_call_unsucessful_requests_call_raises_exception_agencies(self, mock_response):
# 		mock_response.side_effect = requests.exceptions.RequestException
# 		string_buffer = io.StringIO()

# 		with redirect_stdout(string_buffer):
# 			admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.AGENCIES)
# 			captured_output = admin_api_handler_object.api_call(mock_response)

# 		captured_output = string_buffer.getvalue()

# 		self.assertEqual(captured_output[0:26], 'requests exception caught:')


# 	@patch('requests.get')
# 	def test_api_call_unsucessful_raises_exception_agencies(self, mock_response):
# 		mock_response.side_effect = Exception('Generic exception')
# 		string_buffer = io.StringIO()

# 		with redirect_stdout(string_buffer):
# 			admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.AGENCIES)
# 			captured_output = admin_api_handler_object.api_call(mock_response)

# 		captured_output = string_buffer.getvalue()

# 		self.assertEqual(captured_output[0:25], 'Generic exception caught:')
#  	# api_call tests
# 	# END: AGENCIES Enum

# 	# START: CORRECTIONS Enum
#  	# build_url test(s)
# 	def test_build_url_returns_expected_object_corrections(self):
# 		admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.CORRECTIONS)
# 		object_returned = admin_api_handler_object.build_url()

# 		self.assertIsInstance(object_returned, str)

# 	def test_build_url_returns_expected_url_corrections(self):
# 		admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.CORRECTIONS)
# 		url_returned = admin_api_handler_object.build_url()

# 		url_expected = 'https://www.ecfr.gov/api/admin/v1/corrections.json'

# 		self.assertEqual(url_returned[0:59], url_expected)
# 	# build_url test(s)


# 	# api_call tests
# 	@patch('requests.get')
# 	def test_api_call_successful_returns_expected_object_corrections(self, mock_response):
# 		mock_response.return_value.status_code = 200
# 		mock_response.return_value.json.return_value = {'Example key': 'Example value'}

# 		admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.CORRECTIONS)
# 		object_returned = admin_api_handler_object.api_call(mock_response)
# 		self.assertIsInstance(object_returned, dict)


# 	@patch('requests.get')
# 	def test_api_call_non_200_terminates_with_expected_output_corrections(self, mock_response):
# 		mock_response.return_value.status_code = 404
# 		string_buffer = io.StringIO()

# 		with redirect_stdout(string_buffer):
# 			admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.CORRECTIONS)
# 			captured_output = admin_api_handler_object.api_call(mock_response)

# 		captured_output = string_buffer.getvalue()

# 		self.assertEqual(captured_output[0:16], 'Status code: 404')


# 	@patch('requests.get')
# 	def test_api_call_unsucessful_requests_call_raises_exception_corrections(self, mock_response):
# 		mock_response.side_effect = requests.exceptions.RequestException
# 		string_buffer = io.StringIO()

# 		with redirect_stdout(string_buffer):
# 			admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.CORRECTIONS)
# 			captured_output = admin_api_handler_object.api_call(mock_response)

# 		captured_output = string_buffer.getvalue()

# 		self.assertEqual(captured_output[0:26], 'requests exception caught:')


# 	@patch('requests.get')
# 	def test_api_call_unsucessful_raises_exception_corrections(self, mock_response):
# 		mock_response.side_effect = Exception('Generic exception')
# 		string_buffer = io.StringIO()

# 		with redirect_stdout(string_buffer):
# 			admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.CORRECTIONS)
# 			captured_output = admin_api_handler_object.api_call(mock_response)

# 		captured_output = string_buffer.getvalue()

# 		self.assertEqual(captured_output[0:25], 'Generic exception caught:')
#  	# api_call tests
# 	# END: CORRECTIONS Enum

# 	# START: CORRRECTIONS_TITLE Enum
#  	# build_url test(s)
# 	def test_build_url_returns_expected_object_corrections_title(self):
# 		admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.CORRECTIONS_TITLE)
# 		object_returned = admin_api_handler_object.build_url(1)

# 		self.assertIsInstance(object_returned, str)

# 	def test_build_url_returns_expected_url_corrections_title(self):
# 		admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.CORRECTIONS_TITLE)
# 		url_returned = admin_api_handler_object.build_url(1)

# 		url_expected = 'https://www.ecfr.gov/api/admin/v1/corrections/title.json'

# 		self.assertEqual(url_returned[0:47], url_expected[0:47])
# 	# build_url test(s)


# 	# api_call tests
# 	@patch('requests.get')
# 	def test_api_call_successful_returns_expected_object_corrections_title(self, mock_response):
# 		mock_response.return_value.status_code = 200
# 		mock_response.return_value.json.return_value = {'Example key': 'Example value'}

# 		admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.CORRECTIONS_TITLE)
# 		object_returned = admin_api_handler_object.api_call(mock_response)
# 		self.assertIsInstance(object_returned, dict)


# 	@patch('requests.get')
# 	def test_api_call_non_200_terminates_with_expected_output_corrections_title(self, mock_response):
# 		mock_response.return_value.status_code = 404
# 		string_buffer = io.StringIO()

# 		with redirect_stdout(string_buffer):
# 			admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.CORRECTIONS_TITLE)
# 			captured_output = admin_api_handler_object.api_call(mock_response)

# 		captured_output = string_buffer.getvalue()

# 		self.assertEqual(captured_output[0:16], 'Status code: 404')


# 	@patch('requests.get')
# 	def test_api_call_unsucessful_requests_call_raises_exception_corrections_title(self, mock_response):
# 		mock_response.side_effect = requests.exceptions.RequestException
# 		string_buffer = io.StringIO()

# 		with redirect_stdout(string_buffer):
# 			admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.CORRECTIONS_TITLE)
# 			captured_output = admin_api_handler_object.api_call(mock_response)

# 		captured_output = string_buffer.getvalue()

# 		self.assertEqual(captured_output[0:26], 'requests exception caught:')


# 	@patch('requests.get')
# 	def test_api_call_unsucessful_raises_exception_corrections_title(self, mock_response):
# 		mock_response.side_effect = Exception('Generic exception')
# 		string_buffer = io.StringIO()

# 		with redirect_stdout(string_buffer):
# 			admin_api_handler_object = admin_api_handler(admin_api_handler.AdminType.CORRECTIONS_TITLE)
# 			captured_output = admin_api_handler_object.api_call(mock_response)

# 		captured_output = string_buffer.getvalue()

# 		self.assertEqual(captured_output[0:25], 'Generic exception caught:')
#  	# api_call tests
# 	# END: CORRRECTIONS_TITLE Enum