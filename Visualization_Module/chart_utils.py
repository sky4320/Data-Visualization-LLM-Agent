"""
Helper utilities for customizing and rendering charts.
"""

import plotly.graph_objects as go

def format_chart_layout(title="Chart", x_title=None, y_title=None):
    # Return a Plotly layout object with common settings
    return go.Layout(
        title=title,
        xaxis=dict(title=x_title),
        yaxis=dict(title=y_title),
        margin=dict(l=40, r=40, t=40, b=40),
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(size=12)
    )

def apply_accessibility_settings(fig):
    # Improves contrast and font sizing for accessibility
    fig.update_layout(
        font=dict(size=14),
        legend=dict(orientation="h", y=-0.2),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    return fig
