import requests
from enum import Enum
import api.api_constants as api_constants
from api.query_modifier import QueryModifier as query_modifier

# START: ApiHandler Class
class ApiHandler:
	# Considering...
	# @abstractmethod

	# Inner class ServiceType provides all possible services.
	class ServiceType(Enum):
		SEARCH = 1
		ADMIN = 2
		VERSIONER = 3 # Don't think I'll ever use this.
	# END: Enums

	# START: Constructor
	# /api/{service}/v1/{search_type}...
	def __init__(self, service: ServiceType):
		self.service = service
	# END: Constructor

	# START: Proposed Methods
	# https://www.youtube.com/watch?v=MHCmE4ABnNs
	# Any real benefit of splitting build and call responsibility? Hm...
	# Maybe will see benefits when building unique url in children.

	# generic call
	# def api_call(query):

	# build get
	# RETURNS URL string?
	# def build_get():

	# END: Proposed Methods
# END: ApiHandler Class