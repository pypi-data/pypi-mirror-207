from setuptools import setup, find_packages

setup(
    name='csv_to_dynamodb',
    version='0.2.19',
    author='Jason Miller',
    author_email='hackr@duck.com',
    description='A library for automatically creating DynamoDB tables from CSV files and, optionally, automatically populating those tables.',
    long_description='A library for automatically creating DynamoDB tables from CSV files and, optionally, automatically populating those tables. The populate_table function handles floats/decimals, NaN, missing values, and create a unique Id for each row to use as a key.',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'botocore',
        'numpy',
        'pandas',
        'uuid'
    ],
)
