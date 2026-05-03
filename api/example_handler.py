# ADD: Unit tests
import json

class ExampleHandler:
	# Generates a static response dict object to avoid
	# unnecessary api calls.
	# RETURNS canned response dict object
	def example_response(query):
		try:
			with open(f'assets/example_requests/{query}.json', 'r') as file:
				example = json.load(file)

			return example
		except FileNotFoundError as error:
			print(f'File not found.\n{error}')
		# Raises generic exception.
		except Exception as error:
			print(f'Generic error caught: {error}')