import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data-raw")
PROCESSED_DIR = os.path.join(os.path.dirname(__file__), "..", "data-processed")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def build_dashboard():
    prices = pd.read_csv(os.path.join(RAW_DIR, "Wholesale_prices.csv"))
    scores = pd.read_csv(os.path.join(PROCESSED_DIR, "region_scores.csv"))
    capacity = pd.read_csv(os.path.join(RAW_DIR, "renewable_capacity.csv"))
    
    color_map = {
        "Top Pick": "#3fb950",
        "Good Option": "#d29922",
        "Consider Carefully": "#f85149"
    }
    colors = scores["recommendation"].map(color_map).tolist()
    
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=(
            "Regional Energy Procurement Score",
            "Wholesale Electricity Prices 2022-2025 ($/MWh)",
            "Interconnection Queue Wait Time (years)",
            "Renewable Capacity by State (GW)"
        ),
        vertical_spacing=0.18,
        horizontal_spacing=0.12
    )
    
    fig.add_trace(
        go.Bar(
            x=scores["hub"],
            y=scores["total_score"],
            marker_color=colors,
            text=scores["recommendation"],
            textposition="outside",
            name="Total Score"
        ),
        row=1, col=1
    )
    
    for _, row in prices.iterrows():
        fig.add_trace(
            go.Scatter(
                x=["2022", "2023", "2024", "2025F"],
                y=[row["price_2022"], row["price_2023"], row["price_2024"], row["price_2025_forecast"]],
                mode="lines+markers",
                name=row["hub"],
                showlegend=True
            ),
            row=1, col=2
        )
        
    fig.add_trace(
        go.Bar(
            x=scores["interconnection_wait_years"],
            y=scores["hub"],
            orientation="h",
            marker_color="#58a6ff",
            name="Wait years"
        ),
        row=2, col=1
    )
    
    for tech, group in capacity.groupby("technology"):
        fig.add_trace(
            go.Bar(
                x=group["state"],
                y=group["capacity_gw"],
                name=tech,
                text=group["capacity_gw"],
                textposition="outside"
            ),
            row=2, col=2
        )
        
    fig.update_layout(
        title={
            "text": "US Energy Market Analysis for Data Center Procurement - 2024",
            "font": {"size": 18}
        },
        height=900,
        template="plotly_dark",
        legend=dict(orientation="h", y=-0.12),
        paper_bgcolor="#0d1117",
        plot_bgcolor= "#0d1117",
        font=dict(color="#e6edf3")
    )
    
    fig.update_yaxes(range=[0, 11], row=1, col=1)
    
    path = os.path.join(OUTPUT_DIR, "dashboard.html")
    fig.write_html(path)
    print(f"[Dashboard] Saved -> {path}")
    
if __name__ == "__main__":
    build_dashboard()
