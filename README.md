# README

This script is used to import data from a JSON file into a PostgreSQL database. It assumes that you have a PostgreSQL database set up and have the necessary credentials to connect to it.

## Prerequisites

- PostgreSQL database
- Python 3.x
- psycopg2 library (can be installed using pip install psycopg2)

## Setup

1. Update the db_params dictionary with your database connection details (host, database name, username, password).
2. Update the json_file_path variable with the path to your JSON file.
3. Run the script.

## Usage

1. Make sure you have a PostgreSQL database set up.
2. Prepare a JSON file with the data you want to import.
3. Update the script with your database connection details and JSON file path.
4. Run the script.

The script will create a table called message_table if it doesn't already exist in the specified database. It will then read the data from the JSON file and insert it into the table.

Once the script has finished running, it will print a success message indicating that the data has been successfully saved in the database.

Note: Make sure you have the necessary permissions to create tables and insert data into the specified database.
