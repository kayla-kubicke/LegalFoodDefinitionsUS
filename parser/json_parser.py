import json
from api.api_handler import ApiHandler as api_handler


class JSONParser:
	# What's the deal with the spans?
	# https://www.youtube.com/watch?v=Z87gchDzsAA

	# Scrub html.
		# NOTE: span class=\"elipsis\" eliminate information.

	# Generate list with terms above.
	def ugly_list(query): # Ugly duckling will transform into swan.
 		# request = api_handler.simple_call(query)
		# print(example['results'][2]['headings']['section']) # Update.

		# REMOVE after manual testing.
		with open('parser/example.json', 'r') as file:
			example = json.load(file)

		print('\n')

		for result in example['results']:
			print(result['headings']['section'] + '\n')
		# REMOVE


JSONParser.ugly_list('milk')