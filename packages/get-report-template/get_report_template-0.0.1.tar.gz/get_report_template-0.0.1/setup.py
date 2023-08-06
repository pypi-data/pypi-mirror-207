from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='get_report_template',
    version='0.0.1',
    description='',
    author='JayTrairat',
    author_email='jaytrairat@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jaytrairat/python-get-report-template',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'get-report-template = src.get_report_template:main'
        ]
    }
)