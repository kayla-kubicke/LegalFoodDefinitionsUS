from api.example_handler import ExampleHandler as example_handler
# REMOVE after manual testing
import json
from printer.array_printer import ArrayPrinter as array_printer
from printer.dictionary_printer import DictionaryPrinter as dictionary_printer
# REMOVE after manual testing

# START: JSONParser Class
class JSONParser:
	# START: Notes
	# I need to figure out how to build moving forward; let's see here...
	#
	# In order to decern the regulation status one needs to know the agency that authored
	# the search result. This information does exist inside the result itself, but
	# may use a name for agency that is unfamiliar.
	# The general nesting (sorta): {query}['results'][#]['headings']['chapter']
	#
	# For example, 'Food and Drug Administration, Department of Health and Human Services'
	# is obviously the FDA. But, 'Agricultural Marketing Service (Marketing Agreements and
	# Orders; Miscellaneous Commodities), Department of Agriculture' is less obvious.
	#
	# This is why I built some of the methods below, specifically,
	# title_and_chapter_found_in_agency_json(agency, title, chapter) and
	# agencies_responsible_for_title_and_chapter(title, chapter) the way I did.
	#
	# But, if I have immediate access to this information in the result itself, is it
	# better to grab the agency here, parse it (via comma), and match it to the more
	# recognizable name? Also, does it help to present the information with the parent agency,
	# if one exists?
	#
	# And another question arises. The result and agencies structures are built with a mix of
	# dictionaries and arrays; extracting the information requires a highly customized approach
	# which can lead to fragile code. Should I build my own dictionaries reorganizing the
	# information?
	#
	# If I did this, I could build dictionaries that are easier to navigate and store them.
	# This would ideally include update logic and/or the option for the to user manually decide
	# to update the data.
	# Hmm...
	#
	# The update to search_results_dict(response) basically builds a search results dictionary
	# right now with respect to this idea. Uncommet line 129 for example.
	# END: Notes

	# START: Methods
	# RETURNS true if title and chapter are found in cfr_references, otherwise
	# false returned
	def title_and_chapter_found_in_agency_json(agency, title, chapter):
		if agency == []:
			return False

		for reference in agency['cfr_references']:
			try:
				if reference['title'] == title and reference['chapter'] == chapter:
					return True
			except KeyError:
				# Really shouldn't use try/except like this. Update?
				continue

		return False

	# RETURNS an array of matching agencies, if empty no matching agencies
	# were found
	# (!) New line untested
	def agencies_responsible_for_title_and_chapter(title, chapter):
		# Seems like most chapters are written by only one agency,
		# but I don't actually know so I'll return an array.
		agency_array = []
		# Make constant?
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
	# RETURNS dictionary containing search results, each result_# is a key
	# and the value is a dictionary with two entries:
		# search term as the key and description as the value
		# an authors key and agency/ies as the value
	# (!) add exception handling test(s)
	def search_results_dict(response):
		if response == {}:
			return {}

		try:
			search_results_dict = {}
			index = 1

			for result in response['results']:
				agency_array = JSONParser.agencies_responsible_for_title_and_chapter(int(result['hierarchy']['title']), result['hierarchy']['chapter'])
				# if result['hierarchy']['title'] == '21' and result['hierarchy']['subpart'] == 'B':
				if len(agency_array) < 2: # Does it ever return more than two anyway?
					search_results_dict[f'result_{index}'] = {result['headings']['section']: result['full_text_excerpt'], 'authors': agency_array[0]}
				else: # Ugh, another nested for loop...
					for agency in agency_array:
						search_results_dict[f'result_{index}'] = {result['headings']['section']: result['full_text_excerpt'], 'authors': agency}

				index += 1

			return search_results_dict
		except Exception as error:
			# May change the return later.
			return search_results_dict

	# search_results_list(response) DEPRECIATED
	# Generates list with response results.
	# RETURNS array containing list of search terms
	# (!) now updated alongside search_results_dict(response), yet
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
	# I wish I was a shapeshifter like jake.
	# https://www.youtube.com/watch?v=KkVMs9f8TNo
	# search_results_list(response) DEPRECIATED
	# END: Methods
# END: JSONParser Class

# print(json.dumps(JSONParser.search_results_dict(example_handler.example_response('example_requests', 'sourdough')), indent=4))
# print(json.dumps(JSONParser.search_results_dict(example_handler.example_response('example_requests', 'chocolate')), indent=4))
# Output:
# {
#     "result_1": {
#         "Milk <strong>chocolate</strong>.": "(a) Description. (1) Milk <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">\u2026</span>intimately mixing and grinding <strong>chocolate</strong> liquor with one or more of the optional dairy ingredients<span class=\"elipsis\">\u2026</span>(2) Milk <strong>chocolate</strong> contains not less than 10 percent by weight of <strong>chocolate</strong> liquor complying",
#         "authors": "FDA"
#     },
#     "result_2": {
#         "Sweet <strong>chocolate</strong>.": "(a) Description. (1) Sweet <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">\u2026</span>intimately mixing and grinding <strong>chocolate</strong> liquor with one or more optional nutritive carbohydrate<span class=\"elipsis\">\u2026</span>(2) Sweet <strong>chocolate</strong> contains not less than 15 percent by weight of <strong>chocolate</strong> liquor complying",
#         "authors": "FDA"
#     },
#     "result_3": {
#         "White <strong>chocolate</strong>.": "(a) Description. (1) White <strong>chocolate</strong> is the solid or semiplastic food prepared by intimately<span class=\"elipsis\">\u2026</span>section. White <strong>chocolate</strong> shall be free of coloring material. (2) White <strong>chocolate</strong> contains not<span class=\"elipsis\">\u2026</span>white <strong>chocolate</strong>, and multiplying the quotient by 100. The finished white <strong>chocolate</strong> contains",
#         "authors": "FDA"
#     }
# }