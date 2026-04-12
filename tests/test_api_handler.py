# START: Mock
# from unittest.mock import patch
# ADD: import statement here

# class TestApiHandler:
#	@patch('')
# END: Mock


# Broken: the command itself is likely fine,
# pretty sure PYTHONPATH isn't correctly set.
# from api.api_handler import ApiHandler

# Given this, why is 'sys.path' populated with several paths?
# import sys
# print(sys.path)

# ?:|

## REMOVE
# Super ultra fun import error
# 'ImportError: attempted relative import with no known parent package'
# https://www.youtube.com/watch?v=4KeII31qyck
#
# import sys
# sys.path.append('..')
# Code above simply adds specified path to array containing the paths
# python will search to locate modules (and packages?).
# Also, the addition is temporary; it's appended during runtime and
# only kept for the duration of the current process.
# As suspected, it's bad practice to throw path traversing trash
# in your code.
#
# I think I figured it out... I need to be build an .env project file.
# Need to set the evironmental variable(s) properly; specifically PYTHONPATH.
# Right now, 'echo $PYTHONPATH' returns nothing.
#
# One could do it directly in here, but I'm going to assume that's also
# bad practice and looks like hacky garbage.
# It would look something like:
# import os
# os.environ['PYTHONPATH']='../wow/that/looks/kinda/dangerous'
#
# NOTE: Update .gitignore after confirming this is actually the solution.
## REMOVE

print('working')


# class TestHandler:
# ApiHandler.simple_call('soups');