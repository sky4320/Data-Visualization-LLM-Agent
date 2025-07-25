import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from backend.llm_handler import generate_sql
from backend.query_executor import run_query

# Page config
st.set_page_config(page_title="LLM Data Analyst", layout="wide")
st.title("💬 LLM-driven Conversational Data Analyst")
st.markdown("Ask questions in natural language and get insights with SQL and visual charts!")

# Sidebar
st.sidebar.header("🛠️ Settings")
language = st.sidebar.selectbox("Select Language", ["English", "Spanish", "French"], index=0)
chart_type = st.sidebar.radio("📈 Chart Type", ["Auto", "Bar", "Pie", "Line"])

# Input box
user_query = st.text_input("🔎 Enter your data question here:")

# Session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Placeholders
sql_output_placeholder = st.empty()
data_output_placeholder = st.empty()
chart_output_placeholder = st.empty()

# Main logic
if user_query:
    with st.spinner("Generating SQL and fetching data..."):
        try:
            # 1. Connect to DB
            conn = sqlite3.connect("Chinook_Sqlite.sqlite")

            # 2. Generate SQL from NL
            generated_sql = generate_sql(user_query, conn)
            sql_output_placeholder.code(generated_sql, language="sql")

            # 3. Run SQL
            df = run_query(generated_sql)

            # 4. Show result table or error
            if isinstance(df, str):
                st.error(df)
            elif df.empty:
                st.warning("No results found.")
            else:
                data_output_placeholder.dataframe(df)

                # 5. Chart
                if chart_type == "Auto":
                    if df.shape[1] == 2 and df.dtypes[1] in ("int64", "float64"):
                        fig = px.bar(df, x=df.columns[0], y=df.columns[1])
                    else:
                        fig = None
                elif chart_type == "Bar":
                    fig = px.bar(df, x=df.columns[0], y=df.columns[1])
                elif chart_type == "Pie":
                    fig = px.pie(df, names=df.columns[0], values=df.columns[1])
                elif chart_type == "Line":
                    fig = px.line(df, x=df.columns[0], y=df.columns[1])

                if fig:
                    chart_output_placeholder.plotly_chart(fig, use_container_width=True)
                else:
                    st.info("No suitable chart could be generated.")

            conn.close()
            st.session_state.history.append(user_query)

        except Exception as e:
            st.error(f"❌ Unexpected error: {e}")

# History
with st.expander("🕒 View Query History"):
    for i, q in enumerate(st.session_state.history[::-1]):
        st.markdown(f"**{len(st.session_state.history)-i}.** {q}")
