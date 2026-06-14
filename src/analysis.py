import pandas as pd
import os

RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data-raw")
CLEAN_DIR = os.path.join(os.path.dirname(__file__), "..", "data-processed")
os.makedirs(CLEAN_DIR, exist_ok=True)

def normalize_inverse(series: pd.Series) -> pd.Series:
    return 1 + 9 * (series.max() - series) / (series.max() - series.min())

def normalize_direct(series: pd.Series) -> pd.Series:
    return 1 + 9 * (series - series.min()) / (series.max() - series.min())

def score_regions() -> pd.DataFrame:
    df = pd.read_csv(os.path.join(RAW_DIR, "wholesale_prices.csv"))
    
    df["price_score"] = normalize_inverse(df["price_2024"]).round(2)
    df["interconnection_score"] = normalize_inverse(df["interconnection_wait_years"]).round(2)
    df["renewable_score"] = normalize_inverse(df["renewable_pct_2024"]).round(2)
    
    df["total_score"] = (
        df["price_score"] * 0.40 +
        df["interconnection_score"] * 0.40 +
        df["renewable_score"] * 0.20
    ).round(2)
    
    def recommend(score):
        if score >= 7.5:
            return "Top Pick"
        elif score >= 5.0:
            return "Good Option"
        else:
            return "Consider Carefully"
    
    df["recommendation"] = df["total_score"].apply(recommend)
    
    df = df.sort_values("total_score", ascending=False).reset_index(drop=True)
    
    path = os.path.join(CLEAN_DIR, "region_scores.csv")
    df.to_csv(path, index=False)
    print(f"[Analysis]  Score saved -> {path}")
    return df

if __name__ == "__main__":
    df = score_regions()
    print("\n── Regional Ranking ──────────────────────────")
    print(df[["hub", "region", "price_score", "interconnection_score",
            "renewable_score", "total_score", "recommendation"]].to_string(index=False))