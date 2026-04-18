# START: imports
from unittest.mock import patch
from api.api_handler import ApiHandler as api_handler
# END: imports

# START: patch(es)
@patch('requests.get')
# END: patch(es)

# The code below is garbage-ish...

# Including argument 'unittest.TestCase' provides convenient testing tools
# (such as assert) to class. Add later, not using it right now.
class TestApiHandler:
	# argument mock_search_term is 'connected' to patch above.
	# How? I don't quite understand the underlying interaction.
	def test_simple_call(mock_search_term):
		# Set values for mock_search_term
		# mock_search_term.return_value.status_code = 202 # Not being used right now.
		mock_search_term.return_value.json.return_value = {'Example key': 'Example value'}

		test_result = api_handler.simple_call(mock_search_term)

		# Add assert statement maybe; right now the method just prints
		# given json to terminal. Would need to capture and see if objects
		# are equal... may not be worth the time. Should just focus on
		# logic restructure and proper testing.


# Test:
# - (?) url is built correctly
# - test all status codes after logic is added
# - (?) json is printed
# - (OR) generic exception is triggered

TestApiHandler.test_simple_call()
# If method is uncommented it prints to terminal:
# '{'Example key': 'Example value'}'
# The exception will never be hit, but shows successful patch.
# Prints as expected; progress.
# https://www.youtube.com/watch?v=LeCI9kww3Dk
