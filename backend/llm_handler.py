from dotenv import load_dotenv
import os
from pathlib import Path
from openai import OpenAI

# Load .env from the project root
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("OPENAI_API_KEY")
print("API Key from env:", api_key)

client = OpenAI(api_key=api_key)


#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Set in .env or environment')


#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Set in .env or environment

def get_schema(cursor):
    schema = ""
    tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    for table in tables:
        table_name = table[0]
        columns = cursor.execute(f"PRAGMA table_info({table_name});").fetchall()
        col_names = [col[1] for col in columns]
        schema += f"Table: {table_name} | Columns: {', '.join(col_names)}\n"
    return schema

def generate_sql(natural_query, conn):
    cursor = conn.cursor()
    schema = get_schema(cursor)
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
