from setuptools import setup, find_packages
# import codecs
# import os
# 
# here = os.path.abspath(os.path.dirname(__file__))
# 
# with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
#     long_description = "\n" + fh.read()\

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '''0.10'''
DESCRIPTION = '''includes functions for finding windows based on various attributes, getting information about visible and invisible windows, and making window names unique'''

# Setting up
setup(
    name="appshwnd",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/appshwnd',
    author="Johannes Fischer",
    author_email="aulasparticularesdealemaosp@gmail.com",
    description=DESCRIPTION,
long_description = long_description,
long_description_content_type="text/markdown",
    #packages=['ctypes_window_info', 'flexible_partial'],
    keywords=['ctypes', 'hwnd', 'search', 'windows'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.10', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Utilities'],
    install_requires=['ctypes_window_info', 'flexible_partial'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*