# Need to link agency with individual result.
	# This helps determine if result is legal, non-binding, etc.
# BUILD: agency_responsible_for_result(...); workshop name :/

# Also, I'm going to move JSONParser.example_response(query) and JSONParser.custom_print
# methods where they belong. Technically, should pull a separate branch but it's
# distracting me.
# https://www.youtube.com/watch?v=kewkTjNfUfk

import json
# REMOVE after manual testing
from api.example_handler import ExampleHandler as example_handler
from printer.array_printer import ArrayPrinter as array_printer
from printer.dictionary_printer import DictionaryPrinter as dictionary_printer
# REMOVE after manual testing

# START: JSONParser Class
class JSONParser:
	# START: Methods
	# Generates dictionary with response results.
	# RETURNS dictionary containing result (results/headings/section)
	# as the key and description (full_text_excerpt) as the value.
	def search_results_dict(response):
		search_results_dict = {}

		for result in response['results']:
			# UPDATE!
			# Restricts results returned to 'Food for Human Consumption' chapter.
			if result['hierarchy']['title'] == '21' and result['hierarchy']['subpart'] == 'B':
				search_results_dict[result['headings']['section']] = result['full_text_excerpt']

		return search_results_dict

	# search_results_list(response) DEPRECIATED
	# Generates list with response results.
	# RETURNS array containing list of search terms
	def search_results_list(response):
		search_results_list = []

		for result in response['results']:
			if result['hierarchy']['title'] == '21' and result['hierarchy']['subpart'] == 'B':
				search_results_list.append(result['headings']['section'])

		return search_results_list
	# search_results_list(response) DEPRECIATED
	# END: Methods
# END: JSONParser Class

# array_printer.array_custom_print(JSONParser.search_results_list(example_handler.example_response('sourdough')))
# dictionary_printer.dict_key_custom_print(JSONParser.search_results_dict(example_handler.example_response('sourdough')))