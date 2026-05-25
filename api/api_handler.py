import requests
from api.query_modifier import QueryModifier as query_modifier

# START: ApiHandler Class
class ApiHandler:
	# Maybe make this a parent class and the children calls?
	# https://docs.python.org/3/tutorial/classes.html#inheritance
	# Hm... yeah, I think that's the next step.
	# Just make it as flexible as possible.
	#
	# Children:
	# search_results
	# correction - includes revisions, so I can grab most recent date data
	# count - if a I build a spliter, can call to get count for split/combo query
		# so user can select split or combo
	# Basic agency call? Do I need this?

	# START: Constants
	ECFR = 'https://www.ecfr.gov'
	SEARCH = '/api/search/v1/results?'
	QUERY = 'query='

	# Agency slug list
	USDA = 'agriculture-department' # Legal and non-binding guidance
	EPA = 'environmental-protection-agency' # Pesticide-related results
	FDA = 'food-and-drug-administration' # Legal and non-binding guidance
	FWS = 'fish-and-wildlife-service' # Wild foods definitions and non-binding guidance
	ATF ='alcohol-tobacco-firearms-and-explosives-bureau' # Booze
	MMC = 'marine-mammal-commission' # Wild foods definitions and non-binding guidance
	slug_array = [USDA, FDA, EPA, FWS, ATF, MMC]

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
	# RETURNS formated agency slug parameter string
	def format_agency_parameter(slug_array):
		return_string = ''
		param = 'agency_slugs%5B%5D='
		for slug in slug_array:
			return_string = return_string + param + slug + '&'

		return return_string

	# A search results call to api
	# RETURNS
	# Successful: dict object
	# Unsuccessful:
		# If response is returned but status code != 200:
		# If an error is encountered during request:
	def search_results_call(query):
		try:
			query = query_modifier.pad_query(query)

			searchResultsResponse = requests.get(ApiHandler.ECFR + ApiHandler.SEARCH + ApiHandler.QUERY + query + '&' +
				ApiHandler.format_agency_parameter(ApiHandler.slug_array) + ApiHandler.PER_PAGE + '3' +
				'&' + ApiHandler.PAGE + '1' + '&' + ApiHandler.ORDER + 'relevance' +
				'&' + ApiHandler.PAGINATE_BY + 'results')

			if searchResultsResponse.status_code == 200:
				return searchResultsResponse.json() # Object type: dict
			else:
				print(f'Status code: {searchResultsResponse.status_code} returned. Process stopped.')
				return

		except requests.exceptions.RequestException as error:
			print(f'requests exception caught: {error}')
		except Exception as error:
			print(f'Generic exception caught: {error}')
	# END: Methods
# END: ApiHandler Class