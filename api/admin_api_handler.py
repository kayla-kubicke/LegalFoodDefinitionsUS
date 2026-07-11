import requests
from enum import Enum
import api.api_constants as api_constants
from api.api_handler import ApiHandler as api_handler
from api.query_modifier import QueryModifier as query_modifier

# ADD: Tests!!!

class AdminApiHandler(api_handler):
	# START: Enums
	# .../v1/agencies.json
	# .../v1/corrections.json
	# .../v1/corrections/title/{title}.json #NOTE: Title is an int
	class AdminType(str, Enum):
		AGENCIES = 'agencies.json'
		CORRECTIONS = 'corrections.json'
		# CORRECTIONS_TITLE = ''
	# END: Enums

	# START: Constructor
	def __init__(self, admin_type: AdminType, service: api_handler.ServiceType = api_handler.ServiceType.ADMIN):
		super().__init__(service)
		self.admin_type = admin_type.value
	# END: Constructor

	# START: Methods
	def build_url(self, query):
		return 'dummy value'

	def api_call(self, query):
		return 'dummy value'
	# https://www.youtube.com/watch?v=Vf8ee-gccpc
	# I f'ing love the badlands.
	# (So hot though!)