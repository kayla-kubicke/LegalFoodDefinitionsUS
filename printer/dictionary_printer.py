# ADD: Unit tests

class DictionaryPrinter:
	# Prints dict keys as list to terminal.
	# No RETURN, just prints to terminal
	def dict_key_custom_print(dictionary):
		if dictionary == {}:
			print('No results found. Food term does not appear to be legally defined.')
		else:
			for key in dictionary:
				print(key)