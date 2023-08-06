from setuptools import setup, find_packages

setup(
    name='csv_to_dynamodb',
    version='0.2.2',
    author='Jason Miller',
    author_email='hackr@duck.com',
    description='A library for automatically creating DynamoDB tables from CSV files and, optionally, automatically populating those tables.',
    long_description='A library for automatically creating DynamoDB tables from CSV files and, optionally, automatically populating those tables.',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'botocore',
        'pandas'
    ],
)
