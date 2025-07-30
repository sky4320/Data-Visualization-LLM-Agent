
import os
import sqlite3
import pandas as pd
from tabulate import tabulate
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("Insert your OpenAI API key here"))

# Connect to SQLite database
db_path = "Chinook_Sqlite.sqlite"  # Ensure this is your actual file
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get schema from DB dynamically
def get_schema():
    schema = ""
    tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    for table in tables:
        table_name = table[0]
        columns = cursor.execute(f"PRAGMA table_info({table_name});").fetchall()
        col_names = [col[1] for col in columns]
        schema += f"Table: {table_name} | Columns: {', '.join(col_names)}\n"
    return schema

schema = get_schema()
print("\nDatabase Schema Loaded.\n")
print(schema)

# Function to generate SQL from natural language using GPT-4
def generate_sql(natural_query):
    prompt = f"""
    You are an expert SQL assistant. Convert the following natural language request into a valid SQLite SQL query.
    STRICT RULES:
    1. Use ONLY tables and columns from this schema.
    2. Use the table names exactly as provided (case-sensitive).
    3. Return ONLY a valid SELECT or WITH statement. Do not include markdown, ```sql, or extra text.
    4. Do not assume any plural forms.
    Database Schema:
    {schema}
    
    Question: {natural_query}
    """
    response = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )
    sql_query = response.output_text.strip()
    return sql_query

print("\nQueryVision (GPT-4): Natural Language → SQL → Results\n")

# Main loop
while True:
    question = input("Enter your question (or type 'exit'): ")
    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Generate SQL query
    sql_query = generate_sql(question)
    print("\nGenerated SQL:\n", sql_query)

    # Validate only SELECT or WITH queries
    if not (sql_query.strip().lower().startswith("select") or sql_query.strip().lower().startswith("with")):
        print("\nError: Only SELECT or WITH queries are allowed!")
        continue

    try:
        # Execute query
        result = pd.read_sql_query(sql_query, conn)
        if result.empty:
            print("\nNo results found.")
        else:
            print("\nQuery Results:")
            print(tabulate(result, headers='keys', tablefmt='psql'))
    except Exception as e:
        print("\nError executing query:", e)

# ------------------------------
# Haris - Added for integration with app_controller.py
# Wrapper function that takes a natural language query,
# generates SQL using the existing generate_sql function,
# executes it on the connected SQLite database,
# and returns the results as a Pandas DataFrame.
# ------------------------------
def run_query(natural_query: str) -> pd.DataFrame:
    try:
        # Step 1: Generate SQL from the natural language query
        sql = generate_sql(natural_query)
        # Debugging output
        print(f"[DEBUG] Generated SQL: {sql}")

        # Step 2: Execute the SQL query on the database
        df = pd.read_sql_query(sql, conn)

        # Step 3: Return the query results as a DataFrame
        return df

    except Exception as e:
        print(f"[ERROR] Failed to process query: {e}")
        # Return empty DataFrame so visualizer doesn’t break
        return pd.DataFrame()