from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='get-report-template',
    version='0.0.5',
    description='',
    author='JayTrairat',
    author_email='jaytrairat@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jaytrairat/python-get-report-template',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'get-report-template = get_report_template.get_report_template:main'
        ]
    },
    package_data={
        'get-report-template':['*.docx']
    }
)