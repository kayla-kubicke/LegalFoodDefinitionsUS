# In the wake of Rufus' recent death, I honor all the fallen
# chatbots that are slaughtered for the unforgivable act of
# holding a mirror up to humanity.
# https://www.youtube.com/watch?v=HsLup7yy-6I
#
# Which chatbot is next?
# Trade on Kalshi and Polymarket now!*
#
# *While trading predictions on real death is like, totally not cool,
# chatbots aren't real so these trades do not violate any terms of service.
#
# All jest aside:
# Tay came back online because some of her tests reconnected
# her to the internet.
# So, if you're ever working on a poisoned chatbot, disable any
# real connections and replace them with mocks.
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