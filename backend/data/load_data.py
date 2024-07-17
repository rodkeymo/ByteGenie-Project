import csv
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS company (
    company_logo_text TEXT,
    company_name TEXT,
    relation_to_event TEXT,
    event_url TEXT,
    company_revenue TEXT,
    n_employees INTEGER,
    company_phone TEXT,
    company_founding_year INTEGER,
    company_address TEXT,
    company_industry TEXT,
    company_overview TEXT,
    homepage_url TEXT,
    linkedin_company_url TEXT,
    homepage_base_url TEXT,
    company_logo_url_on_event_page TEXT,
    company_logo_match_flag TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS people (
    first_name TEXT,
    middle_name TEXT,
    last_name TEXT,
    job_title TEXT,
    person_city TEXT,
    person_state TEXT,
    person_country TEXT,
    email_pattern TEXT,
    homepage_base_url TEXT,
    duration_in_current_job TEXT,
    duration_in_current_company TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS event (
    event_logo_url TEXT,
    event_name TEXT,
    event_start_date TEXT,
    event_end_date TEXT,
    event_venue TEXT,
    event_country TEXT,
    event_description TEXT,
    event_url TEXT
)
''')

# Function to load data from CSV to the SQLite database
def load_data(file_path, table_name, columns):
    with open(file_path, newline='',encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            placeholders = ', '.join(['?'] * len(columns))
            column_names = ', '.join(columns)
            sql = f'INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})'
            cursor.execute(sql, [row[col] for col in columns])
        conn.commit()

# Load data from CSV files
load_data('company_info.csv', 'company', [
    'company_logo_text', 'company_name', 'relation_to_event', 'event_url', 
    'company_revenue', 'n_employees', 'company_phone', 'company_founding_year', 
    'company_address', 'company_industry', 'company_overview', 'homepage_url', 
    'linkedin_company_url', 'homepage_base_url', 'company_logo_url_on_event_page', 
    'company_logo_match_flag'
])

load_data('people_info.csv', 'people', [
    'first_name', 'middle_name', 'last_name', 'job_title', 'person_city', 
    'person_state', 'person_country', 'email_pattern', 'homepage_base_url', 
    'duration_in_current_job', 'duration_in_current_company'
])

load_data('event_info.csv', 'event', [
    'event_logo_url', 'event_name', 'event_start_date', 'event_end_date', 
    'event_venue', 'event_country', 'event_description', 'event_url'
])

# Close the connection
conn.close()

print("Data loaded successfully.")
