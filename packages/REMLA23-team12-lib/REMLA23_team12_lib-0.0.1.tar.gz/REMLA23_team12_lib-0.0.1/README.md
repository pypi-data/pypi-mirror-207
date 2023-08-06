# lib
To lease python package:
1. Create a PyPI account
2. Create "setup.py".This is a guide file for python module distribution and installation.(the 'name' in setup.py should be the same as the name of the file to be uploaded.)
3. Install setuptools and twine by "pip install setuptools twine".
4. Run "python setup.py sdist bdist_wheel" to create distribution files in a dist.
5. Run "twine upload <actual path to dist/ directory>/*".  Then the distribution files will upload to PyPI.

We also create release.yml as the workflow file to automate the release process.

TODO: check wether the version is automatically updated by the workflow.
