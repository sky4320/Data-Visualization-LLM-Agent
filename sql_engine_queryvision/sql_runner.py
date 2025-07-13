import sqlite3
import pandas as pd
import logging

logging.basicConfig(
    filename = "query_logs.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def run_query(user_sql):
    try:
        # Connect to Chinook SQLite DB
        conn = sqlite3.connect("Chinook_Sqlite.sqlite")
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