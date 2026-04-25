import json
from api.api_handler import ApiHandler as api_handler

# START: JSONParser Class
class JSONParser:
	# What's the deal with the spans? ?:|
	# Scrub html.
		# NOTE: span class=\"elipsis\" eliminates information.

	# START: Methods
	# REMOVE after manual testing or make happy home for specific json examples.
	# Expand method to accept whatever canned example desired.
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
	# REMOVE

	# REMOVE after manual testing or make happy home for printing services.
	# Longer term maybe override print(...)?
	# No RETURNS just prints to terminal
	def array_custom_print(array):
		print('\n'.join(map(str, array)))

	def dict_key_custom_print(dictionary):
		for key in dictionary:
			print(key)
	# REMOVE

	# Generates dictionary with response results.
	# RETURNS
	# dictionary containing term (results/headings/section) as the key and
	# description (full_text_excerpt) as the value.
	# https://www.youtube.com/watch?v=bkMdFBetM7U
	def search_results_dict(response):
		search_results_dict = {}

		for result in response['results']:
			search_results_dict[result['headings']['section']] = result['full_text_excerpt']

		return search_results_dict

	# Generates list with response results.
	# Updated query to response to eliminate coupling.
	# RETURNS
	# array containing list of unscrubbed search terms
	def search_results_list(response):
		# Longer term, will likely return dict with section as key
		# and full_text_excerpt as value.
		search_results_list = []

		for result in response['results']:
			search_results_list.append(result['headings']['section'])

		return search_results_list
	# END: Methods
# END: JSONParser Class

# JSONParser.array_custom_print(JSONParser.search_results_list(JSONParser.example_response()))
# JSONParser.dict_key_custom_print(JSONParser.search_results_dict(JSONParser.example_response()))