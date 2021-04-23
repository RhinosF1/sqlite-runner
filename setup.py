from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

# with open('CHANGELOG.md') as history_file:
    # history = history_file.read()

with open('dev-requirements.txt') as dev_requirements_file:
    dev_requirements = list(dev_requirements_file.readlines())


setup(
    name='sqliterunner',
    version='0.0.1',
    url='https://github.com/Pycryptor10/sqlite-runne',
    description='Simple script for making SQL Queries easier.',
    long_description=readme,  # + '\n\n' + history,
    long_description_content_type='text/markdown',  # This is important!
    author='Pycryptor10',
    author_email='Pycryptor10@gmail.com',
    packages=find_packages('.'),
    include_package_data=True,
    tests_require=dev_requirements,
    test_suite='tests',
    license='GPL3',
)