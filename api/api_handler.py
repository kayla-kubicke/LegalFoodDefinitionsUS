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
	PAGINATE_BY = 'paginate_by='
	# END: Page parameters
	# END: Constants

	# START: Methods
	# A simple call to api
	def simple_call(query):
		try:
			# Object type: requests.models.Repsonse
			simpleRequest = requests.get(f'{ApiHandler.ECFR}{ApiHandler.SEARCH}{ApiHandler.QUERY}' + query + '&'
				+ f'{ApiHandler.PER_PAGE}' + '3' + '&' + f'{ApiHandler.PAGE}' + '1' + '&'
				+ f'{ApiHandler.ORDER}' + 'relevance' + '&' + f'{ApiHandler.PAGINATE_BY}' + 'results')

			if simpleRequest.status_code == 200:
				# Object type: dict
				return simpleRequest.json()
			elif type(simpleRequest.status_code) == int:
				raise RuntimeError(f'Status code: {simpleRequest.status_code} returned. Process stopped.')

		# Generic exception raised if any error is encountered during request.
		except requests.exceptions.RequestException as error:
			print(f'Generic exception: {error}')
	# END: Methods
# END: ApiHandler Class
