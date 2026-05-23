import requests

# START: ApiHandler Class
class ApiHandler:
	# START: Constants
	ECFR = 'https://www.ecfr.gov'
	SEARCH = '/api/search/v1/results?'
	QUERY = 'query='
	# SPACE = %20 # Move to query_builder later.

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
			return_string = f'{return_string}' + f'{param}' + f'{slug}' + '&'

		return return_string

	# A search results call to api
	# RETURNS
	# Successful: dict object
	# Unsuccessful:
		# If response is returned but status code != 200:
		# If an error is encountered during request:
	def search_results_call(query):
		try:
			# ADD: Send query to StringModifier
			# Forgot to fix this after I realized the formatting was redundant.
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

# print(ApiHandler.search_results_call('chocolate'))