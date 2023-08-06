# csv-to-dynamodb

A Python library to create a DynamoDB table from a CSV file. Optionally, these tables can be populated with populate_table, which also supports directories and lists of CSVs as inputs.

## Installation

Available on PyPI (and therefore via pip, pip3, etc). 

https://pypi.org/project/csv-to-dynamodb/0.1.0/

```python
pip3 install csv-to-dynamodb
```

## Dependencies

This library uses boto3, botocore, and pandas. They are included in the requirements.txt and the setup.py files.

## Usage

The `create_table` method can be used to create tables as follows:

```python
import csv_to_dynamodb

# Required:
access_key = "your_aws_access_key"
secret_key = "your_aws_secret_key"
region     = "your_aws_region"
csv_path   = "/path/to/your/csv_file.csv"

# Optional:
table_name = "your_table_name"
hash_key   = "your_hash_key"
range_key  = "your_range_key"

# Invocation:
table = csv_to_dynamodb.create_table(
    access_key = access_key,
    secret_key = secret_key,
    region     = region,
    csv_path   = csv_path
)
```

`populate_table` creates the table if it's not already created and populates it. It will populate an existing but empty table of the same name if the columns and data types match.

```
populate_table(
    access_key = access_key,
    secret_key = secret_key,
    region     = region,
    csv_path   = csv_path,
    table_name = table_name,
    hash_key   = hash_key,
    range_key  = range_key
)
```

See sample_usage.py and sample_usage2.py for more examples.

## Arguments:

- access_key (required): Your AWS access key.
- secret_key (required): Your AWS secret key.
- region (required): The AWS region you want to create the table in.
- csv_path (required): The path to your CSV file.
- table_name (optional): The name you want to give to your DynamoDB table. If not specified, it will default to the name of your CSV file with non-alphanumeric characters replaced with underscores.
- hash_key (optional): The name of the column in your CSV file to use as the hash key for your DynamoDB table. If not specified, it will default to the first column in your CSV file.
- range_key (optional): The name of the column in your CSV file to use as the range key for your DynamoDB table. If not specified, your table will not have a range key.

## License: 

GNU v3

