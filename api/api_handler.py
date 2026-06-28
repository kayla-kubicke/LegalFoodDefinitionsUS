# import requests
from abc import ABC, abstractmethod
from enum import Enum
# import api.api_constants as api_constants
# from api.query_modifier import QueryModifier as query_modifier

# START: ApiHandler Class
class ApiHandler(ABC):
	# Inner class ServiceType provides all possible services.
		# Admin Service: /api/admin/v1/...
		# Search Service: /api/search/v1/...
		# Versioner Service: /api/versioner/v1/...
		#
		# Could use StrEnum or this supposed convention?
	# class ServiceType(Enum):
	# 	SEARCH = 1
	# 	ADMIN = 2
	# 	VERSIONER = 3
	# END: Enums

	class ServiceType(str, Enum):
		SEARCH = 'search'
		ADMIN = 'admin'
		VERSIONER = 'versioner'

	# SERVICE_TYPE_DICT = {

	# }

	# START: Constructor
	# /api/{service}/v1/{search_type}...
	def __init__(self, service: ServiceType):
		self.service = service
	# END: Constructor

	# START: Proposed Methods
	@abstractmethod
	def api_call(self, query):
		...

	# I'll just keep it for now.
	# RETURNS URL string
	@abstractmethod
	def build_url(self):
		...
	# END: Proposed Methods
# END: ApiHandler Class