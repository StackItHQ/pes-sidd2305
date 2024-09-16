import sqlite3

def connect_to_db():
    """Create a connection to the SQLite database."""
    try:
        conn = sqlite3.connect('sync_db.db')
        print("Connected to the SQLite database successfully.")
        return conn
    except sqlite3.Error as e:
        print(f"An error occurred while connecting to the SQLite database: {e}")
        return None

def delete_all_records():
    """Delete all records from the sync_table in the SQLite database."""
    with connect_to_db() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM sync_table')  # This deletes all rows from the table
        conn.commit()  # Commit the transaction to save the changes
    print("All records deleted successfully!")
delete_all_records()