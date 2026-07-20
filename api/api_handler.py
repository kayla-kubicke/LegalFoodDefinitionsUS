import requests
from enum import Enum
from abc import ABC, abstractmethod
import api.api_constants as api_constants
from api.query_modifier import QueryModifier as query_modifier

# START: ApiHandler Class
class ApiHandler(ABC):
	# START: Enums
	# Inner class ServiceType provides all possible services
	class ServiceType(str, Enum):
		SEARCH = 'search'
		ADMIN = 'admin'
		VERSIONER = 'versioner'
	# END: Enums

	# START: Constructor
	# /api/{service}/v1/{search_type}...
	def __init__(self, service: ServiceType):
		self.service = service.value
	# END: Constructor

	# START: Methods
	def build_url(self):
		...

	# RETURNS
	# Successful: dict object
	# Unsuccessful:
		# If response is returned but status code != 200:
		# If an error is encountered during request:

	# Ugh... actually, I should remove the query param... remove super and query param, add
	# placeholder.

	# search uses a query
	# admin uses a title
	# versioner uses date and title
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
	# END: Methods
# END: ApiHandler Class