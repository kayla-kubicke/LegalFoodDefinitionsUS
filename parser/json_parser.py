from enum import Enum
from api.example_handler import ExampleHandler as example_handler
# REMOVE after manual testing
from printer.array_printer import ArrayPrinter as array_printer
from printer.dictionary_printer import DictionaryPrinter as dictionary_printer
# REMOVE after manual testing

# START: JSONParser Class
class JSONParser:
	# START: Constructor
	# UPDATE: Refactor class
	# def __init__(self, author_object_type: AuthorObjectType = AuthorObjectType.SET):
	# 	self.author_object_type = author_object_type
	# END: Constructor

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

	# Attempting to update search_results_dict(...) so I have the option to
	# create a classic json or a dict with nested sets.
	#
	# The coupling with agencies_responsible_for_title_and_chapter(...) is a little
	# worrisome.
	# Obviously, test suite fails.
	class AuthorObjectType(Enum):
		SET = 1
		LIST = 2

	# (!) Should this be a constant and/or moved to top of class?
	# Yes.
	# author_object_type_dict = {
	# 	AuthorObjectType.SET: set,
	# 	AuthorObjectType.LIST: []
	# }

	# Update the dict so I can id the correct method.
	author_object_type_dict = {
		AuthorObjectType.SET: { type: set, 'insert_method': 'add' },
		AuthorObjectType.LIST: { type: [], 'insert_method': 'append' }
	}
	# retrieved_function = getattr(type, insert_method)

	# RETURNS an array of matching agencies, if empty no matching agencies
	# were found
	# ADD: id parent agency
	# ADD: Testing
	# https://www.youtube.com/watch?v=hiQgQCK8nn0
	def agencies_responsible_for_title_and_chapter(title, chapter, author_object_type: AuthorObjectType = AuthorObjectType.SET): # Remove default?
		agencies = example_handler.example_response('agency_data', 'agencies')
		# 'Selects' returned_object's type.
		# author_object = JSONParser.author_object_type_dict.get(author_object_type)
		author_object = JSONParser.author_object_type_dict[author_object_type][type]
		# Is this the best way to deal with this?
		# Maybe it's time to add a constructor... Yeah.
		if len(author_object) != 0:
			# clear() works on both objects... thankfully.
			author_object.clear()

		# Ugh, no.
		retrieved_function = getattr([], JSONParser.author_object_type_dict[author_object_type]['insert_method'])
		# print(retrieved_function)
		# print(getattr([], JSONParser.author_object_type_dict[author_object_type]['insert_method']).callable())

		# Can't avoid nested for loops because of the json's structure.
		for agency in agencies['agencies']:
			if agency['children'] != []:
				for child in agency['children']:
					if JSONParser.title_and_chapter_found_in_agency_json(child, title, chapter):
						author_object.append(child['short_name'])
						# NO.
						# author_object.retrieved_function(child['short_name'])
			else:
				if JSONParser.title_and_chapter_found_in_agency_json(agency, title, chapter):
					author_object.append(agency['short_name'])
					# NO.
					# author_object.retrieved_function(agency['short_name'])

		if author_object == []:
			author_object.append('unknown')

		return author_object

	# Generates dictionary with response results.
	# UPDATE: RETURNS
	# (?) A better way to deal with the method coupling?
	# ADD: Testing
	def search_results_dict(response, author_object_type: AuthorObjectType = AuthorObjectType.SET):
		if response == {}:
			return {}

		try:
			search_results_dict = {}
			index = 1

			for result in response['results']:
				agency_object = JSONParser.agencies_responsible_for_title_and_chapter(int(result['hierarchy']['title']), result['hierarchy']['chapter'], author_object_type)
				search_results_dict[f'result_{index}'] = {result['headings']['section']: result['full_text_excerpt'], 'authors': agency_object}

				index += 1

			return search_results_dict
		except Exception as error:
			print(f'Generic error caught: {error}')

	# I think it's time to remove this...
	# Remember too remove the tests, too.
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
print(JSONParser.search_results_dict(choco, JSONParser.AuthorObjectType.LIST)) # , JSONParser.AuthorObjectType.LIST