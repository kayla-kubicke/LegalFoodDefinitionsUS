class QueryModifier:
	SPACE = '%20'

	def pad_query(query):
		modified_query = ''

		for character in query:
			if character == ' ':
				modified_query = modified_query + QueryModifier.SPACE
			else:
				modified_query = modified_query + character

		return modified_query