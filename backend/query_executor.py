import sqlite3
import pandas as pd
import logging

logging.basicConfig(filename="query_logs.log", level=logging.INFO)

def run_query(sql_query, db_path="Chinook_Sqlite.sqlite"):
    try:
        conn = sqlite3.connect(db_path)
        if not sql_query.strip().lower().startswith(("select", "with")):
            return "Only SELECT or WITH queries are allowed!"

        df = pd.read_sql_query(sql_query, conn)
        conn.close()
        logging.info(f"SUCCESS: {sql_query}")
        return df
    except Exception as e:
        logging.error(f"ERROR: {sql_query} - {str(e)}")
        return f"Error: {str(e)}"
