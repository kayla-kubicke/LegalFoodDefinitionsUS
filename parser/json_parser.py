from api.example_handler import ExampleHandler as example_handler
# REMOVE after manual testing
import json
from printer.array_printer import ArrayPrinter as array_printer
from printer.dictionary_printer import DictionaryPrinter as dictionary_printer
# REMOVE after manual testing

# START: JSONParser Class
class JSONParser:
	# START: Methods
	# RETURNS True if title and chapter match values, False if title and
	# chapter never match
	def title_and_chapter_found_in_agency_json(agency, title, chapter):
		if agency == []:
			return False

		for reference in agency['cfr_references']:
			if reference.get('title') == title and reference.get('chapter') == chapter:
				return True
			else:
				continue

		return False

	# RETURNS an array of matching agencies, if empty no matching agencies
	# were found
	# ADD: id parent agency
	def agencies_responsible_for_title_and_chapter(title, chapter):
		# Seems like most chapters are written by only one agency,
		# but I don't actually know so I'll return an array.
		agency_array = []
		agencies = example_handler.example_response('agency_data', 'agencies')

		# Can't avoid nested for loops because of the json's structure.
		for agency in agencies['agencies']:
			if agency['children'] != []:
				for child in agency['children']:
					if JSONParser.title_and_chapter_found_in_agency_json(child, title, chapter):
						agency_array.append(child['short_name'])
			else:
				if JSONParser.title_and_chapter_found_in_agency_json(agency, title, chapter):
					agency_array.append(agency['short_name'])

		if agency_array == []:
			agency_array.append('unknown')

		return agency_array

	# Generates dictionary with response results.
	# UPDATE: RETURNS
	# (!) add exception handling test for output?
	# ADD: Second param, with the option of set or array; default = set. 
	def search_results_dict(response):
		if response == {}:
			return {}

		try:
			search_results_dict = {}
			index = 1

			for result in response['results']:
				agency_array = JSONParser.agencies_responsible_for_title_and_chapter(int(result['hierarchy']['title']), result['hierarchy']['chapter'])
				search_results_dict[f'result_{index}'] = {result['headings']['section']: result['full_text_excerpt'], 'authors': set(agency_array)}

				index += 1

			return search_results_dict
		except Exception as error:
			# Choosing to avoid silent handling whenever possible.
			print(f'Generic exception caught: {error}')

	# search_results_list(response) DEPRECIATED
	# Generates list with response results.
	# RETURNS array containing list of search terms
	# (!) not updated alongside search_results_dict(response), yet
	# (!) add exception handling test(s)
	def search_results_list(response):
		if response == {}:
			return []

		try:
			search_results_list = []
			for result in response['results']:
				if result['hierarchy']['title'] == '21' and result['hierarchy']['subpart'] == 'B':
					search_results_list.append(result['headings']['section'])

			return search_results_list

		except Exception as error:
			return search_results_list
	# search_results_list(response) DEPRECIATED
	# END: Methods
# END: JSONParser Class