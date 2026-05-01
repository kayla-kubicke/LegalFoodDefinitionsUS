# ADD: Unit tests

class ArrayPrinter:
	# Prints array as list to terminal.
	# No RETURN, just prints to terminal
	def array_custom_print(array):
		if array == []:
			print('No results found. Food term does not appear in document.')
		else:
			print('\n'.join(map(str, array)))