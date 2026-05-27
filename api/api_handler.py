import requests
# from enum import Enum
import api.api_constants as api_constants
from api.query_modifier import QueryModifier as query_modifier

# START: ApiHandler Class
class ApiHandler:
	# https://docs.python.org/3/tutorial/classes.html#inheritance
	#
	# Children:
	# (search) search_results
	# (admin) correction - includes revisions, so I can grab most recent date data
	# count - if a I build a spliter, can call to get count for split/combo query
		# so user can select split or combo
	# Basic agency call? Do I need this?

	# START: Enums
	# service Enum
		# admin, search, versioner
	# END: Enums

	# START: Constructor
	# def __init__(self, service):
		# /api/{service}/v1/{search_type}...
		#
		# self.service = service
	# END: Constructor

	# START: Proposed Methods
	# generic call
	# build get
	# That's it?
	# https://www.youtube.com/watch?v=URQ6E5gGNCI
	# END: Proposed Methods

	# Migrate this stuff later.
	# START: Methods
	# Move to SearchResultsApiHandler
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

			searchResultsResponse = requests.get(api_constants.ECFR + api_constants.SEARCH + api_constants.QUERY + query + '&' +
				ApiHandler.format_agency_parameter(api_constants.SLUG_ARRAY) + api_constants.PER_PAGE + '3' +
				'&' + api_constants.PAGE + '1' + '&' + api_constants.ORDER + 'relevance' +
				'&' + api_constants.PAGINATE_BY + 'results')

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