# plots.py
from __future__ import annotations
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Choose a palette (Plotly built-in: "Set2", "Pastel1", "Dark2", etc.)
COLOR_SEQ = px.colors.qualitative.Set2

def headcount_by_department(df: pd.DataFrame):
    dff = df.groupby("Department", dropna=True, as_index=False).size()
    fig = px.bar(
        dff,
        x="Department",
        y="size",
        labels={"size": "Employees"},
        title="Headcount by Department",
        color="Department",
        color_discrete_sequence=COLOR_SEQ
    )
    fig.update_layout(margin=dict(l=10, r=10, t=50, b=10))
    return fig

def age_distribution(df: pd.DataFrame):
    # Box plot
    box = px.box(
        df,
        x="Department",
        y="Age",
        color="Department",
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    # Scatter plot (dots on top of box)
    scatter = px.strip(
        df,
        x="Department",
        y="Age",
        color="Department",
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    # Combine: box + dots
    fig = go.Figure(data=box.data + scatter.data)

    # Layout tweaks
    fig.update_traces(jitter=0.3, marker=dict(size=6, opacity=0.6), selector=dict(type="scatter"))
    fig.update_layout(
        title="Age Distribution by Department",
        xaxis_title="Department",
        yaxis_title="Age",
        margin=dict(l=10, r=10, t=50, b=10),
        showlegend=False
    )

    return fig

def vacation_taken_by_department(df: pd.DataFrame):
    dff = df.groupby("Department", dropna=True, as_index=False)["Vacation Days Taken"].sum()
    fig = px.bar(
        dff,
        x="Department",
        y="Vacation Days Taken",
        labels={"Vacation Days Taken": "Total Vacation Days Taken"},
        title="Vacation Days Taken by Department",
        color="Department",
        color_discrete_sequence=COLOR_SEQ
    )
    fig.update_layout(margin=dict(l=10, r=10, t=50, b=10))
    return fig
