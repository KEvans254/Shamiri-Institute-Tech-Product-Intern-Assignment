# Shamiri Institute Tech Product Intern Assignment

## How to run the script
1. Install the required dependencies:
`pip install -r requirements.txt`

2. Update the .env file with your database credentials:
`DATABASE_URL=postgresql://[user]:[password]@[host]:[port]/[database]`

3. Run the script:
`python main.py`

## Optional

### Improving the Script's Efficiency
There are several ways to make the script more efficient:

1. Using a bulk insert method: Instead of inserting the records one by one, you can use a bulk insert method to insert multiple records at once. This will significantly reduce the time taken to insert the data into the database.

2. Caching data: If the data in the CSV file is large, you can cache the data in memory and then insert it into the database. This will reduce the time taken to read the data from the CSV file and insert it into the database.

3. Using a database connection pool: A database connection pool allows multiple connections to be made to the database and reused, which can reduce the time taken to establish a connection to the database.

### Ensuring the Script Runs whenever the CSV File is Updated
To ensure that the script runs whenever the CSV file is updated, you can set up a scheduling tool such as cron jobs or Windows Task Scheduler to run the script at a regular interval. For example, you can set the script to run every hour to check for updates to the CSV file. Additionally, you can add a check in the script to compare the modification date of the CSV file with the date of the last run of the script, and only run the script if the CSV file has been updated since the last run.