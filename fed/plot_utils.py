import plotly.express as px
import pandas as pd

def plot_single(df: pd.DataFrame, country: str):
    """Plot GDP over time for a single country."""
    country_df = df[df["Country"] == country]

    fig = px.line(
        country_df,
        x="Year",
        y="GDP",
        title=f"GDP Between 2000 and 2022 for {country}",
    )

    fig.update_traces(line=dict(width=3))
    fig.show()

def plot_multiple_countries(df: pd.DataFrame):
    """Plot GDP comparison for all countries in the dataset."""
    fig = px.line(
        df,
        x="Year",
        y="GDP",
        color="Country",
        title="GDP Comparison: 2000–2022",
    )

    fig.update_traces(line=dict(width=3))
    fig.show()
