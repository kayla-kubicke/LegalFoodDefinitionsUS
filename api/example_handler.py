# ADD: Unit tests
import json

class ExampleHandler:
	# Generates a static response dict object to avoid
	# unnecessary api calls.
	# RETURNS canned response dict object
	# Since I'm just using the method for testing purpose, for now,
	# I'm going to build the method with another param for the directory
	# location. I'll stick to this convention.
	def example_response(type, query):
		try:
			with open(f'assets/{type}/{query}.json', 'r') as file:
				example = json.load(file)

			return example
		except FileNotFoundError as error:
			print(f'File not found.\n{error}')
		# Raises generic exception.
		except Exception as error:
			print(f'Generic error caught: {error}')