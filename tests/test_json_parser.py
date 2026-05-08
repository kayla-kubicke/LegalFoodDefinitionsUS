# Individual test runner command:
# 'python3 -m unittest tests/test_json_parser.py'

# START: imports
import unittest
from parser.json_parser import JSONParser as json_parser
from api.example_handler import ExampleHandler as example_handler
# END: imports

# START: TestJSONParser Class
class TestJSONParser(unittest.TestCase):
	# START: Constants
	CHOCOLATE_REPSONSE = example_handler.example_response('example_requests', 'chocolate')
	VERMOUTH_REPSONSE = example_handler.example_response('example_requests', 'vermouth')
	AGENCIES_DATA = example_handler.example_response('agency_data', 'agencies')
	# END: Constants

	# START: Tests
	def test_title_and_chapter_found_returns_true_if_title_and_chapter_found(self):
		agency = TestJSONParser.AGENCIES_DATA['agencies'][0]['children'][0]
		bool_returned = json_parser.title_and_chapter_found_in_agency_json(agency, 7, 'I')

		self.assertEqual(bool_returned, True)


	def test_title_and_chapter_found_returns_false_if_title_and_chapter_not_found(self):
		agency = TestJSONParser.AGENCIES_DATA['agencies'][0]['children'][0]
		bool_returned = json_parser.title_and_chapter_found_in_agency_json(agency, 7, 'V')

		self.assertEqual(bool_returned, False)


	def test_agencies_responsible_for_title_and_chapter_returns_array_expected_if_match_found(self):
		array_returned = json_parser.agencies_responsible_for_title_and_chapter(21, 'I')
		array_expected = ['FDA']

		self.assertEqual(array_returned, array_expected)


	def test_agencies_responsible_for_title_and_chapter_returns_empty_array_if_no_matches_are_found(self):
		array_returned = json_parser.agencies_responsible_for_title_and_chapter(450, 'I')

		self.assertEqual(array_returned, ['unknown'])


	def test_results_found_search_results_dict(self):
		dict_returned = json_parser.search_results_dict(TestJSONParser.CHOCOLATE_REPSONSE)

		expected_dict = {
			'result_1': {
					'Milk <strong>chocolate</strong>.': '(a) Description. (1) Milk <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class="elipsis">…</span>intimately mixing and grinding <strong>chocolate</strong> liquor with one or more of the optional dairy ingredients<span class="elipsis">…</span>(2) Milk <strong>chocolate</strong> contains not less than 10 percent by weight of <strong>chocolate</strong> liquor complying',
					'authors': 'FDA'
				},
			'result_2': {
					'Sweet <strong>chocolate</strong>.': '(a) Description. (1) Sweet <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class="elipsis">…</span>intimately mixing and grinding <strong>chocolate</strong> liquor with one or more optional nutritive carbohydrate<span class="elipsis">…</span>(2) Sweet <strong>chocolate</strong> contains not less than 15 percent by weight of <strong>chocolate</strong> liquor complying',
					'authors': 'FDA'
				},
			'result_3': {
					'White <strong>chocolate</strong>.': '(a) Description. (1) White <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class="elipsis">…</span>section. White <strong>chocolate</strong> shall be free of coloring material. (2) White <strong>chocolate</strong> contains not<span class="elipsis">…</span>white <strong>chocolate</strong>, and multiplying the quotient by 100. The finished white <strong>chocolate</strong> contains',
					'authors': 'FDA'
				}
		}

		self.assertEqual(dict_returned, expected_dict)


	def test_no_results_found_search_results_dict(self):
		# dict_returned = json_parser.search_results_dict(TestJSONParser.VERMOUTH_REPSONSE)
		dict_returned = json_parser.search_results_dict({})


		self.assertEqual(dict_returned, {})


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