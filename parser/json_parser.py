import json
# REMOVE after manual testing
from api.example_handler import ExampleHandler as example_handler
from printer.array_printer import ArrayPrinter as array_printer
from printer.dictionary_printer import DictionaryPrinter as dictionary_printer
# REMOVE after manual testing

# START: JSONParser Class
class JSONParser:
	# START: Methods
	# UPDATE: method names?
	# https://www.youtube.com/watch?v=dI1keSSwdcI
	# RETURNS true if title and chapter are found in cfr_references, otherwise false returned
	# (!) Untested, just manual testing today
	def title_and_chapter_found(agency, title, chapter):
		# Check for empty array? Shouldn't happen...
		for reference in agency['cfr_references']:
			try:
				if reference['title'] == title and reference['chapter'] == chapter:
					return True
			except KeyError:
				continue

		return False

	# https://www.youtube.com/watch?v=hj0yVN8pFNw
	# RETURNS an array of matching agencies
	# (!) Untested, just manual testing today
	def agencies_responsible_for_title_and_chapter(title, chapter):
		# Seems like most chapters are written by only one agency,
		# but I don't actually know so I'll return an array.
		agency_array = []

		agencies = example_handler.example_response('agencies')

		# Yikes...
		# Can't avoid nested for loops because of the json's structure.
		# ¯\_(ツ)_/¯
		# Maybe use these methods to build a 'database' to avoid these calls longer term.
		# Uncomment lines 88 & 89
		for agency in agencies['agencies']:
			if agency['children'] != []:
				for child in agency['children']:
					if JSONParser.title_and_chapter_found(child, title, chapter):
						agency_array.append(child['short_name'])
			else:
				if JSONParser.title_and_chapter_found(agency, title, chapter):
					agency_array.append(agency['short_name'])

		return agency_array

	# Generates dictionary with response results.
	# RETURNS dictionary containing result (results/headings/section)
	# as the key and description (full_text_excerpt) as the value.
	# ADD: Ugh, just build a database so I don't repeat searches.
	def search_results_dict(response):
		search_results_dict = {}

		for result in response['results']:
			# UPDATE!
			# Restricts results returned to 'Food for Human Consumption' chapter.
			# What's the best way to do this?
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

# thing = JSONParser.agencies_responsible_for_title_and_chapter(25, 'VII')
# print('\n'.join(map(str, thing)))