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
    list_tables_and_columns("Chinook_Sqlite.sqlite")
