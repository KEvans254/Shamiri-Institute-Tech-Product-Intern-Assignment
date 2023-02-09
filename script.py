import os
import psycopg2
import csv

def create_table(conn, cursor):
    # Drops table if it already exists
    cursor.execute("DROP TABLE IF EXISTS mock_data;")
    # Create table
    cursor.execute("""
        CREATE TABLE mock_data (
            id INTEGER,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            gender TEXT,
            ip_address TEXT,
            isAdmin BOOLEAN
        );
    """)
    print("Table created successfully.")
    # Commit changes
    conn.commit()

def insert_data(conn, cursor):
    with open('MOCK_DATA.csv', 'r') as f:
        # Create a reader object
        reader = csv.reader(f)
        # Skip the header row
        next(reader)
        # Insert data into table
        for row in reader:
            # Handle missing data by using the NULL value
            row = [None if value == '' else value for value in row]
            cursor.execute("""
                INSERT INTO mock_data (id, first_name, last_name, email, gender, ip_address, isAdmin)
                VALUES (%s, %s, %s, %s, %s, %s, %s);
            """, row)
    # Commit changes
    conn.commit()
    print("Data inserted successfully.")

def main():
    # Load database credentials from .env file
    DATABASE_URL = os.getenv("DATABASE_URL")
    # Connect to database
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    # Create table and insert data
    create_table(conn, cursor)
    insert_data(conn, cursor)
    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
