# from unittest.mock import patch
# ADD: import statement here

# class TestApiHandler:
#	@patch('')


# Broken
from ..api.api_handler import simple_call
# Need to import each method??? Gross.
# I must be missing something.
# Maybe it would just be 'import {correct traversal code}api.api_handler'
# for the class import?

## REMOVE
# Super ultra fun import error
# 'ImportError: attempted relative import with no known parent package'
# Just need to pop up one directory.
#
# import sys/sys.path.append('..') suggestion does not work (maybe investigate further?)
# What is this even doing anyway?...
#
# from ..api.api_handler import simple_call suggestion does not work
# '..' doesn't cause directory traversal as expected
#
# __init__.py addition to api/api_handler.py is not needed for ../test_handler.py to function
# https://www.youtube.com/watch?v=XswVWE0Jq84
## REMOVE

print('working')


# class TestHandler:
# ApiHandler.simple_call('soups');