# START: Mock
# from unittest.mock import patch
# ADD: import statement here

# class TestApiHandler:
#	@patch('')
# END: Mock

# Still broken.
from api.api_handler import ApiHandler

## REMOVE
# https://www.youtube.com/watch?v=o0vUppC58V8
# Added setup.py and ran 'pip install -e .'; still broken.
# No .pth file was generated; just generated an .egg-info metadata file.
# ???
# So either setup.py is incorrect or running editable mode
# is not really the solution.
# https://stackoverflow.com/questions/2145779/setup-py-installing-just-a-pth-file
## REMOVE


# class TestHandler:
# ApiHandler.simple_call('soups');