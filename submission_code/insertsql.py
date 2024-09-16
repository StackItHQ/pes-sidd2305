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


def insert_sample_records():
    """Insert some sample records into the SQLite database."""
    sample_records = [
        ('Alice Johnson', 'alice.johnson@example.com', '+1234567890'),
        ('Bob Smith', 'bob.smith@example.com', '+0987654321'),
        ('Charlie Brown', 'charlie.brown@example.com', '+1122334455'),
        ('David Lee', 'david.lee@example.com', '+5566778899'),
        ('Eva Davis', 'eva.davis@example.com', '+9988776655')
    ]
    
    with connect_to_db() as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO sync_table (name, email, phone_number) VALUES (?, ?, ?)", sample_records)
        conn.commit()
    
    print("Sample records inserted into SQLite database successfully!")
insert_sample_records()