# Libs
from botocore.exceptions import ClientError
from botocore.exceptions import NoCredentialsError
from math import isnan, isinf

import csv
import boto3
import decimal
import numpy as np
import os
import pandas as pd
import re
import uuid

# Main function
def create_table(access_key, secret_key, region, csv_path, table_name=None, hash_key=None, range_key=None):
    # Read in the CSV file and count the rows
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        header = reader.fieldnames
        num_rows = sum(1 for row in reader)

    # Read in all rows if there are fewer than 100, or sample 100 rows otherwise
    if num_rows < 100:
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            sample = [row for row in reader]
    else:
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            sample = [next(reader) for _ in range(100)]

    # Identify the column names
    column_names = header

    # Identify the data types for each column
    column_data_types = {}
    for name in column_names:
        column_data = [row[name] for row in sample if row[name]]
        if all(x.isdigit() for x in column_data):
            column_data_types[name] = 'N'
        else:
            column_data_types[name] = 'S'

    # Validate the table name
    if table_name is None:
        table_name = re.sub(r'\W+', '_', csv_path.split('/')[-1].split('.')[0])
    else:
        table_name = re.sub(r'\W+', '_', table_name)

    # Validate the column names
    for i in range(len(column_names)):
        column_names[i] = re.sub(r'\W+', '_', column_names[i])

    # Validate hash_key and range_key
    if hash_key is None:
        hash_key = column_names[0]

    if hash_key not in column_names:
        raise ValueError("Provided hash_key is not a valid column name.")

    if range_key and range_key not in column_names:
        raise ValueError("Provided range_key is not a valid column name.")

    # Create the DynamoDB table
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    dynamodb = session.resource('dynamodb')
    key_schema = [{'AttributeName': hash_key, 'KeyType': 'HASH'}]
    attribute_definitions = [{'AttributeName': hash_key, 'AttributeType': column_data_types[hash_key]}]

    if range_key:
        key_schema.append({'AttributeName': range_key, 'KeyType': 'RANGE'})
        attribute_definitions.append({'AttributeName': range_key, 'AttributeType': column_data_types[range_key]})

    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definitions,
        ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
    )

    # Wait for the table to become active
    table.wait_until_exists()

    return table

# Data ingest
def populate_table(access_key, secret_key, region, csv_path, table_name=None, hash_key=None, range_key=None):
    if isinstance(csv_path, str):
        csv_files = [csv_path]
    else:
        csv_files = csv_path

    for file_path in csv_files:
        if table_name is None:
            table_name = re.sub(r'\W+', '_', os.path.basename(file_path).split('.')[0])

        if os.path.isdir(file_path):
            csv_files_in_dir = [os.path.join(file_path, f) for f in os.listdir(file_path) if f.endswith('.csv')]
            csv_files.extend(csv_files_in_dir)
            continue

        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )
        dynamodb = session.resource('dynamodb')

        try:
            table = create_table(access_key, secret_key, region, file_path, table_name, hash_key, range_key)
            table = dynamodb.Table(table.name)
        except ClientError as e:
            if e.response['Error']['Code'] == "ResourceInUseException":
                table = dynamodb.Table(table_name)
            else:
                print(f"Unexpected error: {e}")
                continue
                
        if table.item_count > 0:
            print(f"The table {table.name} is not empty. Data upload stopped for this table.")
            continue

        chunksize = 500
        for chunk in pd.read_csv(file_path, chunksize=chunksize):
            # Replacing np.nan values with empty string
            chunk.replace(to_replace=np.nan, value="", inplace=True)

            # Add a unique key for each record
            unique_ids = pd.Series([uuid.uuid4().hex for _ in range(len(chunk))], name="UniqueID")
            chunk = pd.concat([chunk, unique_ids], axis=1)

            items = chunk.to_dict('records')

            # Convert data to proper format for dynamodb
            for item in items:
                for k, v in item.items():
                    try:
                        if pd.notnull(v):
                            if isinstance(v, float):
                                if isnan(v) or isinf(v):
                                    item[k] = None  # Or replace with a value of your choice
                                else:
                                    item[k] = decimal.Decimal(str(v))
                            elif isinstance(v, int):
                                item[k] = decimal.Decimal(str(v))
                            else:
                                item[k] = str(v)
                    except Exception as e:
                        print(f"Error converting value: {v} of type {type(v)} for key: {k}")
                        print(f"Unexpected error during conversion: {e}")
                        continue

            try:
                with table.batch_writer() as batch:
                    for item in items:
                        batch.put_item(Item=item)

            except NoCredentialsError:
                print("No AWS credentials found.")
                continue
            except Exception as e:
                print(f"Unexpected error: {e}")
                continue

        print(f"Data upload completed for {file_path} to table {table.name}.")
