from setuptools import setup, find_packages

setup(
    name='csv_to_dynamodb',
    version='0.1.0',
    author='Jason Miller',
    author_email='hackr@duck.com',
    description='A library for automatically creating DynamoDB tables from CSV files.',
    packages=find_packages(),
    install_requires=[
        'boto3',
    ],
)
