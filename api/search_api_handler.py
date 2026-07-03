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
	class SearchType(str, Enum):
		RESULTS = 'results'
		COUNT = 'count'
		SUMMARY = 'summary'
		COUNTS = 'counts' # Maybe just make extra enums? Not scalable, but doubt API will grow too much...
		SUGGESTIONS = 'suggestions'

	# SEARCH_TYPE_DICT = {

	# }

	# START: Constructor
	def __init__(self, search_type: SearchType, service: api_handler.ServiceType = api_handler.ServiceType.SEARCH):
		# self.service = service.value # Type check in parent? Or just let python be python?
		super().__init__(service) # Better?
		self.search_type = search_type.value
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

	def build_url(self, query):
		# url = '''api_constants.ECFR + api_constants.SEARCH + api_constants.QUERY + query + '&' +
		# 		SearchApiHandler.format_agency_parameter(api_constants.SLUG_ARRAY) + api_constants.PER_PAGE + '3' +
		# 		'&' + api_constants.PAGE + '1' + '&' + api_constants.ORDER + 'relevance' +
		# 		'&' + api_constants.PAGINATE_BY + 'results'\\'''

		# ADD: Dummy url test

		url = f'''api_constants.ECFR + '/api/' + {self.service} + '/v1/' + {self.search_type} + query + '&' +
			SearchApiHandler.format_agency_parameter(api_constants.SLUG_ARRAY) + api_constants.PER_PAGE + '3' +
			'&' + api_constants.PAGE + '1' + '&' + api_constants.ORDER + 'relevance' +
			'&' + api_constants.PAGINATE_BY + 'results'\\'''

		return url
	# <3 <3 <3
	# https://www.youtube.com/watch?v=RoaOFFCSegc

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