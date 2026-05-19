# Individual test runner command:
# 'python3 -m unittest tests/test_json_parser.py'

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
	def test_agencies_responsible_for_title_and_chapter_returns_set_expected_if_match_found_among_children_set_default(self):
		json_parser_object = json_parser()
		set_returned = json_parser_object.agencies_responsible_for_title_and_chapter(21, 'I')
		set_expected = {'FDA'}

		self.assertEqual(set_returned, set_expected)


	def test_agencies_responsible_for_title_and_chapter_returns_list_expected_if_match_found_among_children_list(self):
		json_parser_object = json_parser(json_parser.AuthorObjectType.LIST)
		list_returned = json_parser_object.agencies_responsible_for_title_and_chapter(21, 'I')
		list_expected = ['FDA']

		self.assertEqual(list_returned, list_expected)


	def test_agencies_responsible_for_title_and_chapter_returns_set_expected_if_match_found_no_children_set_default(self):
		json_parser_object = json_parser()
		set_returned = json_parser_object.agencies_responsible_for_title_and_chapter(50, 'V')
		set_expected = {'MMC'}

		self.assertEqual(set_returned, set_expected)


	def test_agencies_responsible_for_title_and_chapter_returns_list_expected_if_match_found_no_children_list(self):
		json_parser_object = json_parser(json_parser.AuthorObjectType.LIST)
		list_returned = json_parser_object.agencies_responsible_for_title_and_chapter(50, 'V')
		list_expected = ['MMC']

		self.assertEqual(list_returned, list_expected)


	def test_agencies_responsible_for_title_and_chapter_returns_empty_set_if_no_matches_are_found_set_default(self):
		json_parser_object = json_parser()
		set_returned = json_parser_object.agencies_responsible_for_title_and_chapter(450, 'I')

		self.assertEqual(set_returned, {'unknown'})


	def test_agencies_responsible_for_title_and_chapter_returns_empty_list_if_no_matches_are_found_list(self):
		json_parser_object = json_parser(json_parser.AuthorObjectType.LIST)
		list_returned = json_parser_object.agencies_responsible_for_title_and_chapter(450, 'I')

		self.assertEqual(list_returned, ['unknown'])
	# agencies_responsible_for_title_and_chapter tests


# 	# search_results_dict tests
	def test_search_results_dict_returns_expected_author_if_results_found_default_set(self):
		json_parser_object = json_parser()
		dict_returned = json_parser_object.search_results_dict(TestJSONParser.CHOCOLATE_REPSONSE)

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


	def test_search_results_dict_returns_expected_author_if_results_found_list(self):
		json_parser_object = json_parser(json_parser.AuthorObjectType.LIST)
		dict_returned = json_parser_object.search_results_dict(TestJSONParser.CHOCOLATE_REPSONSE)

		expected_dict = {
			"result_1": {
					"Milk <strong>chocolate</strong>.": "(a) Description. (1) Milk <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">\u2026</span>intimately mixing and grinding <strong>chocolate</strong> liquor with one or more of the optional dairy ingredients<span class=\"elipsis\">\u2026</span>(2) Milk <strong>chocolate</strong> contains not less than 10 percent by weight of <strong>chocolate</strong> liquor complying",
					"authors": ["FDA"]
				},
			"result_2": {
					"Sweet <strong>chocolate</strong>.": "(a) Description. (1) Sweet <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">\u2026</span>intimately mixing and grinding <strong>chocolate</strong> liquor with one or more optional nutritive carbohydrate<span class=\"elipsis\">\u2026</span>(2) Sweet <strong>chocolate</strong> contains not less than 15 percent by weight of <strong>chocolate</strong> liquor complying",
					"authors": ["FDA"]
				},
			"result_3": {
					"White <strong>chocolate</strong>.": "(a) Description. (1) White <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">\u2026</span>section. White <strong>chocolate</strong> shall be free of coloring material. (2) White <strong>chocolate</strong> contains not<span class=\"elipsis\">\u2026</span>white <strong>chocolate</strong>, and multiplying the quotient by 100. The finished white <strong>chocolate</strong> contains",
					"authors": ["FDA"]
				}
		}

		self.assertEqual(dict_returned, expected_dict)


	def test_search_results_dict_if_no_results_found_returns_empty_dict_with_default_set(self):
		json_parser_object = json_parser()
		dict_returned = json_parser_object.search_results_dict(TestJSONParser.VERMOUTH_REPSONSE)

		self.assertEqual(dict_returned, {})


	def test_search_results_dict_if_no_results_found_returns_empty_dict_with_list(self):
		json_parser_object = json_parser(json_parser.AuthorObjectType.LIST)
		dict_returned = json_parser_object.search_results_dict(TestJSONParser.VERMOUTH_REPSONSE)

		self.assertEqual(dict_returned, {})


	def test_search_results_dict_empty_dict_returns_empty_dict_with_default_set(self):
		json_parser_object = json_parser()
		dict_returned = json_parser_object.search_results_dict({})

		self.assertEqual(dict_returned, {})


	def test_search_results_dict_empty_dict_returns_empty_dict_with_list(self):
		json_parser_object = json_parser(json_parser.AuthorObjectType.LIST)
		dict_returned = json_parser_object.search_results_dict({})

		self.assertEqual(dict_returned, {})


	def test_search_results_dict_returns_expected_dict_for_agency_object_containing_over_two_results_default_set(self):
		json_parser_object = json_parser()
		with patch.object(json_parser_object, 'agencies_responsible_for_title_and_chapter', return_value = {'ABC', 'EFG', 'HIJ'}):
			dict_returned = json_parser_object.search_results_dict(TestJSONParser.CHOCOLATE_REPSONSE)

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


	def test_search_results_dict_returns_expected_dict_for_agency_object_containing_over_two_results_list(self):
		json_parser_object = json_parser(json_parser.AuthorObjectType.LIST)
		with patch.object(json_parser_object, 'agencies_responsible_for_title_and_chapter', return_value = ['ABC', 'EFG', 'HIJ']):
			dict_returned = json_parser_object.search_results_dict(TestJSONParser.CHOCOLATE_REPSONSE)

		dict_expected = {
		    "result_1": {
		        "Milk <strong>chocolate</strong>.": "(a) Description. (1) Milk <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">\u2026</span>intimately mixing and grinding <strong>chocolate</strong> liquor with one or more of the optional dairy ingredients<span class=\"elipsis\">\u2026</span>(2) Milk <strong>chocolate</strong> contains not less than 10 percent by weight of <strong>chocolate</strong> liquor complying",
		        "authors": ["ABC", "EFG", "HIJ"]
		    },
		    "result_2": {
		        "Sweet <strong>chocolate</strong>.": "(a) Description. (1) Sweet <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">\u2026</span>intimately mixing and grinding <strong>chocolate</strong> liquor with one or more optional nutritive carbohydrate<span class=\"elipsis\">\u2026</span>(2) Sweet <strong>chocolate</strong> contains not less than 15 percent by weight of <strong>chocolate</strong> liquor complying",
		        "authors": ["ABC", "EFG", "HIJ"]
		    },
		    "result_3": {
		        "White <strong>chocolate</strong>.": "(a) Description. (1) White <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">\u2026</span>section. White <strong>chocolate</strong> shall be free of coloring material. (2) White <strong>chocolate</strong> contains not<span class=\"elipsis\">\u2026</span>white <strong>chocolate</strong>, and multiplying the quotient by 100. The finished white <strong>chocolate</strong> contains",
		        "authors": ["ABC", "EFG", "HIJ"]
		    }
		}

		self.assertEqual(dict_returned, dict_expected)


	def test_search_results_dict_handles_exception_with_default_set(self):
		json_parser_object = json_parser()
		with patch.object(json_parser_object, 'search_results_dict', side_effect = Exception('Generic exception')):
			with self.assertRaises(Exception):
					json_parser_object.search_results_dict(TestJSONParser.CHOCOLATE_REPSONSE)


	def test_search_results_dict_handles_exception_with_list(self):
		json_parser_object = json_parser(json_parser.AuthorObjectType.LIST)
		with patch.object(json_parser_object, 'search_results_dict', side_effect = Exception('Generic exception')):
			with self.assertRaises(Exception):
					json_parser_object.search_results_dict(TestJSONParser.CHOCOLATE_REPSONSE)


	def test_search_results_dict_outputs_expected_when_exception_encountered_with_default_set(self):
		json_parser_object = json_parser()
		with patch.object(json_parser_object, 'agencies_responsible_for_title_and_chapter', side_effect = Exception('Generic exception')):
			string_buffer = io.StringIO()

			with redirect_stdout(string_buffer):
				json_parser_object.search_results_dict(TestJSONParser.CHOCOLATE_REPSONSE)

			captured_output = string_buffer.getvalue()

			self.assertEqual(captured_output[0:21], 'Generic error caught:')


	def test_search_results_dict_outputs_expected_when_exception_encountered_with_list(self):
		json_parser_object = json_parser(json_parser.AuthorObjectType.LIST)
		with patch.object(json_parser_object, 'agencies_responsible_for_title_and_chapter', side_effect = Exception('Generic exception')):
			string_buffer = io.StringIO()

			with redirect_stdout(string_buffer):
				json_parser_object.search_results_dict(TestJSONParser.CHOCOLATE_REPSONSE)

			captured_output = string_buffer.getvalue()

			self.assertEqual(captured_output[0:21], 'Generic error caught:')
	# https://www.youtube.com/watch?v=H0WK6nwwxN8
	# search_results_dict tests
	# END: Tests
# END: TestJSONParser Class