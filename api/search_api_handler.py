# import requests
# from enum import Enum
# import api.api_constants as api_constants
# from api.query_modifier import QueryModifier as query_modifier

# (!) Update methods.
# class SearchApiHandler(ApiHandler):
	# START: Enum
	# class SearchType(Enum):
		# RESULTS = 1
		# COUNT = 2
		# SUMMARY = 3
		# COUNTS = 4 # Requires another url option
		# SUGGESTIONS = 5
	# END: Enum

	# START: Constructor
	# def __init__(self, service: ServiceType, ):
		# super().__init__(self, service: ServiceType)
		# 
	# END: Constructor

	# # START: Methods
	# # Move to SearchResultsApiHandler
	# # RETURNS formated agency slug parameter string
	# def format_agency_parameter(slug_array):
	# 	return_string = ''
	# 	param = 'agency_slugs%5B%5D='
	# 	for slug in slug_array:
	# 		return_string = return_string + param + slug + '&'

	# 	return return_string

	# # A search results call to api
	# # RETURNS
	# # Successful: dict object
	# # Unsuccessful:
	# 	# If response is returned but status code != 200:
	# 	# If an error is encountered during request:
	# def search_results_call(query):
	# 	try:
	# 		query = query_modifier.pad_query(query)

	# 		searchResultsResponse = requests.get(api_constants.ECFR + api_constants.SEARCH + api_constants.QUERY + query + '&' +
	# 			ApiHandler.format_agency_parameter(api_constants.SLUG_ARRAY) + api_constants.PER_PAGE + '3' +
	# 			'&' + api_constants.PAGE + '1' + '&' + api_constants.ORDER + 'relevance' +
	# 			'&' + api_constants.PAGINATE_BY + 'results')

	# 		if searchResultsResponse.status_code == 200:
	# 			return searchResultsResponse.json() # Object type: dict
	# 		else:
	# 			print(f'Status code: {searchResultsResponse.status_code} returned. Process stopped.')
	# 			return

	# 	except requests.exceptions.RequestException as error:
	# 		print(f'requests exception caught: {error}')
	# 	except Exception as error:
	# 		print(f'Generic exception caught: {error}')