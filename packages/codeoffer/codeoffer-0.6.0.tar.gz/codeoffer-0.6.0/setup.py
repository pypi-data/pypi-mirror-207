from setuptools import setup, find_packages

setup(
    name='codeoffer',
    version='0.6.0',
    description='Python library that simplifies access to the Public CodeOffer API',
    author='CodeOffer',
    author_email='contact@codeoffer.net',
    packages=find_packages(),
    url='https://github.com/codeoffer/v1-python-library',
    project_urls={
        'Documentation': 'https://github.com/codeoffer/v1-python-library',
        'Source': 'https://github.com/codeoffer/v1-python-library'
    },
    long_description_content_type="text/markdown",
    long_description=open("README.md", "r", encoding="utf-8").read(),
)
