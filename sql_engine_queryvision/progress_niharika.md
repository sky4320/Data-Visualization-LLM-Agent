# *Backend Progress Summary – Niharika*
*Project*: Data Visualization LLM Agent  
*Role*: LLM Integration & Natural Language → SQL Conversion  
*Team*: Dallas AI Summer 2025 – Team QueryVision  

---

## *Overview*
My role focused on integrating the GPT-powered LLM (Large Language Model) to translate natural language questions into accurate SQL queries and enabling smooth interaction between the AI model and the database backend. The objective was to ensure the model-generated queries are syntactically correct, context-aware, and compatible with the Chinook database schema.

---

## *Completed Work*

### *1. OpenAI API Integration*
- Set up *OpenAI GPT-4* model for text-to-SQL conversion.
- Created an nl_2_sql_runner_OPENAI.py script that:
  - Accepts user input in natural language.
  - Sends the prompt along with the *database schema* to GPT for better query accuracy.
  - Returns a clean SQL query by enforcing strict formatting rules (only SQL code, no extra text).

---

### *2. Database Schema Context*
- Implemented a *schema extraction function* to dynamically fetch:
  - All table names.
  - Their columns from the SQLite database.
- Included schema in the prompt to improve GPT-generated query accuracy.
- Verified that the generated queries align with Chinook's schema, e.g.:
  - *Tables*: Customer, Invoice, Track, Album, Artist, etc.
  - *Columns*: CustomerId, FirstName, LastName, Email, etc.

---

### *3. Query Execution with Safety*
- Integrated GPT-generated SQL queries with pandas.read_sql_query() for safe execution.
- Implemented validation to ensure only *SELECT* or *WITH* statements are executed.
- Added error handling for:
  - Syntax issues in GPT-generated queries.
  - Missing or incorrect table/column names.
- Ensured that the execution fails gracefully and displays clear error messages to the user.

---

### *4. Iterative Debugging & Optimization*
- Resolved issues with:
  - GPT generating incomplete queries.
  - Incorrect table names (e.g., generating customers instead of Customer).
- Added prompt tuning to ensure accurate capitalization and syntax based on the Chinook DB.
- Verified output by comparing generated SQL with manual queries.

---

### *5. Interactive Query Flow*
- Built a loop for continuous user interaction:
  - *Step 1*: User enters natural language query.
  - *Step 2*: GPT converts it to SQL.
  - *Step 3: System executes and displays results in a **tabular format* using tabulate.
- Added support for multiple queries until the user types exit.

---

## *Setup & Execution Guide (For Teammates)*

### *Prerequisites*
Install Python and dependencies:
```bash
pip install openai pandas tabulate

---

### *Set your OpenAI API Key*
export OPENAI_API_KEY="your_api_key"    # Linux/Mac
$env:OPENAI_API_KEY="your_api_key"      # Windows PowerShell
