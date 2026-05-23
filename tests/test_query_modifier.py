# Individual test runner command:
# 'python3 -m unittest tests/test_query_modifier.py'

# START: imports
import unittest
from unittest.mock import patch
from api.query_modifier import QueryModifier as query_modifier
# END: imports

# START: TestQueryModifer Class
class TestQueryModifer(unittest.TestCase):
	# pad_query tests
	def test_pad_query(self):
		string_returned = query_modifier.pad_query('milk chocolate')

		self.assertEqual(string_returned, 'milk%20chocolate')
	# pad_query tests
# END: TestQueryModifer Class