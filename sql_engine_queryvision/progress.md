# Backend Progress Summary – Siva Keshav
**Project**: Data Visualization LLM Agent
**Role**: Database & Query Execution
**Team**: Dallas AI Summer 2025 – Team QueryVision

---

## Overview
As part of my role, I built the backend SQL execution component for QueryVision. The goal was to provide a clean, reliable, and secure function that takes SQL queries (from a UI or LLM), runs them on the Chinook database, and returns readable results with proper error handling and logging. The logic is designed to be modular and easy to integrate.

---

## Completed Work

### 1. Chinook Database Setup
- Downloaded `Chinook_Sqlite.sqlite` and placed it in the project folder.
- Verified the file using Python scripts to ensure that all expected tables and data are available.

### 2. Core Query Execution (`sql_runner.py`)
- Created a function `run_query(sql_query)` which:
- Connects to the SQLite database
- Executes read-only queries (`SELECT`, `WITH`)
- Returns a pandas DataFrame if successful
- Returns error messages gracefully if the query fails
- Includes validation to reject unsafe queries (e.g., `INSERT`, `DROP`, etc.)
- Integrated logging for both success and error cases

### 3. Logging Setup
- Logs are saved in `query_logs.log`
- Each entry includes:
- Timestamp
- Query
- Result type (Success or Error)
- Helps with debugging and query tracking

### 4. Schema Explorer (`check_tables.py`)
- Built a script that prints all table names and their columns from the Chinook database
- Makes it easier for the LLM or frontend team to understand the database structure

Example:
```
Customer: CustomerId, FirstName, LastName, Email
Invoice: InvoiceId, CustomerId, Total, InvoiceDate
```

### 5. Query Testing Script (`query_tests.py`)
- Contains a list of test queries to validate different use cases
- Uses the `tabulate` library for clean output formatting in the terminal
- Includes successful queries, joins, CTEs, and intentional errors

---

## Setup & Execution Guide (For Teammates)

### Prerequisites
Install Python (version 3.8 or higher recommended):
https://www.python.org/downloads

Install required libraries:
```bash
pip install pandas tabulate
```

---

### File Structure Example

```
queryvision_sql_engine/
├── sql_runner.py
├── query_tests.py
├── check_tables.py
├── Chinook_Sqlite.sqlite
└── query_logs.log (auto-created)
```

---

### How to Use:

**A. Run test queries**
```bash
python query_tests.py
```

**B. View database structure**
```bash
python check_tables.py
```

**C. View logs**
Open `query_logs.log` in any editor or use terminal:
```bash
cat query_logs.log
```

---

## File Reference

| File | Purpose |
|------|---------|
| `sql_runner.py` | Core query execution logic with logging and safety |
| `query_tests.py` | Contains multiple test queries and formats output |
| `check_tables.py` | Utility to list all tables and their columns |
| `Chinook_Sqlite.sqlite` | The sample SQLite database |
| `query_logs.log` | Automatically created; stores success and error logs |

---

## Current Status

- Backend functionality is complete and tested
- Modular and ready for integration with LLM or frontend
- All major query types (joins, aggregates, CTEs, etc.) are supported
- Logging and schema inspection are built-in

---

## Optional Enhancements (Future Work)

- Log query execution time
- Export results to CSV/JSON
- Add REST API endpoint for query execution
- Create a query history or template feature

---

## Final Note

This backend is production-ready and flexible. If anyone on the team needs help with integration, testing, or enhancements, I’m happy to assist. Everything has been designed to plug in easily with the rest of the system.
