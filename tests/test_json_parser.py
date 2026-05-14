# Individual test runner command:
# 'python3 -m unittest tests/test_json_parser.py'

# NOTE: Test suite is incomplete.
# This is a work in progress and needs a decent amount of clean up before merging.

# START: imports
import unittest
from unittest.mock import patch
from parser.json_parser import JSONParser as json_parser
from api.example_handler import ExampleHandler as example_handler
import io
from contextlib import redirect_stdout
# END: imports

# START: TestJSONParser Class
class TestJSONParser(unittest.TestCase):
	# START: Constants
	CHOCOLATE_REPSONSE = example_handler.example_response('example_requests', 'chocolate')
	VERMOUTH_REPSONSE = example_handler.example_response('example_requests', 'vermouth')
	AGENCIES_DATA = example_handler.example_response('agency_data', 'agencies')
	# END: Constants

	# START: Tests
	# title_and_chapter_found_in_agency_json tests
	# ADD: Expand agencies tested
	def test_title_and_chapter_found_returns_true_if_title_and_chapter_found(self):
		agency = TestJSONParser.AGENCIES_DATA['agencies'][0]['children'][0]
		bool_returned = json_parser.title_and_chapter_found_in_agency_json(agency, 7, 'I')

		self.assertEqual(bool_returned, True)


	def test_title_and_chapter_found_returns_false_if_title_and_chapter_not_found(self):
		agency = TestJSONParser.AGENCIES_DATA['agencies'][0]['children'][0]
		bool_returned = json_parser.title_and_chapter_found_in_agency_json(agency, 7, 'V')

		self.assertEqual(bool_returned, False)
	# title_and_chapter_found_in_agency_json tests


	# agencies_responsible_for_title_and_chapter tests
	def test_agencies_responsible_for_title_and_chapter_returns_array_expected_if_match_found_among_children(self):
		array_returned = json_parser.agencies_responsible_for_title_and_chapter(21, 'I')
		array_expected = ['FDA']

		self.assertEqual(array_returned, array_expected)


	def test_agencies_responsible_for_title_and_chapter_returns_array_expected_if_match_found_no_children(self):
		array_returned = json_parser.agencies_responsible_for_title_and_chapter(50, 'V')
		array_expected = ['MMC']

		self.assertEqual(array_returned, array_expected)


	def test_agencies_responsible_for_title_and_chapter_returns_empty_array_if_no_matches_are_found(self):
		array_returned = json_parser.agencies_responsible_for_title_and_chapter(450, 'I')

		self.assertEqual(array_returned, ['unknown'])
	# agencies_responsible_for_title_and_chapter tests


	# (!) UPDATE
	# search_results_dict tests
	def test_results_found_search_results_dict_returns_expected_author_set(self):
		dict_returned = json_parser.search_results_dict(TestJSONParser.CHOCOLATE_REPSONSE)

		expected_dict = {
			"result_1": {
					"Milk <strong>chocolate</strong>.": "(a) Description. (1) Milk <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">\u2026</span>intimately mixing and grinding <strong>chocolate</strong> liquor with one or more of the optional dairy ingredients<span class=\"elipsis\">\u2026</span>(2) Milk <strong>chocolate</strong> contains not less than 10 percent by weight of <strong>chocolate</strong> liquor complying",
					"authors": {"FDA"}
				},
			"result_2": {
					"Sweet <strong>chocolate</strong>.": "(a) Description. (1) Sweet <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">\u2026</span>intimately mixing and grinding <strong>chocolate</strong> liquor with one or more optional nutritive carbohydrate<span class=\"elipsis\">\u2026</span>(2) Sweet <strong>chocolate</strong> contains not less than 15 percent by weight of <strong>chocolate</strong> liquor complying",
					"authors": {"FDA"}
				},
			"result_3": {
					"White <strong>chocolate</strong>.": "(a) Description. (1) White <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">\u2026</span>section. White <strong>chocolate</strong> shall be free of coloring material. (2) White <strong>chocolate</strong> contains not<span class=\"elipsis\">\u2026</span>white <strong>chocolate</strong>, and multiplying the quotient by 100. The finished white <strong>chocolate</strong> contains",
					"authors": {"FDA"}
				}
		}

		self.assertEqual(dict_returned, expected_dict)


	def test_no_results_found_search_results_dict_returns_empty_array(self):
		dict_returned = json_parser.search_results_dict(TestJSONParser.VERMOUTH_REPSONSE)

		self.assertEqual(dict_returned, {})


	def test_search_results_dict_empty_dict_returns_empty_array(self):
		dict_returned = json_parser.search_results_dict({})

		self.assertEqual(dict_returned, {})


	def test_search_results_dict_returns_expected_dict_for_agency_array_containing_over_two_results(self):
		with patch.object(json_parser, 'agencies_responsible_for_title_and_chapter', return_value = ['ABC', 'EFG', 'HIJ']):
			dict_returned = json_parser.search_results_dict(TestJSONParser.CHOCOLATE_REPSONSE)

		dict_expected = {
		    "result_1": {
		        "Milk <strong>chocolate</strong>.": "(a) Description. (1) Milk <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">\u2026</span>intimately mixing and grinding <strong>chocolate</strong> liquor with one or more of the optional dairy ingredients<span class=\"elipsis\">\u2026</span>(2) Milk <strong>chocolate</strong> contains not less than 10 percent by weight of <strong>chocolate</strong> liquor complying",
		        "authors": {"ABC", "EFG", "HIJ"}
		    },
		    "result_2": {
		        "Sweet <strong>chocolate</strong>.": "(a) Description. (1) Sweet <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">\u2026</span>intimately mixing and grinding <strong>chocolate</strong> liquor with one or more optional nutritive carbohydrate<span class=\"elipsis\">\u2026</span>(2) Sweet <strong>chocolate</strong> contains not less than 15 percent by weight of <strong>chocolate</strong> liquor complying",
		        "authors": {"ABC", "EFG", "HIJ"}
		    },
		    "result_3": {
		        "White <strong>chocolate</strong>.": "(a) Description. (1) White <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">\u2026</span>section. White <strong>chocolate</strong> shall be free of coloring material. (2) White <strong>chocolate</strong> contains not<span class=\"elipsis\">\u2026</span>white <strong>chocolate</strong>, and multiplying the quotient by 100. The finished white <strong>chocolate</strong> contains",
		        "authors": {"ABC", "EFG", "HIJ"}
		    }
		}

		self.assertEqual(dict_returned, dict_expected)


	def test_search_results_dict_handles_exception(self):
		with patch.object(json_parser, 'search_results_dict', side_effect = Exception('Generic exception')):
			with self.assertRaises(Exception):
					json_parser.search_results_dict(TestJSONParser.CHOCOLATE_REPSONSE)


	# Technically, this only tests the output if the error occurs outside of the
	# original method call, but I'm going to let it be.
	# https://www.youtube.com/watch?v=WvwK3gPPXHM
	def test_search_results_dict_outputs_expected_when_exception_encountered(self):
		with patch.object(json_parser, 'agencies_responsible_for_title_and_chapter', side_effect = Exception('Generic exception')):
			string_buffer = io.StringIO()

			with redirect_stdout(string_buffer):
				json_parser.search_results_dict(TestJSONParser.CHOCOLATE_REPSONSE)

			captured_output = string_buffer.getvalue()

			self.assertEqual(captured_output[0:21], 'Generic error caught:')
	# search_results_dict tests


	def test_results_found_search_results_list(self):
		array_returned = json_parser.search_results_list(TestJSONParser.CHOCOLATE_REPSONSE)

		array_expected = [
			'Milk <strong>chocolate</strong>.',
			'Sweet <strong>chocolate</strong>.',
			'White <strong>chocolate</strong>.'
		]

		self.assertEqual(array_returned, array_expected)


	def test_no_results_found_search_results_list(self):
		array_returned = json_parser.search_results_list(TestJSONParser.VERMOUTH_REPSONSE)

		self.assertEqual(array_returned, [])
	# END: Tests
# END: TestJSONParser Class