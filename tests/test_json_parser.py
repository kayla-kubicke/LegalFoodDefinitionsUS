# Individual test runner command:
# 'python3 -m unittest tests/test_json_parser.py'

# START: imports
import unittest
from parser.json_parser import JSONParser as json_parser
from api.example_handler import ExampleHandler as example_handler
# END: imports

# START: TestJSONParser Class
class TestJSONParser(unittest.TestCase):
	# START: Tests

	# ADD TESTS: title_and_chapter_found(agency, title, chapter)

	# ADD TESTS: def agencies_responsible_for_title_and_chapter(title, chapter)

	def test_results_found_search_results_dict(self):
		example_response = example_handler.example_response('chocolate')
		dict_returned = json_parser.search_results_dict(example_response)

		comparison_dict = {'<strong>Milk</strong> <strong>chocolate</strong>.': '(a) Description. (1) <strong>Milk</strong> <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">…</span>intimately mixing and grinding <strong>chocolate</strong> liquor with one or more of the optional dairy ingredients<span class=\"elipsis\">…</span>section. (2) <strong>Milk</strong> <strong>chocolate</strong> contains not less than 10 percent by weight of <strong>chocolate</strong> liquor',
		'Skim <strong>milk</strong> <strong>chocolate</strong>.': '(a) Description. Skim <strong>milk</strong> <strong>chocolate</strong> is the food that conforms to the standard of identity<span class=\"elipsis\">…</span>label declaration of ingredients for <strong>milk</strong> <strong>chocolate</strong> in § 163.130, except that: (1) The optional<span class=\"elipsis\">…</span>are limited to skim <strong>milk</strong>, evaporated skim <strong>milk</strong>, concentrated skim <strong>milk</strong>, sweetened condensed',
		'<strong>Milk</strong> <strong>chocolate</strong> and vegetable fat coating.': '(a) Description. <strong>Milk</strong> <strong>chocolate</strong> and vegetable fat coating is the food that conforms to<span class=\"elipsis\">…</span>of ingredients for <strong>milk</strong> <strong>chocolate</strong> in § 163.130 or skim <strong>milk</strong> <strong>chocolate</strong> in § 163.140, except<span class=\"elipsis\">…</span>less than 12 percent by weight of nonfat <strong>milk</strong> solids shall be calculated using only those',
		'Sweet <strong>chocolate</strong>.': '(a) Description. (1) Sweet <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">…</span>intimately mixing and grinding <strong>chocolate</strong> liquor with one or more optional nutritive carbohydrate<span class=\"elipsis\">…</span>(2) Sweet <strong>chocolate</strong> contains not less than 15 percent by weight of <strong>chocolate</strong> liquor complying',
		'White <strong>chocolate</strong>.': '(a) Description. (1) White <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">…</span>section. White <strong>chocolate</strong> shall be free of coloring material. (2) White <strong>chocolate</strong> contains not<span class=\"elipsis\">…</span>white <strong>chocolate</strong>, and multiplying the quotient by 100. The finished white <strong>chocolate</strong> contains',
		}

		self.assertEqual(dict_returned, comparison_dict)

	def test_no_results_found_search_results_dict(self):
		example_response = example_handler.example_response('sourdough')
		dict_returned = json_parser.search_results_dict(example_response)

		self.assertEqual(dict_returned, {})

	def test_results_found_search_results_list(self):
		example_response = example_handler.example_response('chocolate')
		array_returned = json_parser.search_results_list(example_response)

		comparison_array = ['<strong>Milk</strong> <strong>chocolate</strong>.',
		'Skim <strong>milk</strong> <strong>chocolate</strong>.',
		'<strong>Milk</strong> <strong>chocolate</strong> and vegetable fat coating.',
		'Sweet <strong>chocolate</strong>.',
		'White <strong>chocolate</strong>.']

		self.assertEqual(array_returned, comparison_array)

	def test_no_results_found_search_results_list(self):
		example_response = example_handler.example_response('sourdough')
		array_returned = json_parser.search_results_list(example_response)

		self.assertEqual(array_returned, [])
	# END: Tests
# END: TestJSONParser Class