from parser.json_parser import JSONParser as json_parser

class JSONAssembler():
	# What do I need?
	# Write JSON to file
	# No RETURN
	def publish_JSON(type, name, assembled_json):
		try:
			with open(f'assets/{type}/{name}.json', 'w') as file:
				file.write(assembled_json)

		except Exception as error:
			print(f'Generic error caught: {error}')

	# links agency to title and chapter


	# build collection of agency title/chapter jsons?