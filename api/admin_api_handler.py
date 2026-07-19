import requests
from enum import Enum
import api.api_constants as api_constants
from api.api_handler import ApiHandler as api_handler
from api.query_modifier import QueryModifier as query_modifier

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
	# Untested.
	# title will only be used for CORRECTIONS_TITLE, if needed.
	# RETURNS URL string
	def build_url(self, title = ''):
		# For AGENCIES and CORRECTIONS:
		if (self.admin_type == 'agencies' or self.admin_type == 'corrections') and self.admin_type != 'corrections/title/':
			# Spot check
			return f'{api_constants.ECFR}/api/{self.service}/v1/{self.admin_type}.json'

		# For CORRECTIONS_TITLE: Includes {title}
		if isinstance(title, int):
			title = str(title)

		if self.admin_type == 'corrections/title/' and title == '':
			raise ValueError('title param required for ...corrections/title/... url')

		return f'{api_constants.ECFR}/api/{self.service}/v1/{self.admin_type}{title}.json'

	# A search results call to api
	# RETURNS
	# Successful: dict object
	# Unsuccessful:
		# If response is returned but status code != 200:
		# If an error is encountered during request:
	def api_call(self, query):
		return super().api_call(query)



	# I need to prioritize whiteboard/data structure stuff.
	# Consequetly, this project will be placed on the back burner.

	#
	# Use the following as needed.

	# When the thoughts of your mistakes overwhelm you:
		# https://www.youtube.com/watch?v=IP9TaFDe7qk

	# When you feel like haunting your own home:
		# https://www.youtube.com/watch?v=u9FguM9aAM8

	# When the vapid hellscape begins to consume you:
		# https://www.youtube.com/watch?v=qOM107PIxV8

	# When you're accidentally the villian:
		# https://www.youtube.com/watch?v=wlI_BgVvtQY

	# When you start to think way too much about the Stranger Situation:
		# https://www.youtube.com/watch?v=Hm3cf3jsWNw