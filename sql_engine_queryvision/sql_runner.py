
import sqlite3
import pandas as pd
import logging
import os

# Always use the absolute path for DB and log file
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "Chinook_Sqlite.sqlite")
log_path = os.path.join(script_dir, "query_logs.log")

logging.basicConfig(
    filename = log_path,
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def run_query(user_sql):
    try:
        # Connect to Chinook SQLite DB (always use absolute path)
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Allow only SELECT and WITH queries (CTEs)
        safe_start = ("select", "with")
        if not user_sql.strip().lower().startswith(safe_start):
            return "Only SELECT or WITH queries are allowed!"

        # Run the query
        cursor.execute(user_sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(rows, columns=columns)

        # Close DB connection
        conn.close()
        logging.info(f"SUCCESS: {user_sql}")
        return df

    except Exception as e:
        logging.error(f"ERROR: {user_sql} - {str(e)}")
        return f"Error: {str(e)}"


# # Sample Query to Test
# if __name__ == "__main__":
#     sample_sql = """
#     WITH usa_customers AS (
#     SELECT CustomerId, FirstName, Country
#     FROM Customer
#     WHERE Country = 'USA'
#     )
#     SELECT * FROM usa_customers LIMIT 5;
#     """

#     result = run_query(sample_sql)
#     print(result)