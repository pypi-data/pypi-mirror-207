import os, sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'zeroth_normalizer'))

from setuptools import setup, find_packages
from version import version as VERSION

description = ''
with open('README.md', 'r', encoding="UTF-8") as _file:
  description = _file.read()
  _file.close()

setup(
  name                = 'zeroth_normalizer',
  version             = VERSION,
  description         = 'zeroth korean text normalizer',
  long_description    = description,
  long_description_content_type = 'text/markdown',
  author              = 'drowsy-probius',
  author_email        = 'k123s456h@gmail.com',
  url                 = 'https://github.com/drowsy-probius/zeroth-normalizer',
  license             = 'MIT',
  install_requires    =  ['requests'],
  packages            = find_packages(exclude = []),
  keywords            = ['natural language processor', 'normalizer', 'zeroth', 'korean', 'text normalizer', 'korean text', 'korean language'],
  python_requires     = '>=3.8',
  package_data        = {},
  zip_safe            = False,
  classifiers         = [
    'Programming Language :: Python :: 3.8',
    'Operating System :: OS Independent',
  ],
)

# rm -r build/ dist/ papagopy.egg*
# python3 setup.py sdist bdist_wheel
# python3 -m twine upload dist/*