from unittest.mock import patch
from api.api_handler import ApiHandler as api_handler

# START: patch(es)
# https://www.youtube.com/watch?v=3T7C1Sdl-tA
@patch('requests.get') # Should it just be 'requests'?
# END: patch(es)

# I've never worked with unittest; going to be a learning curve.
# The code below is garbage...

# class TestApiHandler:
	# search_term = 'chocolate'
	# # Method needs a different parameter, but what is parameter?
	# def test_simple_call(search_term):
	# 	# ADD: 'set' patch?

	# 	api_handler.simple_call(search_term)


# Test:
# - url is built correctly
# - json is printed
# - (OR) generic exception is triggered

# TestApiHandler.test_simple_call()
# If method is uncommented it prints to terminal:
# '<MagicMock name='get().json()' id='4478706960'>'
# Definitely not right... :)
