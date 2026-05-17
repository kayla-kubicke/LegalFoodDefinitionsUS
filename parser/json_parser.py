from enum import Enum
from api.example_handler import ExampleHandler as example_handler
# REMOVE after manual testing
from printer.array_printer import ArrayPrinter as array_printer
from printer.dictionary_printer import DictionaryPrinter as dictionary_printer
# REMOVE after manual testing

# START: JSONParser Class
# Getting ready to merge.
# Maybe the name is bit misleading. Hm... The class turned out
# to both parse and return a search results object... I could split
# it up between two classes longer term if it's really an issue.
class JSONParser:
	# Inner class AuthorObjectType is used to restrict the object type
	# of the 'authors' key inside the search results object.
	# https://www.youtube.com/watch?v=L7Ln56-p6lY
	class AuthorObjectType(Enum):
		SET = 1
		LIST = 2

	# Expanded dictionary was introduced so I could dynamically select
	# the object type as well as the correct push/insert method.
	AUTHOR_OBJECT_TYPE_DICT = {
		AuthorObjectType.SET: { type: set(), 'insert_method': 'add' },
		AuthorObjectType.LIST: { type: [], 'insert_method': 'append' }
	}

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

	# RETURNS an array of matching agencies, if empty no matching agencies
	# were found
	# ADD: id parent agency
	# ADD: Testing
	# UPDATE: Reduce repeat code
	def agencies_responsible_for_title_and_chapter(title, chapter, author_object_type: AuthorObjectType = AuthorObjectType.SET): # Remove default?
		agencies = example_handler.example_response('agency_data', 'agencies')
		aotDict = JSONParser.AUTHOR_OBJECT_TYPE_DICT
		# 'Selects' returned_object's type.
		author_object = aotDict[author_object_type][type]

		if len(author_object) != 0:
			author_object.clear()

		# Can't avoid nested for loops because of the json's structure.
		for agency in agencies['agencies']:
			if agency['children'] != []:
				for child in agency['children']:
					if JSONParser.title_and_chapter_found_in_agency_json(child, title, chapter):
						getattr(author_object, aotDict[author_object_type]['insert_method'])(child['short_name'])
			else:
				if JSONParser.title_and_chapter_found_in_agency_json(agency, title, chapter):
					getattr(author_object, aotDict[author_object_type]['insert_method'])(agency['short_name'])

		if len(author_object) == 0:
			getattr(author_object, aotDict[author_object_type]['insert_method'])('unknown')

		return author_object

	# Generates dictionary with response results.
	# UPDATE: RETURNS
		# Successful: dict object containing search results
		# Unsuccessful: outputs information about error encountered
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

# choco = example_handler.example_response('example_requests', 'chocolate')
# print(JSONParser.search_results_dict(choco)) # , JSONParser.AuthorObjectType.LIST