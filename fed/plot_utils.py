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
        labels={"GDP": "GDP (in USD)", "Year": "Year"},
    )
    # add shaded region for 2008–2009
    fig.add_vrect(
        x0="2008", x1="2009",
        fillcolor="red",
        opacity=0.2,
        layer="below",
        line_width=0,
    )

    # optional annotation label
    fig.add_annotation(
        x="2008.5", y=max(df["GDP"]),
        text="Global Financial Crisis",
        showarrow=False,
        font=dict(size=12, color="red")
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
        labels={"GDP": "GDP (in USD)", "Year": "Year"},
    )
    # add shaded region for 2008–2009
    fig.add_vrect(
        x0="2008", x1="2009",
        fillcolor="red",
        opacity=0.2,
        layer="below",
        line_width=0,
    )

    # optional annotation label
    fig.add_annotation(
        x="2008.5", y=max(df["GDP"]),
        text="Global Financial Crisis",
        showarrow=False,
        font=dict(size=12, color="red")
    )
    fig.update_traces(line=dict(width=3))
    fig.show()
