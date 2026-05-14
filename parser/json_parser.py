from enum import Enum
from api.example_handler import ExampleHandler as example_handler
# REMOVE after manual testing
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

	# https://www.youtube.com/watch?v=bgGsacqNVOQ
	# Attempting to update search_results_dict(...) so I have the option to
	# create a classic json or a dict with nested sets.
	#
	# The coupling with agencies_responsible_for_title_and_chapter(...) is a little
	# worrisome.
	# Obviously, test suite fails.
	class AuthorObject(Enum):
		SET = 1 # Maybe use bool? :/ But doesn't clearly convey what is going on.
		LIST = 2 # Also, can't update a bool, but this is extremely unlikey to grow.
		# But, how to control the object creation? getattr?

	# (!) Should this be a constant and/or moved to top of class?
	# Yes.
	author_object_dict = {
		AuthorObject.SET: set,
		AuthorObject.LIST: []
	}

	# Update the dict so I can id the correct method.
	# author_object_dict = {
	# 	AuthorObject.SET: { type: set, insert_method: 'add' }
	# 	AuthorObject.LIST: { type: [], insert_method: 'append' }
	# }
	# retrieved_function = getattr(type, insert_method)

	# RETURNS an array of matching agencies, if empty no matching agencies
	# were found
	# ADD: id parent agency
	# ADD: Testing
	def agencies_responsible_for_title_and_chapter(title, chapter, author_object): # FIX: author_object unbounded
		# Sets agency_object type
		# UPDATE, ew!
		agency_object = author_object
		# UPDATE
		agencies = example_handler.example_response('agency_data', 'agencies')

		# Can't avoid nested for loops because of the json's structure.
		for agency in agencies['agencies']:
			if agency['children'] != []:
				for child in agency['children']:
					if JSONParser.title_and_chapter_found_in_agency_json(child, title, chapter):
						agency_object.append(child['short_name'])
			else:
				if JSONParser.title_and_chapter_found_in_agency_json(agency, title, chapter):
					agency_object.append(agency['short_name'])

		if agency_object == []:
			agency_object.append('unknown')

		return agency_object
	# https://www.youtube.com/watch?v=rWYBcsK8V5E


	# Generates dictionary with response results.
	# UPDATE: RETURNS
	# (?) A better way to deal with the method coupling?
	# ADD: Testing
	def search_results_dict(response, author_object: AuthorObject = AuthorObject.SET):
		if response == {}:
			return {}

		try:
			# Is this required and/or needs refining?
			author_object = JSONParser.author_object_dict.get(author_object)
			search_results_dict = {}
			index = 1

			for result in response['results']:
				agency_object = JSONParser.agencies_responsible_for_title_and_chapter(int(result['hierarchy']['title']), result['hierarchy']['chapter'], author_object)
				# Address agency array? Address it method above?
				search_results_dict[f'result_{index}'] = {result['headings']['section']: result['full_text_excerpt'], 'authors': set(agency_object)} # getattr(...)

				index += 1

			return search_results_dict
		except Exception as error:
			print(f'Generic error caught: {error}')

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

choco = example_handler.example_response('example_requests', 'chocolate')
print(JSONParser.search_results_dict(choco, JSONParser.AuthorObject.LIST)) # , JSONParser.AuthorObject.LIST