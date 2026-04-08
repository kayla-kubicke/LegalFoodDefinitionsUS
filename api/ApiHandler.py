# TO DO: Add requests source code... eventually
# https://requests.readthedocs.io/en/latest/user/install/#install

# ADD: peudeocode/general class organization
# Request docs: https://requests.readthedocs.io/en/latest/

# Reminder...
# Activate the environment 
# source .venv/bin/activate

import requests

# https://www.youtube.com/watch?v=-Wtj59opWKg
# START: ApiHandler Class
class ApiHandler:
	# START: Constants
	ECFR = 'https://www.ecfr.gov'
	SECTION = '/api/versioner/v1/versions/title-'
	# END: Constants

	# START: Methods
	# A simple test call to api
	def simple_call():
		simpleRequest = requests.get(f'{ApiHandler.ECFR}{ApiHandler.SECTION}' + '21.json')
		# Just prints json blob to terminal
		print(simpleRequest.json())
	# END: Methods
# END: ApiHandler Class

ApiHandler.simple_call()