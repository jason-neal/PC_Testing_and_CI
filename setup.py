#Example setup.py file for a project.
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Example steup.py',
    'author': 'Jason Neal',
    'url': 'https://github.com/jason-neal/PC_Testing_and_CI.git',
    'download_url': 'https://github.com/jason-neal/PC_Testing_and_CI.git',
    'author_email': 'jason.neal@astro.up.pt',
    'version': '0.1',
    'license': 'MIT',
    'setup_requires': [],
    'install_requires': ['pytest'],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    'extras_require': {
        'dev': ['check-manifest'],
        'test': ['hypothesis'],
    },
    'packages': [],
    'scripts': ["examples.py"],
    'name': 'PC_Testing_and_CI',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    "classifiers": [
        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        # Specify the Python versions you support here.
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
    ],
    # What does your project relate to?
    "keywords": [],
}

setup(**config)
