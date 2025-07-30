"""
app_controller.py
Controller script that integrates natural language to SQL (via nl_2_sql_runner_OPENAI.py)
with the visualization module to provide an end-to-end pipeline.
"""

from sql_engine_queryvision.nl_2_sql_runner_OPENAI import run_query
from Visualization_Module.visualizer import generate_visualization

def handle_query(user_input: str):
    """
    Takes a user's natural language input, generates SQL, executes it,
    retrieves the results as a DataFrame, and passes it to the visualizer.
    """
    try:
        # Run the query and get results
        df = run_query(user_input)

        # If results are empty, notify the user
        if df.empty:
            print("No results found for your query.")
            return

        # Visualize the query results
        generate_visualization(df)

    except Exception as e:
        print(f"Error processing query: {e}")

if __name__ == "__main__":
    print("Welcome to the AI Data Chatbot!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Ask a question about your data: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        handle_query(user_input)
