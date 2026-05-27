# import re
# https://docs.python.org/3/library/re.html
import api.api_constants as api_constants

class QueryModifier:
	# What do I need to do?
	# Remove excess spaces.
	# Remove non-alpha characters? Can't see why a query would use non-alphas.
	#
	# re.split(...)
	# Could split and...
		# use individual term(s)
		# make combos of all terms (quickly becomes costly, not too useful under normal conditions)

	def pad_query(query):
		modified_query = ''

		for character in query:
			if character == ' ':
				modified_query = modified_query + api_constants.SPACE
			else:
				modified_query = modified_query + character

		return modified_query