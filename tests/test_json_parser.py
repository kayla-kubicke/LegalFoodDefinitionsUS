# Test runner command:
# 'python3 -m unittest tests/test_json_parser.py'

# START: imports & patch(es)
import unittest
from parser.json_parser import JSONParser as json_parser
# END: imports & patch(es)

# Not including tests for example_reponse() or array_custom_print(array)
# because both methods will be moved into classes with distinct responsibilities.

# START: TestJSONParser Class
# https://www.youtube.com/watch?v=VqQmgHcIHN0
class TestJSONParser(unittest.TestCase):
	# START: Tests
	def test_ugly_list(self):
		# (!) NOTE: Currently coupled with example_response()
		# REMOVE
		# Update after example_response() is given new home.
		example_response = json_parser.example_response()
		# REMOVE
		array_returned = json_parser.ugly_list(example_response)

		comparison_array = ['<strong>Milk</strong> <strong>chocolate</strong>.',
		'Skim <strong>milk</strong> <strong>chocolate</strong>.',
		'<strong>Milk</strong> <strong>chocolate</strong> and vegetable fat coating.',
		'Sweet <strong>chocolate</strong>.',
		'White <strong>chocolate</strong>.']

		# Fragile, but wanted to set up basic testing.
		self.assertEqual(array_returned, comparison_array)
	# END: Tests
# https://www.youtube.com/watch?v=YwIssvTKjug
# END: TestJSONParser Class