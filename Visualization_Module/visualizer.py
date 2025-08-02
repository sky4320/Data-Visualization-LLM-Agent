"""
Core visualization logic to render SQL query results into visual formats.
Supports tables, bar charts, pie charts, and line graphs.
"""

import pandas as pd
import plotly.express as px
import streamlit as st
from .chart_utils import format_chart_layout, apply_accessibility_settings

def detect_chart_type(df: pd.DataFrame) -> str:
    # If only two columns and one is numeric, suggest a bar or pie chart
    if df.shape[1] == 2:
        if pd.api.types.is_numeric_dtype(df.iloc[:, 1]):
            if df.shape[0] <= 10:
                return 'pie'
            return 'bar'
    # If the first column appears to be time or index data, use line chart
    if 'date' in df.columns[0].lower() or 'time' in df.columns[0].lower():
        return 'line'
    # Default fallback to tabular view
    return 'table'

def generate_visualization(df: pd.DataFrame):
    # Guard clause for empty data
    if df.empty:
        st.warning("No data available to visualize.")
        return

    # Detect the best chart type based on data
    chart_type = detect_chart_type(df)

    # Render bar chart
    if chart_type == 'bar':
        fig = px.bar(df, x=df.columns[0], y=df.columns[1], title="Bar Chart")
        fig.update_layout(format_chart_layout("Bar Chart", df.columns[0], df.columns[1]))
        fig = apply_accessibility_settings(fig)
        st.plotly_chart(fig)

    # Render pie chart
    elif chart_type == 'pie':
        fig = px.pie(df, names=df.columns[0], values=df.columns[1], title="Pie Chart")
        fig.update_layout(format_chart_layout("Pie Chart"))
        fig = apply_accessibility_settings(fig)
        st.plotly_chart(fig)

    # Render line chart
    elif chart_type == 'line':
        fig = px.line(df, x=df.columns[0], y=df.columns[1], title="Line Chart")
        fig.update_layout(format_chart_layout("Line Chart", df.columns[0], df.columns[1]))
        fig = apply_accessibility_settings(fig)
        st.plotly_chart(fig)

    # Render table if no suitable chart is found
    else:
        st.dataframe(df)
