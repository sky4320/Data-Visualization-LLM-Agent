

import sqlite3
import pandas as pd
import logging
import os

def run_query(sql_query, db_path, log_path=None):
    if log_path is None:
        # Always use the project root for logs
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_path = os.path.join(project_root, "query_logs.log")
    # Always set logging config with format before any logging
    logging.basicConfig(filename=log_path, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
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
