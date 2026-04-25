import json
from api.api_handler import ApiHandler as api_handler

# START: JSONParser Class
class JSONParser:
	# START: Methods
	# Generates a static response dict object to avoid
	# unnecessary api calls.
	# RETURNS canned response dict object
	def example_response():
		try:
			with open('parser/example.json', 'r') as file:
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
		print('\n'.join(map(str, array)))

	# Prints dict keys as list to terminal.
	# No RETURN, just prints to terminal
	def dict_key_custom_print(dictionary):
		for key in dictionary:
			print(key)
	# REMOVE

	# Generates dictionary with response results.
	# RETURNS dictionary containing result (results/headings/section)
	# as the key and description (full_text_excerpt) as the value.
	def search_results_dict(response):
		search_results_dict = {}

		for result in response['results']:
			search_results_dict[result['headings']['section']] = result['full_text_excerpt']

		return search_results_dict

	# Generates list with response results.
	# RETURNS array containing list of search terms
	def search_results_list(response):
		search_results_list = []

		for result in response['results']:
			search_results_list.append(result['headings']['section'])

		return search_results_list
	# END: Methods
# END: JSONParser Class