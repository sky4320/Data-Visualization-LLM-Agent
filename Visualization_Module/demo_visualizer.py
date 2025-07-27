"""
Standalone demo script for testing visualizer.py with mock data.
Run this file using: `streamlit run demo_visualizer.py`
"""

import streamlit as st
import pandas as pd
from visualizer import generate_visualization

# Title
st.title("LLM Chatbot: Visualization Module Demo")

# Dropdown to select a chart type scenario
chart_type = st.selectbox("Select a sample data type to visualize", ["Bar Chart", "Pie Chart", "Line Chart", "Table"])

# Load sample data based on selected chart type
if chart_type == "Bar Chart":
    df = pd.DataFrame({
        "Product": ["Apples", "Oranges", "Bananas", "Grapes", "Berries"],
        "Sales": [150, 200, 90, 120, 180]
    })

elif chart_type == "Pie Chart":
    df = pd.DataFrame({
        "Category": ["A", "B", "C", "D"],
        "Count": [45, 30, 15, 10]
    })

elif chart_type == "Line Chart":
    df = pd.DataFrame({
        "Date": pd.date_range(start="2023-01-01", periods=10),
        "Visitors": [100, 150, 120, 130, 180, 160, 200, 190, 210, 230]
    })

else:  # Table view
    df = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Score": [88, 92, 79, 85]
    })

# Show raw data
st.subheader("Raw Data")
st.dataframe(df)

# Show visual output
st.subheader("Visualization Output")
generate_visualization(df)
