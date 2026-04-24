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
	# REMOVE

	# Generate list with response results.
	# Updated query to response to eliminate coupling.
	# RETURNS
	# array containing list of unscrubbed search terms
	def ugly_list(response):
		# Longer term, will likely return dict with section as key
		# and full_text_excerpt as value.
		ugly_list =[]

		for result in response['results']:
			ugly_list.append(result['headings']['section'])

		return ugly_list
	# END: Methods
# END: JSONParser Class

# JSONParser.array_custom_print(JSONParser.ugly_list(JSONParser.example_response()))