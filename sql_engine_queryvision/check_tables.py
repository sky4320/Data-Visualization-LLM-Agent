
import os
import sqlite3

def list_tables_and_columns(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Get all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]

    print("Tables and Columns in Database:\n")

    for table in tables:
        print(f"*****{table}*****")
        try:
            # Get column names for each table
            cursor.execute(f"PRAGMA table_info({table});")
            columns = [col[1] for col in cursor.fetchall()]
            for col in columns:
                print(f" - {col}")
        except Exception as e:
            print(f"Error fetching columns: {e}")
        print()

    conn.close()

if __name__ == "__main__":
    # Always use the Chinook_Sqlite.sqlite in the sql_engine_queryvision directory relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "Chinook_Sqlite.sqlite")
    if not os.path.exists(db_path):
        print(f"Error: Database file not found at {db_path}")
        exit(1)
    list_tables_and_columns(db_path)
