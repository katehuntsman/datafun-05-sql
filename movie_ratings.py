"""
This script demonstrates interaction with an SQLite database
containing movie directors and their ratings.
"""

import logging
import sqlite3
from pathlib import Path

# Configure logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_database(db_file_path):
    """Create a new SQLite database or connect to existing."""
    try:
        with sqlite3.connect(db_file_path) as conn:
            logging.info("Database created/connected successfully.")
    except Exception as e:
        logging.exception("Failed to create/connect to the database.")

def execute_sql_from_file(db_filepath, sql_file):
    """Execute SQL commands from a file."""
    try:
        with sqlite3.connect(db_filepath) as conn:
            with open(sql_file, 'r') as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Executed SQL from {sql_file}")
    except Exception as e:
        logging.exception("Error executing SQL from file.")

def main():
    logging.info("Program started")

    # Define paths
    db_file_path = Path("movies.db")
    create_tables_path = Path("sql/create_tables.sql")
    insert_records_path = Path("sql/insert_records.sql")

    # Create database
    create_database(db_file_path)

    # Create tables
    execute_sql_from_file(db_file_path, create_tables_path)

    # Insert records
    execute_sql_from_file(db_file_path, insert_records_path)

    logging.info("All SQL operations completed successfully")
    logging.info("Program ended")

if __name__ == "__main__":
    main()
