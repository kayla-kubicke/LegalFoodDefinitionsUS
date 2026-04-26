# Next step is to reduce results to most recent definitions.
import requests

# START: ApiHandler Class
class ApiHandler:
	# START: Constants
	ECFR = 'https://www.ecfr.gov'
	SEARCH = '/api/search/v1/results?'
	QUERY = 'query='
	# SPACE = %20

	# START: Date parameters
	# DATE = 'date='
	# LAST_MOD_AFTER = 'last_modified_after='
	# LAST_MOD_ON_OR_AFTER = 'last_modified_on_or_after='
	# LAST_MOD_BEFORE = 'last_modified_before='
	# LAST_MOD_ON_OR_BEFORE = 'last_modified_on_or_before='
	# END: Date parameters

	# START: Page parameters
	PER_PAGE = 'per_page='
	PAGE = 'page='
	ORDER = 'order='
	# Confirm by date returns most recent first.
	# NOTE:'date' requires one of the last_modified_* options.
	PAGINATE_BY = 'paginate_by='
	# END: Page parameters
	# END: Constants

	# START: Methods
	# A simple call to api
	# RETURNS
	# Successful: dict object
	# Unsuccessful:
		# If response is returned but status code != 200: raises RuntimeError
		# If an error is encountered during request: raises RequestException
	def simple_call(query):
		try:
			# Object type: requests.models.Repsonse
			simpleResponse = requests.get(f'{ApiHandler.ECFR}{ApiHandler.SEARCH}{ApiHandler.QUERY}' + query + '&'
				+ f'{ApiHandler.PER_PAGE}' + '3' + '&' + f'{ApiHandler.PAGE}' + '1' + '&'
				+ f'{ApiHandler.ORDER}' + 'relevance' + '&' + f'{ApiHandler.PAGINATE_BY}' + 'results')

			if simpleResponse.status_code == 200:
				# Object type: dict
				return simpleResponse.json()
			elif type(simpleResponse.status_code) == int:
				raise RuntimeError(f'Status code: {simpleResponse.status_code} returned. Process stopped.')

		# Generic exception raised if any error is encountered during request.
		except requests.exceptions.RequestException as error:
			print(f'Generic exception caught: {error}')
	# END: Methods
# END: ApiHandler Class