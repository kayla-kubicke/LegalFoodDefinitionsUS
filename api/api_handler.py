import requests
from enum import Enum
from abc import ABC, abstractmethod
import api.api_constants as api_constants
# from api.query_modifier import QueryModifier as query_modifier

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
	@abstractmethod
	def build_url(self):
		...

	# RETURNS
	# Successful: dict object
	# Unsuccessful:
		# If response is returned but status code != 200:
		# If an error is encountered during request:

	# versioner uses date and title
	@abstractmethod
	def api_call(self):
		...
	# END: Methods
# END: ApiHandler Class