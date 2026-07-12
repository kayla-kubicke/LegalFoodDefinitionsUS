# import requests
from enum import Enum
import api.api_constants as api_constants
from api.api_handler import ApiHandler as api_handler
# from api.query_modifier import QueryModifier as query_modifier

class SearchApiHandler(api_handler):
	# START: Enums
	class SearchType(str, Enum):
		RESULTS = 'results'
		COUNT = 'count'
		SUMMARY = 'summary'
		COUNTS = 'counts'
		COUNTS_DATES = 'counts/daily'
		COUNTS_TITLE = 'counts/titles'
		COUNTS_HIERARCHY = 'counts/hierarchy'
		SUGGESTIONS = 'suggestions'
	# END: Enums

	# START: Constructor
	def __init__(self, search_type: SearchType, service: api_handler.ServiceType = api_handler.ServiceType.SEARCH):
		super().__init__(service)
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

	# RETURNS URL string
	def build_url(self, query):
		url = f'{api_constants.ECFR}/api/{self.service}/v1/{self.search_type}?query={query}&{SearchApiHandler.format_agency_parameter(api_constants.SLUG_ARRAY)}{api_constants.PER_PAGE}3&{api_constants.PAGE}1&{api_constants.ORDER}relevance&{api_constants.PAGINATE_BY}results'

		return url

	# A search results call to api
	# RETURNS
	# Successful: dict object
	# Unsuccessful:
		# If response is returned but status code != 200:
		# If an error is encountered during request:
	def api_call(self, query):
		return super().api_call(query)