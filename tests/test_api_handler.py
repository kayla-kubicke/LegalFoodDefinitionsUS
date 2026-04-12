# START: Mock
# from unittest.mock import patch
# ADD: import statement here

# class TestApiHandler:
#	@patch('')
# END: Mock


# from api.api_handler import ApiHandler

## REMOVE
# Super ultra fun import error
# 'ImportError: attempted relative import with no known parent package'
#
# .venv vs .env
# The virtual environment is a directory that contains libraries (and interpreters).
# The environment contains configuration information.
#
# os.environ['whatever']... vs. sys.path.append('whatever')
# os.environ['...'] directly modifies environmental variables.
# sys.path.append('...') add specified path to list of paths python will search
# when attempting to import a module (and packages); as noted previously.
#
#
# So... this combination imports correctly and hits print statement.
# import sys
# sys.path.append('/path/to/LegalFoodDefinitionsUS/on/my/machine')
#
# from api.api_handler import ApiHandler
# print ('working')
#
#
# :|
# So, I was wrong yesterday; the whole point of using a virtual environment
# is to avoid messing with your machine's evironmental variables. Although I
# wasn't completely lost becasue if PYTHONPATH is set, sys.path will pull it.
# Given that, hard coding PYTHONPATH on my machine is kinda silly for this purpose,
# but that would work given sys.path's pulling behavior.
#
# The solution seems to be to install e.
# As far I currently know, e basically just adds a .pth file which I could do myself.
# But, according to Gemini, e adds a 'few safety features'.
# Just going to go with e for now.
# 'pip install -e .'
# 'ERROR: ... does not appear to be a Python project: neither 'setup.py' nor 'pyproject.toml' found.''
# Ugh, now I need to set those two files or risk adding to .pth myself...
# https://www.youtube.com/watch?v=gFAXa7lpZmA
## REMOVE


# class TestHandler:
# ApiHandler.simple_call('soups');