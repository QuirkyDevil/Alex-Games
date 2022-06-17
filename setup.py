from   setuptools import setup
import re

with open("Alex_Games/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setup(
    name         = "Alex_Games", 
    author       = "QuirkyDevil", 
    version      = version, 
    description  = "A library for Alex Boat's game logic",
    long_description              = open("README.md").read(),
    long_description_content_type = "text/markdown",
    license      = "MIT",
    url          = "https://github.com/QuirkyDevil/Alex-Games",
    project_urls = {
        "Repository"   : "https://github.com/QuirkyDevil/Alex-Games",
        "Issue tracker": "https://github.com/QuirkyDevil/Alex-Games/issues",
    },
    classifiers  = [
        "Intended Audience :: Developers",
        'Programming Language :: Python',
        'Natural Language :: English',
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    include_package_data = True,
    packages             = ['Alex_Games'],
    install_requires     = ['discord.py', 'english-words', 'akinator.py', 'Pillow',],
    zip_safe        = True,
    python_requires = '>=3.7'
)