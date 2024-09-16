import streamlit as st
import sqlite3
import gspread
import hashlib
import time
from google.oauth2.service_account import Credentials
import pandas as pd

# Google Sheets setup
SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file('credentials.json', scopes=SCOPE)
client = gspread.authorize(creds)
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/187uudwa8AuEx_2XFm2RT29SKCj7l1KRBEF2ooVbVYBg/edit#gid=0')
worksheet = sheet.get_worksheet(0)

# Database functions
def connect_to_db():
    """Create a connection to the SQLite database."""
    return sqlite3.connect('sync_db.db')

def create_table():
    """Create the table if it doesn't already exist."""
    with connect_to_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sync_table (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                phone_number TEXT
            )
        ''')
        conn.commit()

def get_sheet_data():
    """Fetch all data from the Google Sheet."""
    return worksheet.get_all_values()

def hash_data(data):
    """Generate a hash of the data."""
    data_string = ''.join([''.join(row) for row in data])
    return hashlib.sha256(data_string.encode()).hexdigest()

def sync_google_sheets_to_sqlite(data):
    """Sync data from Google Sheets to the SQLite database."""
    with connect_to_db() as conn:
        cursor = conn.cursor()

        # Clear the SQLite table
        cursor.execute("DELETE FROM sync_table")

        # Insert data from Google Sheets into SQLite
        for i in range(1, len(data)):  # Skip the header row
            row = data[i]
            if len(row) == 3:
                cursor.execute("INSERT INTO sync_table (name, email, phone_number) VALUES (?, ?, ?)", row)

        conn.commit()
    print("Google Sheets data synced to SQLite successfully!")  # Log to console

def batch_sync_sqlite_to_google_sheets(batch_size=100):
    """Sync data from the SQLite database to Google Sheets in batches."""
    with connect_to_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, email, phone_number FROM sync_table")
        rows = cursor.fetchall()

    # Clear existing data in the Google Sheet and insert headers
    worksheet.clear()  # Clears all the content in the sheet
    worksheet.append_row(["Name", "Email", "Phone Number"])

    # Insert SQLite rows back to Google Sheets in batches
    for i in range(0, len(rows), batch_size):
        batch = rows[i:i + batch_size]
        worksheet.append_rows(batch)

    print("SQLite data synced to Google Sheets successfully in batches!")  # Log to console

# Create the table if it doesn't exist
create_table()

# Streamlit app
st.title("Siddhanth - SuperJoin Assignment🚀")

# Initialize session state
if 'monitoring' not in st.session_state:
    st.session_state.monitoring = False
if 'last_data_hash' not in st.session_state:
    st.session_state.last_data_hash = hash_data(get_sheet_data())

def update_data():
    """Update the data from Google Sheets to SQLite if changes are detected, and sync SQLite to Google Sheets."""
    current_data = get_sheet_data()
    current_data_hash = hash_data(current_data)
    if current_data_hash != st.session_state.last_data_hash:
        st.write("Change detected. Syncing data...")
        sync_google_sheets_to_sqlite(current_data)
        st.session_state.last_data_hash = current_data_hash  # Update hash to current state

    # Sync changes from SQLite to Google Sheets
    batch_sync_sqlite_to_google_sheets()

# Button for starting/stopping monitoring
if st.button("Start Monitoring Changes"):
    st.session_state.monitoring = True

if st.button("Stop Monitoring Changes"):
    st.session_state.monitoring = False

# Periodic update
if st.session_state.monitoring:
    update_data()
    time.sleep(10)  # Check every 10 seconds
    st.experimental_rerun()  # Rerun the app to continue monitoring

# Button to show table data
if st.button("Show Table Data"):
    with connect_to_db() as conn:
        df = pd.read_sql_query("SELECT * FROM sync_table", conn)
    if df.empty:
        st.write("No data found in the table.")
    else:
        st.write(df)
