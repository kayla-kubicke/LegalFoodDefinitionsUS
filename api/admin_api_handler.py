import requests
from enum import Enum
import api.api_constants as api_constants
from api.api_handler import ApiHandler as api_handler

class AdminApiHandler(api_handler):
	# START: Enums
	# .../v1/agencies.json
	# .../v1/corrections.json
	# .../v1/corrections/title/{title}.json # NOTE: title is an int
	class AdminType(str, Enum):
		AGENCIES = 'agencies'
		CORRECTIONS = 'corrections'
		CORRECTIONS_TITLE = 'corrections/title/'
	# END: Enums

	# START: Constructor
	def __init__(self, admin_type: AdminType, service: api_handler.ServiceType = api_handler.ServiceType.ADMIN):
		super().__init__(service)
		self.admin_type = admin_type.value
	# END: Constructor

	# START: Methods
	# title will only be used for CORRECTIONS_TITLE, if needed.
	# RETURNS URL string
	def build_url(self, title = ''):# -> str:
		# For AGENCIES and CORRECTIONS:
		if (self.admin_type == 'agencies' or self.admin_type == 'corrections') and self.admin_type != 'corrections/title/':
			return f'{api_constants.ECFR}/api/{self.service}/v1/{self.admin_type}.json'

		# For CORRECTIONS_TITLE: Includes {title}
		# https://www.youtube.com/watch?v=Pa-L5dwDGJ4
		# All logic below needs to be refined...
		if isinstance(title, int):
			title = str(title)
		# else:
			# raise

		if self.admin_type == 'corrections/title/' and title == '':
			raise ValueError('title param required for .../corrections/title/... url')

		return f'{api_constants.ECFR}/api/{self.service}/v1/{self.admin_type}{title}.json'

	# A search results call to api
	# RETURNS
	# Successful: dict object
	# Unsuccessful:
		# If response is returned but status code != 200:
		# If an error is encountered during request:
	def api_call(self, title = ''):
		# return super().api_call(query)
		try:
			searchResultsResponse = requests.get(self.build_url(title))

			if searchResultsResponse.status_code == 200:
				return searchResultsResponse.json() # Object type: dict
			else:
				print(f'Status code: {searchResultsResponse.status_code} returned. Process stopped.')
				return

		except requests.exceptions.RequestException as error:
			print(f'requests exception caught: {error}')
		except Exception as error:
			print(f'Generic exception caught: {error}')