# Ugh, what a mess.
# ADD: agency_slugs[]; agencies listed in assets/example_requests/agencies.json
	# Kept the following agencies for agency_slugs[]:
		# USDA and children (REMOVE unnecessary children?)
		# FDA
		# EPA not super useful but touchs pesticide info
		# HHS for child FDA (REMOVE unnecessary children)
		# DOI for child FWS (REMOVE unnecessary children)
		# DOJ for child ATF (REMOVE unnecessary children)
		# MMC
# (?) ADD: Labeling (legal, non-binding guidance, etc)
# (?) ADD: Call for most recent version of chapters used; extract most recent
# dates and fill data parameters.
# (?) ADD: Date updater

import requests

# START: ApiHandler Class
class ApiHandler:
	# START: Constants
	ECFR = 'https://www.ecfr.gov'
	SEARCH = '/api/search/v1/results?'
	QUERY = 'query='
	# SPACE = %20 # Move to query_builder later.

	# Agency slug list
	# (?) ADD: Custom slug selection
	# UPDATE: Custom slug and chapter connection to help determine label
	# https://www.youtube.com/watch?v=iKJI5XGZh9o
	USDA = 'agriculture-department' # Legal and non-binding guidance
	EPA = 'environmental-protection-agency' # Pesticide-related results
	FDA = 'food-and-drug-administration' # Legal and (?) non-binding guidance
	FWS = 'fish-and-wildlife-service' # Wild foods definitions and (?) non-binding guidance
	ATF ='alcohol-tobacco-firearms-and-explosives-bureau' # Booze
	MMC = 'marine-mammal-commission' # Wild foods definitions and (?) non-binding guidance
	slug_array = [f'{USDA}', f'{FDA}', f'{EPA}', f'{FWS}', f'{ATF}', f'{MMC}']

	# START: Date parameters
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
	# Confirm by date returns most recent first.
	# NOTE:'date' requires one of the last_modified_* options.
	PAGINATE_BY = 'paginate_by='
	# END: Page parameters
	# END: Constants

	# START: Methods
	# A simple call to api
	# RETURNS
	# Successful: dict object
	# Unsuccessful:
		# If response is returned but status code != 200: raises RuntimeError
		# If an error is encountered during request: raises RequestException
	def simple_call(query):
		try:
			# slug curl:
			# curl -X GET "https://www.ecfr.gov/api/search/v1/results?query=chocolate&
			# agency_slugs%5B%5D=agriculture-department&agency_slugs%5B%5D=environmental-protection-agency&agency_slugs%5B%5D=food-and-drug-administration&agency_slugs%5B%5D=fish-and-wildlife-service&agency_slugs%5B%5D=alcohol-tobacco-firearms-and-explosives-bureau&agency_slugs%5B%5D=marine-mammal-commission
			# &per_page=15&page=1&order=relevance&paginate_by=results" -H "accept: application/json"
			# Object type: requests.models.Repsonse
			simpleResponse = requests.get(f'{ApiHandler.ECFR}{ApiHandler.SEARCH}{ApiHandler.QUERY}' + query + '&'
				+ f'{ApiHandler.PER_PAGE}' + '3' + '&' + f'{ApiHandler.PAGE}' + '1' + '&'
				+ f'{ApiHandler.ORDER}' + 'relevance' + '&' + f'{ApiHandler.PAGINATE_BY}' + 'results')

			if simpleResponse.status_code == 200:
				# Object type: dict
				return simpleResponse.json()
			elif type(simpleResponse.status_code) == int:
				raise RuntimeError(f'Status code: {simpleResponse.status_code} returned. Process stopped.')

		# Generic exception raised if any error is encountered during request.
		except requests.exceptions.RequestException as error:
			print(f'Generic exception caught: {error}')
	# END: Methods
# END: ApiHandler Class

# print(ApiHandler.simple_call('chocolate'))
# print('\n'.join(map(str, ApiHandler.slug_array)))