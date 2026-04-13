# python's moving away from setup.py to pyproject.toml
# files, but decided to use setup.py.
from setuptools import setup, find_packages

setup(
    name='LegalFoodDefinitionsUS',
    version='1.0.0',
    url='https://github.com/kayla-kubicke/LegalFoodDefinitionsUS.git',
    author='kayla-kubicke',
    author_email='161649341+kayla-kubicke@users.noreply.github.com',
    description='A search tool to navigate food terms regulated by US law.',
    packages=find_packages(),
    install_requires=['requests >= 2.33.1'],
)

# I've included the pip list if, for some horrific reason,
# pip does not automatically install requests' dependencies as expected.
# Also, I have a list of what's suppose to be here... In case
# I nuke something.
# Package            Version
# ------------------ ---------
# certifi            2026.2.25
# charset-normalizer 3.4.7
# idna               3.11
# pip                26.0.1
# requests           2.33.1
# urllib3            2.6.3