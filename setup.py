import io
import json
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'datawatts'
DESCRIPTION = 'datassette podcast and alan watts randomized stream.'
URL = 'https://github.com/run2dev/datawatts'
EMAIL = 'run2devtest@gmail.com'
AUTHOR = 'Degennosaurus REKT'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.4'

here = os.path.abspath(os.path.dirname(__file__))

# Pipfile parser
with io.open(os.path.join(here, 'Pipfile.lock'), encoding='utf-8') as f:
    packages = json.loads(f.read())['default']


# What packages are required for this module to be executed?
REQUIRED = []
for pack in packages.keys():
    pypi = packages[pack]
    REQUIRED.append(pack)


# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

print(long_description)

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    entry_points={
        'console_scripts': ['datawatts=datawatts.run:main'],
    },
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
