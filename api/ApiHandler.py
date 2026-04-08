# TO DO: Add basic testing and error catch
# TO DO: Add requests source code... eventually
# https://requests.readthedocs.io/en/latest/user/install/#install

# ADD: peudeocode/general class organization
# Request docs: https://requests.readthedocs.io/en/latest/

# Reminder...
# Activate the environment 
# source .venv/bin/activate

import requests

# START: ApiHandler Class
class ApiHandler:
	# START: Constants
	ECFR = 'https://www.ecfr.gov'
	SEARCH = '/api/search/v1/results?'
	QUERY = 'query='
	# SPACE = %20 # I'm going to need a massive string and results handler...yikes.

	# NOTE: May not need all parameters; listing to know what I have.

	# https://www.youtube.com/watch?v=_QAIX8410zs
	# START: Date parameters
	# Way to simply get most updated version? Hm...
	# access to and how I can play with search.
	# DATE = 'date='
	# LAST_MOD_AFTER = 'last_modified_after='
	# LAST_MOD_ON_OR_AFTER = 'last_modified_on_or_after='
	# LAST_MOD_BEFORE = 'last_modified_before='
	# LAST_MOD_ON_OR_BEFORE = 'last_modified_on_or_before='
	# END: Date parameters

	# START: Page parameters
	PER_PAGE = 'per_page='
	PAGE = 'page='
	ORDER = 'order='
	PAGINATE_BY = 'paginate_by='
	# END: Page parameters
	# END: Constants

	# START: Methods
	# A simple-ish test call to api
	def simple_call(query):
		simpleRequest = requests.get(f'{ApiHandler.ECFR}{ApiHandler.SEARCH}{ApiHandler.QUERY}' + query + '&'
			+ f'{ApiHandler.PER_PAGE}' + '3' + '&' + f'{ApiHandler.PAGE}' + '1' + '&'
			+ f'{ApiHandler.ORDER}' + 'relevance' + '&' + f'{ApiHandler.PAGINATE_BY}' + 'results')
		# print(f'{ApiHandler.ECFR}{ApiHandler.SEARCH}{ApiHandler.QUERY}' + query + '&'
		# 	+ f'{ApiHandler.PER_PAGE}' + '3' + '&' + f'{ApiHandler.PAGE}' + '1' + '&'
		# 	+ f'{ApiHandler.ORDER}' + 'relevance' + '&' + f'{ApiHandler.PAGINATE_BY}' + 'results')
		# Just prints json blob to terminal
		print(simpleRequest.json())
	# END: Methods
# END: ApiHandler Class

ApiHandler.simple_call('chocolate')