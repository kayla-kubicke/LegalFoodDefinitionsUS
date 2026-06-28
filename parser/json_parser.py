from enum import Enum
from api.example_handler import ExampleHandler as example_handler

# START: JSONParser Class
class JSONParser:
	# Inner class AuthorObjectType restricts the object type
	# of the 'authors' value inside the search results object.
	# (???) Update to use the (str, Enum) convention?
	class AuthorObjectType(Enum):
		SET = 1
		LIST = 2

	# Enables dynamic select of 'authors' object type and the correct
	# push/insert method.
	AUTHOR_OBJECT_TYPE_DICT = {
		AuthorObjectType.SET: { type: set(), 'insert_method': 'add' },
		AuthorObjectType.LIST: { type: [], 'insert_method': 'append' }
	}

	# START: Constructor
	# UPDATE: Refactor class
	def __init__(self, author_object_type: AuthorObjectType = AuthorObjectType.SET):
		self.author_object_type = author_object_type
	# END: Constructor

	# START: Methods
	# RETURNS
		# True if title and chapter match values,
		# False if title and chapter never match
	def title_and_chapter_found_in_agency_json(agency, title, chapter):
		if agency == []:
			return False

		for reference in agency['cfr_references']:
			if reference.get('title') == title and reference.get('chapter') == chapter:
				return True
			else:
				continue

		return False

	# RETURNS a list of matching agencies, if empty no matching agencies
	# were found
	def agencies_responsible_for_title_and_chapter(self, title, chapter):
		agencies = example_handler.example_response('agency_data', 'agencies')
		aotDict = JSONParser.AUTHOR_OBJECT_TYPE_DICT
		# Determines author_object's type.
		author_object = aotDict[self.author_object_type][type]

		if len(author_object) != 0:
			author_object.clear()

		# Can't avoid nested for loops because of the json's structure.
		for agency in agencies['agencies']:
			if agency['children'] != []:
				for child in agency['children']:
					if JSONParser.title_and_chapter_found_in_agency_json(child, title, chapter):
						getattr(author_object, aotDict[self.author_object_type]['insert_method'])(child['short_name'])
			else:
				if JSONParser.title_and_chapter_found_in_agency_json(agency, title, chapter):
					getattr(author_object, aotDict[self.author_object_type]['insert_method'])(agency['short_name'])

		if len(author_object) == 0:
			getattr(author_object, aotDict[self.author_object_type]['insert_method'])('unknown')

		return author_object

	# Generates dictionary with response results.
	# RETURNS
		# Successful: dict object containing search results
		# Unsuccessful: outputs information about error encountered
	def search_results_dict(self, response):
		if response == {}:
			return {}

		try:
			search_results_dict = {}
			index = 1

			for result in response['results']:
				agency_object = self .agencies_responsible_for_title_and_chapter(int(result['hierarchy']['title']), result['hierarchy']['chapter'])
				search_results_dict[f'result_{index}'] = {result['headings']['section']: result['full_text_excerpt'], 'authors': agency_object}

				index += 1

			return search_results_dict
		except Exception as error:
			print(f'Generic error caught: {error}')
	# END: Methods
# END: JSONParser Class