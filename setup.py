from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'my_project_utilities = my_project.utilities:main',
        ],
    },
)
