import json
from api.api_handler import ApiHandler as api_handler

# START: JSONParser Class
class JSONParser:
	# START: Methods
	# Generates a static response dict object to avoid
	# unnecessary api calls.
	# RETURNS canned response dict object
	def example_response(query):
		try:
			with open(f'assets/example_requests/{query}.json', 'r') as file:
				example = json.load(file)

			return example
		except FileNotFoundError as error:
			print(f'File not found.\n{error}')
		# Raises generic exception.
		except Exception as error:
			print(f'Generic error caught: {error}')

	# Prints array as list to terminal.
	# No RETURN, just prints to terminal
	def array_custom_print(array):
		if array == []:
			print('No results found. Food term does not appear to be legally defined.')
		else:
			print('\n'.join(map(str, array)))

	# Prints dict keys as list to terminal.
	# No RETURN, just prints to terminal
	def dict_key_custom_print(dictionary):
		if dictionary == {}:
			print('No results found. Food term does not appear to be legally defined.')
		else:
			for key in dictionary:
				print(key)

	# Generates dictionary with response results.
	# RETURNS dictionary containing result (results/headings/section)
	# as the key and description (full_text_excerpt) as the value.
	def search_results_dict(response):
		search_results_dict = {}

		for result in response['results']:
			# Restricts results returned to 'Food for Human Consumption' chapter.
			# https://www.youtube.com/watch?v=tphhdgi0R9w
			if result['hierarchy']['title'] == '21' and result['hierarchy']['subpart'] == 'B':
				search_results_dict[result['headings']['section']] = result['full_text_excerpt']

		return search_results_dict

	# Depreciated: Generates list with response results.
	# RETURNS array containing list of search terms
	def search_results_list(response):
		search_results_list = []

		for result in response['results']:
			if result['hierarchy']['title'] == '21' and result['hierarchy']['subpart'] == 'B':
				search_results_list.append(result['headings']['section'])

		return search_results_list
	# END: Methods
# END: JSONParser Class

# JSONParser.array_custom_print(JSONParser.search_results_list(JSONParser.example_response('sourdough')))
# JSONParser.dict_key_custom_print(JSONParser.search_results_dict(JSONParser.example_response('sourdough')))