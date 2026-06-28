import requests
from enum import Enum
import api.api_constants as api_constants
from api.api_handler import ApiHandler as api_handler
from api.query_modifier import QueryModifier as query_modifier

class SearchApiHandler(api_handler):
	# START: Enum
		# Search Results: '.../results'
		# Result Count: '.../count' # NOTE: Different than counts
		# Summary Details: '...summary'
		#
		# Count by Dates: '.../counts/daily'
		# Count by Title: '.../counts/titles'
		# Count by Hierarchy: '.../counts/hierarchy'
		#
		# Suggestions: '.../suggestions'
		#
		# Best way to deal with this? Just another dict?
	class SearchType(Enum):
		RESULTS = 1
		COUNT = 2
		SUMMARY = 3
		COUNTS = 4 # Requires another url option
		SUGGESTIONS = 5
	# END: Enum

	# START: Constructor
	# UPDATE: service needs default after (?) string added or?
	def __init__(self, service: api_handler.ServiceType, search_type: SearchType):
		# Can I move the params around so I can make a service default?
		self.service = self.ServiceType.SEARCH
		self.search_type = search_type
	# END: Constructor

	# START: Methods
	# Move to SearchResultsApiHandler
	# RETURNS formated agency slug parameter string
	def format_agency_parameter(slug_array):
		return_string = ''
		param = 'agency_slugs%5B%5D='
		for slug in slug_array:
			return_string = return_string + param + slug + '&'

		return return_string

	# Best way to set params given enum/url situation?
	def build_url(self, query):
		url = '''api_constants.ECFR + api_constants.SEARCH + api_constants.QUERY + query + '&' +
				SearchApiHandler.format_agency_parameter(api_constants.SLUG_ARRAY) + api_constants.PER_PAGE + '3' +
				'&' + api_constants.PAGE + '1' + '&' + api_constants.ORDER + 'relevance' +
				'&' + api_constants.PAGINATE_BY + 'results'\\'''

		return url

	# A search results call to api
	# RETURNS
	# Successful: dict object
	# Unsuccessful:
		# If response is returned but status code != 200:
		# If an error is encountered during request:
	def api_call(self, query):
		try:
			query = query_modifier.pad_query(query)

			searchResultsResponse = requests.get(self.build_url(query))

			if searchResultsResponse.status_code == 200:
				return searchResultsResponse.json() # Object type: dict
			else:
				print(f'Status code: {searchResultsResponse.status_code} returned. Process stopped.')
				return

		except requests.exceptions.RequestException as error:
			print(f'requests exception caught: {error}')
		except Exception as error:
			print(f'Generic exception caught: {error}')